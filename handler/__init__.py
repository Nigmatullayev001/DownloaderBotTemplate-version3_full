from aiogram import Router
from .users import start, help, saved_url, check_sub, instagram_down, tiktok_downloader, qollanma, back, \
    youtube, pinterest_down, snapchat_down, facebook_down


def setup_message_routers() -> Router:
    router = Router()

    # Users routers
    router.include_router(start.router)
    router.include_router(help.router)
    router.include_router(saved_url.router)
    router.include_router(check_sub.router)
    router.include_router(instagram_down.router)
    router.include_router(tiktok_downloader.router)
    router.include_router(qollanma.router)
    router.include_router(back.router)
    router.include_router(youtube.router)
    router.include_router(pinterest_down.router)
    router.include_router(snapchat_down.router)
    router.include_router(facebook_down.router)

    return router
