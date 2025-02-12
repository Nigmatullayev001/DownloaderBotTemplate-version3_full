import aiohttp
import asyncio

url = "https://pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com/api/server"
headers = {
    "x-rapidapi-key": "b1173c1a80msh5a8b6302d359d65p1ff6e3jsnefbdad47bd40",
    "x-rapidapi-host": "pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com",
    "Content-Type": "application/json"
}


async def get_pinterest_download_link(pin_url: str):
    payload = {"id": pin_url}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 200:
                    response_data = await response.json()
                    print(response_data)


                    # Check if response contains the type (image or video)

                    if response_data:
                        print(response_data)
                        return response_data
                    else:
                        return "Unsupported content type."

                    # If 'download_url' exists, return it
                    # if 'download_url' in response_data:
                    #     return response_data['download_url']
                    # else:
                    #     return "Sorry, I couldn't fetch the download link. Please try again later."
                else:
                    return "Failed to fetch data from Pinterest. Please try again later."
    except Exception as e:
        return f"Error: {e}"
