# KPR-Hackathon

---

# Aura: AI-Powered Mall Assistant

[![GitHub Repo](https://img.shields.io/badge/GitHub-KPR--Hackathon-blue?logo=github)](https://github.com/Agiless/KPR-Hackathon.git)

> 🌟 Aura is your **personal mall companion**. It helps shoppers find stores, discover products, navigate malls in 3D, and even stay safe with real-time SOS alerts. Built during the **KPR Hackathon**, Aura reimagines the way we experience shopping malls.

---


## ❓ Why We Built Aura

If you’ve ever been lost in a mall trying to find a store, struggled to locate parking, or panicked when you couldn’t find your family in a crowd — you know the frustration.

Malls are exciting, but they can also be overwhelming. **Aura exists to make that experience effortless and safe.**

---


## 💡 What Aura Can Do

- **AI-Powered Conversational Assistant**  
  Answer queries, provide store info, directions, and highlight ongoing promotions.  

- **Visual Product Search**  
  Snap or upload a product image to instantly find matches inside the mall.  

- **3D Indoor Navigation**  
  Interactive maps with shortest-path guidance to stores, amenities, and exits.  

- **Parking & Service Finder**  
  Check real-time availability of parking spots and other mall services.  

- **SOS Safety System**  
  Trigger emergency alerts for instant community assistance.  

- **Feature Image Rendering**  
  Suggests matching accessories, clothing items, or related products based on your purchase.  

- **Credit System (Aura Coins)**  
  Earn coins by leaving genuine reviews (evaluated via majority sentiment), which can be redeemed for discounts, offers, or selected products.  

---


## 🛠️ Tech Stack

* **Frontend**: React.js, TailwindCSS, Blender (3D maps)
* **Backend**: Django REST APIs (Python)
* **Databases**: SQLite, MongoDB, Vector DB
* **AI/ML**: Qwen-3 LLM, CLIP (vision search), BFS/A\* (pathfinding)
* **Tools**: Docker, Git, Python

---

---

## ⚙️ Getting Started

Clone the repository:

```bash
git clone https://github.com/Agiless/KPR-Hackathon.git
cd KPR-Hackathon
```

### Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r ../requirements.txt
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd app
npm install
npm run dev
```

Open: [http://localhost:5173](http://localhost:5173)

### AI Modules

```bash
cd chatbot
python chatbot_main.py

cd product_search
python recommender.py
```

---

## 🖥️ Using Aura

Once servers are running, you can:

* Chat with the AI for mall queries.
* Upload product photos to search.
* Explore a **3D indoor map**.
* Trigger SOS alerts for emergencies.

Example APIs:

* `POST /api/auth/login` – login
* `GET /api/products` – fetch products
* `POST /api/products/recommend` – get recommendations

---

---

## 🗺️ Roadmap

**Phase 1 – Hackathon MVP** → Visual product search + 3D navigation.
**Phase 2 – Pilot** → Partner with a mall in Chennai/Tiruchirappalli.
**Phase 3 – Scale** → Multi-mall rollout, AR navigation, analytics dashboards.

---

## 💼 Impact

* **Shoppers** → Stress-free, safe, and smarter shopping.
* **Retailers** → More visibility, better sales via promotions & discovery.
* **Mall Management** → Insights, engagement, and real-time safety.

---


✨ Aura isn’t just a hackathon project. It’s our **vision for smarter, safer, and more engaging malls**.

---
