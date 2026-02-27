import os
from dotenv import load_dotenv
import requests
from io import BytesIO
from PIL import Image
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import google.generativeai as genai

load_dotenv()

# ------------------------------
# MongoDB Setup
# ------------------------------
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://mirun:mirun2005@cluster0.wka17ox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["auraMallDB"]
products_collection = db["products"]

# ------------------------------
# Gemini AI Setup
# ------------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------------------
# Lazy Loading CLIP Model
# ------------------------------
_clip_model = None

def get_clip_model():
    global _clip_model
    if _clip_model is None:
        try:
            from sentence_transformers import SentenceTransformer
            print("Loading CLIP model...")
            _clip_model = SentenceTransformer("clip-ViT-B-32")
            print("CLIP model loaded successfully!")
        except Exception as e:
            print(f"Error loading CLIP model: {e}")
            _clip_model = None
    return _clip_model

# ------------------------------
# Index Product Images
# ------------------------------
def index_product_images():
    """
    Generate embeddings for all products and store in MongoDB.
    """
    clip_model = get_clip_model()
    if clip_model is None:
        print("Cannot index products: CLIP model not loaded.")
        return

    docs = list(products_collection.find({}))
    print(f"Found {len(docs)} products to index")

    for product in docs:
        try:
            img_url = product.get("image_url")
            product_id = product["_id"]

            if not img_url:
                print(f"⚠️ Skipping product {product_id} (no image URL)")
                continue

            # Download image
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))

            # Generate embedding
            embedding = clip_model.encode(image).tolist()

            # Save embedding
            products_collection.update_one(
                {"_id": product_id},
                {"$set": {"image_embedding": embedding}}
            )

            print(f"✅ Indexed product: {product.get('name', product_id)}")

        except Exception as e:
            print(f"❌ Failed to index product {product.get('name', product_id)}: {e}")

# ------------------------------
# Fashion Advisor
# ------------------------------
def run_fashion_advisor(user_image_path):
    """
    Given a user's uploaded image, return the top recommended product and AI text.
    """
    try:
        clip_model = get_clip_model()
        if clip_model is None:
            print("CLIP model not available.")
            return None

        # Load user image
        image = Image.open(user_image_path)

        # Generate query vector
        query_vector = clip_model.encode(image).tolist()

        # MongoDB Vector Search
        pipeline = [
            {
                "$vectorSearch": {
                    "index": "vector_index",  # Make sure your Atlas Search index matches
                    "path": "image_embedding",
                    "queryVector": query_vector,
                    "numCandidates": 150,
                    "limit": 5
                }
            },
            {
                "$project": {
                    "name": 1,
                    "brand": 1,
                    "price": 1,
                    "image_url": 1,
                    "_id": 0,
                    "score": {"$meta": "vectorSearchScore"}
                }
            }
        ]

        results = list(products_collection.aggregate(pipeline))
        if not results:
            return None

        # Use Gemini AI to generate text
        gemini_model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"""
        You are a friendly salesperson. Recommend this product in 1-2 lines.
        Product Name: {results[0]['name']}
        Brand: {results[0]['brand']}
        Price: ₹{results[0]['price']}
        """

        response = gemini_model.generate_content(prompt)
        return results[0]["image_url"], response.text

    except Exception as e:
        print(f"Error in run_fashion_advisor: {e}")
        return None
