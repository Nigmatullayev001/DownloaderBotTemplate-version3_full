import requests
from data.config import API_KEY

url = "https://pinterest-video-and-image-downloader.p.rapidapi.com/pinterest"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "pinterest-video-and-image-downloader.p.rapidapi.com"
}


async def get_pinterest_download_link(pin_url: str):
    querystring = {"url": pin_url}

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
