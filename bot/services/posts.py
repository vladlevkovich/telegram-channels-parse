from sqlalchemy import select
from aiogram import Bot
from telethon import TelegramClient
from bot.models.post_models import Post, Channel
from bot.models.user_models import User
from bot.config.config import settings
from bot.database.db import db

bot = Bot(token=settings.TOKEN_BOT)


async def add_channel(message):
    async with db.session() as session:
        user_id = message.from_user.id
        user = await session.scalar(select(User).where(User.user_id == str(user_id)))
        new_channel = Channel(
            user_id=user.id,
            channel=message.text
        )
        session.add(new_channel)
        await session.commit()


async def parse_channel_post(message):
    # posts = bot.get_updates()
    # client = TelegramClient('test_tg', int(api_id), api_hash)
    # while True:
    async with TelegramClient('test_tg', settings.API_ID, settings.API_HASH) as client:
        if not client.is_connected():
            await client.connect()
        async with db.session() as session:
            user = await session.scalar(select(User).where(User.user_id == str(message.from_user.id)))
            smtp = select(Channel).order_by(Channel.id)
            result = await session.execute(smtp)
            channels = result.scalars().all()
            print(channels)

            async for dialog in client.iter_dialogs():
                for channel in channels:
                    # print(type(dialog.name))
                    if dialog.name == channel.channel:
                        print(f'{dialog.name} - {channel.channel}')
                        print(True)
                        messages = client.iter_messages(dialog.id, limit=20)
                        async for channel_message in messages:
                            try:
                                if channel_message.photo:
                                    photo = await client.download_media(channel_message.photo)
                                    with open(photo, 'rb') as f:
                                        photo_file = f.read()
                                new_post = Post(
                                    body=str(channel_message.message),
                                    author=str(dialog.name),
                                    user_id=user.id,
                                    photo=photo_file if photo else None
                                )
                                session.add(new_post)
                                await session.commit()
                            except ValueError as e:
                                raise ValueError(str(e))
                pass
            return user


async def get_chat_id(message):
    async with TelegramClient('test_tg', settings.API_ID, settings.API_HASH) as client:
        async for dialog in client.iter_dialogs():
            if dialog.name == 'Test Channel;':
                print(dialog.id)


async def get_all_posts(message):
    async with db.session() as session:
        user = await session.scalar(select(User).where(User.user_id == str(message.from_user.id)))
        smtp = select(Post).order_by(Post.id)
        result = await session.execute(smtp)
        posts = result.scalars().all()

        for post in posts:
            if post.user_id == user.id:
                await message.answer(f'Post id={post.id}\n {post.body[:10]}\n {post.author}')


async def add_post(message):
    async with db.session() as session:
        post = await session.scalar(select(Post).where(Post.id == int(message.text)))
        if not post:
            raise {'message': 'Post not found'}

        # if post.photo:
        #     photo = await bot.download(post.photo)
        #     with open(photo, 'wb') as f:
        #         pass
        #     await bot.send_photo(chat_id=settings.CHAT_ID, photo=open(photo, 'rb'))
        await bot.send_message(chat_id=settings.CHAT_ID, text=post.body)

