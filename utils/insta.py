import requests
import json

from data.config import API_KEY


def downloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = json.loads(response.text)
    print(result)
    dict = {}
    if "error" in result:
        return "error"
    else:
        print(result)
        if result["Type"] == "Image" or 'Post-Image':
            dict['type'] = "image"
            dict["media"] = result["media"]
            return dict
        elif result["Type"] == "Video" or "Post-Video":
            dict["type"] = "video"
            dict["media"] = result["media"]
            return dict
        elif result["Type"] == "Carousel" or "Post-Carousel":
            dict["type"] = "carousel"
            dict["media"] = result["media"]
            return dict
        else:
            return "error"

# print(downloader(link="https://www.instagram.com/p/CqUfk0mtpBW/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="))
