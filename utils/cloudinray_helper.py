import cloudinary
import cloudinary.uploader
from config import CLOUDINARY_CONFIG

cloudinary.config(**CLOUDINARY_CONFIG)

def upload_image(image_path):
    result = cloudinary.uploader.upload(image_path)
    return result['url']