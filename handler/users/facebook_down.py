from aiogram import F, types, Router
from utils.facebook import get_facebook_download_link
from utils.dp_api.db import Database
from aiogram.enums import ParseMode

router = Router()

# Initialize Database connection
db = Database()


# Define the handler for Pinterest URLs
@router.message(F.text.contains("facebook.com"))
async def fetch_pinterest_url(message: types.Message):
    # Get the download link for the image/video
    download_link = await get_facebook_download_link(message.text)

    # try:
    link_url = "https://faceboook.com"
    # Check if the response contains "stories"
    if download_link:
        type_url = download_link[0]['urls'][0]['name']
        time = download_link[0]["meta"]["duration"]


        if type_url == "MP4":
            link_url = download_link[0]['urls'][0]['url']
            await message.reply_video(video=link_url,
                                      caption=f'{download_link[0]["meta"]["title"]} - {time}',
                                      parse_mode=ParseMode.MARKDOWN)

        elif type_url == "PNG":
            # Extract image URL
            link_url = download_link[0]["urls"][0]['url']
            await message.reply_photo(photo=link_url,
                                      caption=f"{download_link[0]['meta']['title']}",
                                      parse_mode=ParseMode.MARKDOWN)

    db.facebook_add_url(user_id=message.from_user.id, title="{message.from_user.id}", url=link_url)

# except KeyError as e:
#     await message.reply(f"Error: Missing data field ({str(e)})")
# except Exception as e:
#     await message.reply(f"An error occurred: {str(e)}")
