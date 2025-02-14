from aiogram import F, types, Router
from utils.pinterest import get_pinterest_download_link
from utils.dp_api.db import Database
from aiogram.enums import ParseMode

router = Router()

# Initialize Database connection
db = Database()


# Define the handler for Pinterest URLs
@router.message(F.text.contains("pinterest.com"))
async def fetch_pinterest_url(message: types.Message):
    pin_url = message.text.strip()

    # Validate if the URL contains "pinterest.com/pin"
    if "pinterest.com/pin" not in pin_url:
        await message.reply("Please send a valid Pinterest link.")
        return

    # Get the download link for the image/video
    download_link = await get_pinterest_download_link(pin_url)

    # Default link URL
    link_url = 'https://www.pinterest.com'

    # try:
    # Check if the response contains "stories"
    if download_link:
        type_url = download_link['type']

        if type_url == "video":
            link_url = download_link["data"]["url"]
            await message.reply_video(video=link_url, caption="Here is your Pinterest video!",
                                      parse_mode=ParseMode.MARKDOWN)

        elif type_url == "image":
            # Extract image URL
            link_url = download_link["data"]["url"]
            await message.reply_photo(photo=link_url, caption="Here is your Pinterest image!",
                                      parse_mode=ParseMode.MARKDOWN)

    db.snapchat_add_url(user_id=message.from_user.id, title=f"{download_link}_{message.from_user.id}", url=link_url)

# except KeyError as e:
#     await message.reply(f"Error: Missing data field ({str(e)})")
# except Exception as e:
#     await message.reply(f"An error occurred: {str(e)}")
