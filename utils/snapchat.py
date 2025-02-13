import requests
from data.config import API_KEY

url = "https://snapchat-video-downloader-api.p.rapidapi.com/download"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "snapchat-video-downloader-api.p.rapidapi.com"
}


async def get_snapchat_video(url_video: str):
    querystring = {"link": url_video}

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
