from src.database.db import db
from src.bot.keyboards import deletion_confirmation

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery


router = Router()


@router.message(Command('delete_account'))
async def cmd_delete_account(message: types.Message):
    if not message.from_user:
        return
    if db.is_registered(message.from_user.id):
        await message.answer('This will permanently delete all your data. Are you sure?', reply_markup=deletion_confirmation.get_inline_keyboard())
    else:
        await message.answer('You dont have an account, deletion is impossible')


@router.callback_query(F.data == 'deletion_confirmed')
async def delete_account_confirmed(callback: CallbackQuery):
    db.delete_user(callback.from_user.id)
    await callback.answer()
    await callback.message.edit_text(text='Data deletion was successfully', reply_markup=None)


@router.callback_query(F.data == 'deletion_canceled')
async def delete_account_canceled(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='Data deletion was canceled', reply_markup=None)

