from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from bot.config.config import settings
from bot.routers import users_router, post_routers
from bot.services.posts import parse_channel_post
import asyncio

dp = Dispatcher()


async def main():
    bot = Bot(token=settings.TOKEN_BOT, parse_mode=ParseMode.HTML)
    # data = await client.get_dialogs()
    # print(data)
    dp.include_router(users_router.router)
    dp.include_router(post_routers.router)
    await dp.start_polling(bot)

# with client:
#     client.loop.run_until_complete(main())

if __name__ == '__main__':
    asyncio.run(main())

