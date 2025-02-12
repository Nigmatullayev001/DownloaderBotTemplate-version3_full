import logging
import requests

from data.config import API_KEY  # API_KEY ni config fayldan yuklang

# RapidAPI konfiguratsiyasi
RAPIDAPI_HOST = "tiktok-video-downloader-api.p.rapidapi.com"
ENDPOINT = "https://tiktok-video-downloader-api.p.rapidapi.com/media"


def download_tiktok_video(video_url: str) -> str:
    """
    TikTok video yuklab olish funksiyasi.

    Args:
        video_url (str): TikTok video URL manzili.

    Returns:
        str: Suv belgisiz yuklab olish havolasi yoki None.
    """
    try:
        # API so'rovini amalga oshirish
        headers = {
            "x-rapidapi-key": API_KEY,  # Config fayldan API kaliti yuklanadi
            "x-rapidapi-host": RAPIDAPI_HOST,
        }
        querystring = {"videoUrl": video_url}

        response = requests.get(ENDPOINT, headers=headers, params=querystring)
        response_data = response.json()

        # Javob muvaffaqiyatli ekanligini tekshirish
        if response.status_code == 200:
            # Suv belgisiz video URL'ini qaytarish
            print(response_data)
            print(response_data.get("downloadUrl"))
            return response_data.get("downloadUrl")
        else:
            logging.error(f"API xatosi: {response_data.get('message', 'No error message')}")
            return None
    except Exception as e:
        logging.error(f"Xatolik yuz berdi: {e}")
        return None
