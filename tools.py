import requests
import os
from PIL import Image
from os import listdir


def download_img(url, filename):
  img_folder = os.getenv("IMG_FOLDER")
  os.makedirs(img_folder, exist_ok=True)
  file_path = os.path.join(img_folder, filename)

  response = requests.get(url)
  response.raise_for_status()

  with open(file_path, 'wb') as file:
    file.write(response.content)


def crop_img():
    img_folder = os.getenv("IMG_FOLDER")
    crop_folder = os.getenv("CROP_FOLDER")
    os.makedirs(crop_folder, exist_ok=True)

    for img in listdir(img_folder):
        image = Image.open(f"./{img_folder}/{img}")

        if image.width > image.height:
            delta = (image.width - image.height)/2
            coordinates = (delta, 0, image.width - delta, image.height)
        else:
            delta = (image.height - image.width)/2
            coordinates = (0, delta, image.width, image.height - delta)

        cropped = image.crop(coordinates)
        cropped.thumbnail((1080, 1080))
        cropped.save(f"./{crop_folder}/{img}", format="JPEG")


