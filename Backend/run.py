from src.bot import bot

import asyncio


async def main():
    await asyncio.gather(
            bot.run()
        )


if __name__ == '__main__':
    asyncio.run(main())

