import requests
import os
from dotenv import load_dotenv
from PIL import Image


img_folder = os.getenv("IMG_FOLDER")


image = Image.open("ps12_16x20.jpg")

if image.width > image.height:
    delta = (image.width - image.height)/2
    coordinates = (delta, 0, image.width - delta, image.height)
    cropped = image.crop(coordinates)
    cropped.thumbnail((1080, 1080))
    cropped.save("cropped_insta.jpg")
else:
    delta = (image.height - image.width)/2
    coordinates = (0, delta, image.width, image.height - delta)
    cropped = image.crop(coordinates)
    cropped.thumbnail((1080, 1080))
    cropped.save("cropped_insta.jpg")
