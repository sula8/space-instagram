from instabot import Bot
from os import listdir
import time


def insta_upload(login, password, crop_folder):
    bot = Bot()
    bot.login(username=login, password=password)

    for img in listdir(crop_folder):
        bot.upload_photo(f"./{crop_folder}/{img}", caption=f"Просто космос! Файл {img}")
        time.sleep(30)
