from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from bot.services.users import create_user, check_user
from .base_router import router


@router.message(CommandStart())
async def user_register(message: Message):
    # await message.reply(text=str(message))
    user = await check_user(message=message)
    if user:
        await message.answer(f'Ласкаво просимо {message.from_user.first_name}')
        return False
    await create_user(message=message)
    await message.answer(f'User {message.from_user.id} register!')

