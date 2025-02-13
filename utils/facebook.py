import requests
from data.config import API_KEY

url = "https://facebook17.p.rapidapi.com/api/facebook/links"


headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "facebook17.p.rapidapi.com",
    "Content-Type": "application/json"
}


async def get_facebook_download_link(url_link: str):
    payload = {"url": url_link}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
