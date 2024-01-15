import stat

from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from bot.services.posts import add_post, parse_channel_post, add_channel, get_all_posts, get_chat_id


router = Router()


@router.message(Command('posts'))
async def get_posts(message: Message):
    return await get_all_posts(message=message)


class ChannelForm(StatesGroup):
    channel = State()


class PushPost(StatesGroup):
    post_id = State()


@router.message(Command('channel'))
async def add_new_channel(message: Message, state: FSMContext) -> None:
    await message.reply('Enter channel name:')
    await state.set_state(ChannelForm.channel)
    # await message.reply('Enter channel name')


@router.message(ChannelForm.channel)
async def process_channel(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.reply('Їбанько')
    return await add_channel(message)


@router.message(Command('parse'))
async def parse_channels(message: Message):
    await message.answer('Test')
    return await parse_channel_post(message=message)


@router.message(Command('chat'))
async def chat_id(message: Message):
    return await get_chat_id(message=message)


@router.message(Command('push'))
async def publish_post(message: Message, state: FSMContext):
    await message.reply('Enter post id:')
    await state.set_state(PushPost.post_id)


@router.message(PushPost.post_id)
async def process_push_post(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    return await add_post(message=message)


# @router.channel_post
# async def new_post(message: Message) -> Any:
#     return await add_post()
