from sqlalchemy import select
from bot.models.user_models import User
from bot.database.db import db


async def check_user(message):
    async with db.session() as session:
        user = await session.scalar(select(User).where(User.user_id == str(message.from_user.id)))
        return user


async def create_user(message):
    async with db.session() as session:
        first_name = message.from_user.first_name if message.from_user.first_name else None
        last_name = message.from_user.last_name if message.from_user.last_name else None
        new_user = User(
            user_id=str(message.from_user.id),
            user_first_name=first_name,
            user_last_name=last_name
        )
        session.add(new_user)
        await session.commit()
