import os
from PIL import Image
for root, dirs, files in os.walk("images/train"):
    for filename in files:
        if ".jpg" in filename:
            image_path = 'images/train/'+filename
            img = Image.open(image_path)
            width, height = img.size
            print(f"{image_path}: width:{width}, height:{height}")
            new_image = img.resize((200, 300))
            new_image.save("new_images/train/"+filename)

for root, dirs, files in os.walk("images/test"):
    for filename in files:
        if ".jpg" in filename:
            image_path = 'images/test/'+filename
            img = Image.open(image_path)
            width, height = img.size
            print(f"{image_path}: width:{width}, height:{height}")
            new_image = img.resize((200, 300))
            new_image.save("new_images/test/"+filename)
