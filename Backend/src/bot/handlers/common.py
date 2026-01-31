from src.database.db import db

from aiogram import Router, types
from aiogram.filters import CommandStart


router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    if not message.from_user:
        return
    if db.is_registered(message.from_user.id):
        await message.answer(f'Welcome back, {message.from_user.first_name}')
    else:
        db.register_user(message.from_user.id)
        await message.answer(f'Hi, {message.from_user.first_name}! Registration was successfull')

