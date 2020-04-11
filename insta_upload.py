from instabot import Bot
import os
from os import listdir
import time


def insta_upload():
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    crop_folder = os.getenv("CROP_FOLDER")

    bot = Bot()
    bot.login(username=login, password=password)

    for img in listdir(crop_folder):
        bot.upload_photo(f"./{crop_folder}/{img}", caption=f"Просто космос! Файл {img}")
        time.sleep(30)
