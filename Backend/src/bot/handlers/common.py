from aiogram import Router, types
from aiogram.filters import CommandStart


router = Router()


@router.message(CommandStart())
async def cmdStart(message: types.Message):
    if not message.from_user:
        return
    await message.answer(f'Hello, <b>{message.from_user.first_name}</b>')

