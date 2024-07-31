from PIL import Image
from django.shortcuts import get_object_or_404
from celery import shared_task
import time

from .models import Image as Image_model
@shared_task()
def img_to_grayscale_task(img, img_name, img_modle_id):
    img = img.replace('~/' , '')
    image_file = Image.open(img).convert('L')
    time.sleep(15)
    image_file.save(f"media/processed/P_{img_name}") 
    up_image = get_object_or_404(Image_model, id=img_modle_id)
    up_image.processed_image = f"processed/P_{img}"
    up_image.message = up_image.CHOICES[1]
    up_image.save()
    return f"file succusesfully processed in > processed/P_{img}"