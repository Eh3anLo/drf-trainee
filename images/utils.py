from PIL import Image

def gray_scale(img):
    image_file = Image.open(img).convert('L')
    # image_file.show()
    image_file.save(f"media/processed/P_{img}") 
    return f"P_{img}"
