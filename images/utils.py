from PIL import Image
import time

def gray_scale(img):
   image_file = Image.open(img).convert('L')
   time.sleep(15)
   image_file.save(f"media/processed/P_{img}") 
   return f"processed/P_{img}"