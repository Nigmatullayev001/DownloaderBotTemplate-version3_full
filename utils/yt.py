from urllib.parse import urlparse, parse_qs
from data.config import API_KEY

import requests


def extract_video_id(url):
    parsed_url = urlparse(url)
    print(parsed_url)
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        query = parse_qs(parsed_url.query)
        if "v" in query:
            return query["v"][0]
        if parsed_url.path.startswith("/shorts/"):
            return parsed_url.path.split("/")[2]
    elif parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]
    return None


def fetch_video_details(video_id):
    endpoint = f"https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": 'youtube-media-downloader.p.rapidapi.com',
    }
    params = {"videoId": video_id}
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    return None
