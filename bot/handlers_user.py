from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode
from aiogram import F, Router

from bot.states import MainSG

router = Router()


@router.message(Command("start"))
async def start_dialog(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.subscribe, mode=StartMode.RESET_STACK)


