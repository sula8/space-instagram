import requests
from tools import download_img


def fetch_spacex():
  spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
  response = requests.get(spacex_url)
  img_links = response.json()['links']['flickr_images']

  for link in img_links:
    filename = link.split('/')[-1]
    download_img(link, filename)