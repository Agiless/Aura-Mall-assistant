from django.utils.deprecation import MiddlewareMixin

class ForceCORSHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "https://kpr-hackathon.vercel.app"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken, Authorization"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, PATCH, DELETE"
        return response
