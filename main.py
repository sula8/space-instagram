from dotenv import load_dotenv
from tools import crop_img
from fetch_hubble import fetch_hubble
from fetch_spacex import fetch_spacex
from insta_upload import insta_upload

if __name__ == "__main__":
    load_dotenv()
    fetch_spacex()
    fetch_hubble()
    crop_img()
    insta_upload()
