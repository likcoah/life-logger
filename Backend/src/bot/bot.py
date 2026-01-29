from src.config import config
from src.bot.handlers import common

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


async def run():
    print('Starting bot...')

    bot = Bot(
            token=config.bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

    dp = Dispatcher()
    dp.include_routers(
            common.router
        )

    print('Bot started')
    await dp.start_polling(bot)
    print('Bot stopped')

