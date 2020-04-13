import os
from dotenv import load_dotenv
from tools import crop_img
from fetch_hubble import fetch_hubble
from fetch_spacex import fetch_spacex
from insta_upload import insta_upload

if __name__ == "__main__":
    load_dotenv()
    img_folder = os.getenv("IMG_FOLDER")
    crop_folder = os.getenv("CROP_FOLDER")
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    fetch_spacex(img_folder)
    fetch_hubble(img_folder)
    crop_img(img_folder, crop_folder)
    insta_upload(login, password, crop_folder)
