import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from aiogram.fsm.storage.memory import MemoryStorage


from bot.config import Config, load_config
from bot.dialog.dialog import start_dialog
from bot.handlers_user import router
from bot.middlewares.middleware import CheckUserMiddleware, DBSessionMiddleware
from db.create_pool import create_pool
from aiogram.client.bot import DefaultBotProperties


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode="HTML"))
    dp: Dispatcher = Dispatcher(
        name="main_dispatcher",
        storage=MemoryStorage(),
        config=config,
    )

    session_pool = await create_pool()
    dp.update.outer_middleware(DBSessionMiddleware(session_pool))
    dp.update.outer_middleware(CheckUserMiddleware())
    setup_dialogs(dp)

    dp.include_router(router)
    dp.include_router(start_dialog)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
