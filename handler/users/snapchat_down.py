from aiogram import F, types, Router
from utils.snapchat import get_snapchat_video
from utils.dp_api.db import Database
from aiogram.enums import ParseMode

router = Router()

# Initialize Database connection
db = Database()


# Define the handler for Pinterest URLs
@router.message(F.text.contains("snapchat.com"))
async def fetch_pinterest_url(message: types.Message):
    # Get the download link for the image/video
    download_link = await get_snapchat_video(message.text)

    # try:
    link_url = "https://snapchat.com"
    # Check if the response contains "stories"
    if download_link:
        type_url = download_link['data']['medias'][0]['type']
        bytes_size = download_link["data"]["duration"]
        megabytes = int(bytes_size) / 1_000

        if type_url == "video":
            link_url = download_link["data"]['medias'][0]['url']
            await message.reply_video(video=link_url,
                                      caption=f'{download_link["data"]["title"]} - {megabytes} MB',
                                      parse_mode=ParseMode.MARKDOWN)

        elif type_url == "image":
            # Extract image URL
            link_url = download_link["data"]["medias"][0]['url']
            await message.reply_photo(photo=link_url,
                                      caption=f"{download_link['data']['title']} - {megabytes} MB",
                                      parse_mode=ParseMode.MARKDOWN)

    db.snapchat_add_url(message.from_user.id, f"{message.from_user.id}", link_url)

# except KeyError as e:
#     await message.reply(f"Error: Missing data field ({str(e)})")
# except Exception as e:
#     await message.reply(f"An error occurred: {str(e)}")
