import requests
import os
from dotenv import load_dotenv
from PIL import Image



def download_img(url, filename, img_folder):
  os.makedirs(img_folder, exist_ok=True)
  file_path = os.path.join(img_folder, filename)

  response = requests.get(url)
  response.raise_for_status()

  with open(file_path, 'wb') as file:
    file.write(response.content)

def fetch_spacex_last_launch():
  spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
  response = requests.get(spacex_url)
  img_links = response.json()['links']['flickr_images']

  for link in img_links:
    filename = link.split('/')[-1]
    download_img(link, filename)

def fetch_hubble():
  spacecraft_id=1
  hubble_url = 'http://hubblesite.org/api/v3/image/{}'.format(spacecraft_id)
  response = requests.get(hubble_url)
  img_raw_url = response.json()['image_files'][-1]['file_url'].replace('//','https://')

  img_url = requests.get(img_raw_url, verify=False).url

  img_name = response.json()['name']
  filename = img_url.split('/')[-1].replace('full_jpg', img_name)
  download_img(img_url, filename)

def fetch_hubble_collections():
  collection='printshop'
  collection_url = 'http://hubblesite.org/api/v3/images?page=all&collection_name={}'.format(collection)
  collection_response = requests.get(collection_url)
  ids = [response['id'] for response in collection_response.json()]

  for img_id in ids:
    hubble_url = 'http://hubblesite.org/api/v3/image/{}'.format(img_id)
    response = requests.get(hubble_url)
    img_raw_url = response.json()['image_files'][-1]['file_url'].replace('//','https://')

    img_url = requests.get(img_raw_url, verify=False).url

    img_name = response.json()['name']

    filename = img_url.split('/')[-1].replace('full_jpg', img_name)

    download_img(img_url, filename, img_folder)


if __name__ == "__main__":
    load_dotenv()
    img_folder = os.getenv("IMG_FOLDER")
    # fetch_hubble_collections()


    image = Image.open("images/ps12_16x20.jpg")
    coordinates = (10, 15, image.width, image.height)
    cropped = image.crop(coordinates)
    cropped.save("cropped2.jpg")
