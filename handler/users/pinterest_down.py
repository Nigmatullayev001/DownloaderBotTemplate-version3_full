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

    try:
        # Check if the response contains "stories"
        if "data" in download_link and "stories" in download_link["data"]:
            type_url = download_link["data"]["stories"][0].get("type", "")

            if type_url == "story_pin_video_block":
                # Extract video URL
                link_url = download_link["data"]["stories"][0]["video"]["video_list"][0]["url"]
                await message.reply_video(video=link_url, caption="Here is your Pinterest video!", parse_mode=ParseMode.MARKDOWN)

            elif type_url == "story_pin_image_block":
                # Extract image URL
                link_url = download_link["data"]["images"]["orig"]["url"]
                await message.reply_photo(photo=link_url, caption="Here is your Pinterest image!", parse_mode=ParseMode.MARKDOWN)

        # If stories are not present, check for direct video data
        elif "videos" in download_link["data"]:
            link_url = download_link["data"]["videos"].get("V_720P", "")
            if link_url:
                await message.reply_video(video=link_url, caption="Here is your Pinterest video!", parse_mode=ParseMode.MARKDOWN)
            else:
                await message.reply("No high-quality video found.", parse_mode=ParseMode.MARKDOWN)

        # Log the Pinterest link in the database
        db.pinterest_add_url(f"{download_link}_{message.from_user.id}", link_url)

    except KeyError as e:
        await message.reply(f"Error: Missing data field ({str(e)})")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
