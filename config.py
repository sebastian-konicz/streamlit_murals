import os
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# Pobierz klucz API z .env

CLOUDINARY_CONFIG = {
    'cloud_name': os.getenv("CLOUDINARY_CLOUD_NAME"),
    'api_key': os.getenv("CLOUDINARY_API_KEY"),
    'api_secret': os.getenv("CLOUDINARY_API_SECRET"),
    'api_environment': os.getenv("CLOUDINARY_ENVIRONMENT")
}

FIREBASE_CONFIG = {
    'apiKey': "your_api_key",
    'authDomain': "your_auth_domain",
    'projectId': "your_project_id",
}