from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def get_inline_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='Yes, delete it', callback_data='deletion_confirmed')
    builder.button(text='No, cancel deletion', callback_data='deletion_canceled')

    builder.adjust(2)

    return builder.as_markup()

