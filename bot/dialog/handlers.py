import asyncio
from typing import cast

from aiogram import Bot
from aiogram.types import CallbackQuery, Message, InputFile
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram.types import BufferedInputFile



from bot.dialog.utils import add_logo_to_image
from bot.states import MainSG
from db.db import DBUser
from db.repositories.general import Repository
from db.uow import UoW

from phrase import generate_image
import settings
import logging


async def check_subscribe(callback: CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    bot: Bot = dialog_manager.middleware_data["bot"]
    try:
        result = await bot.get_chat_member(chat_id="@vk_dating", user_id=callback.from_user.id)
        if result.status in ["left", "kicked"]:
            await callback.answer("Вы не состоите в группе.", show_alert=True)
        else:
            await dialog_manager.next()
    except Exception:
        logging.error("Ошибка проверки группы")
        await dialog_manager.next()


async def handle_choose_gender(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["gender"] = button.widget_id


async def handle_choose_age(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["age"] = button.widget_id



async def handle_body_type(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["body_type"] = button.widget_id


async def handle_hair_style(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["hair_style"] = button.widget_id
    print(dialog_manager.dialog_data)
    if button.widget_id == "bald":
        dialog_manager.dialog_data["previous_state"] = "bald"
        if dialog_manager.dialog_data["gender"] == "man":
            await dialog_manager.switch_to(state=MainSG.man_look)
        else:
            await dialog_manager.switch_to(state=MainSG.girl_look)
    else:
        await dialog_manager.next()


async def handle_hair_color(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["hair_color"] = button.widget_id
    dialog_manager.dialog_data["previous_state"] = "with_hair"
    if dialog_manager.dialog_data["gender"] == "man":
        await dialog_manager.switch_to(state=MainSG.man_look)
    else:
        await dialog_manager.switch_to(state=MainSG.girl_look)


async def handle_girl_look(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["look"] = button.widget_id
    await dialog_manager.switch_to(state=MainSG.character)


async def back_to_hair_style(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if dialog_manager.dialog_data.get("previous_state") == "bald":
        await dialog_manager.switch_to(state=MainSG.hair_style)
    else:
        await dialog_manager.switch_to(state=MainSG.hair_color)


async def back_to_look(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if dialog_manager.dialog_data["gender"] == "man":
        await dialog_manager.switch_to(state=MainSG.man_look)
    else:
        await dialog_manager.switch_to(state=MainSG.girl_look)


async def handle_man_look(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["look"] = button.widget_id


async def handle_personality(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["personality"] = button.widget_id
    if dialog_manager.dialog_data["gender"] == "man":
        await dialog_manager.switch_to(state=MainSG.feature_man)
    else:
        await dialog_manager.switch_to(state=MainSG.feature_girl)


async def handle_feature(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["feature"] = button.widget_id
    await dialog_manager.switch_to(state=MainSG.are_you_ready)


async def back_to_feature(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if dialog_manager.dialog_data["gender"] == "man":
        await dialog_manager.switch_to(state=MainSG.feature_man)
    else:
        await dialog_manager.switch_to(state=MainSG.feature_girl)



async def handle_final(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await callback.message.edit_text("Генерация займет некоторое время...")
    prompt = ", ".join(
        settings.CHARACTER_MAPPING.get(value, value)
        for key, value in dialog_manager.dialog_data.items() if key != "previous_state")
    prompt = prompt[0].upper() + prompt[1:]
    if dialog_manager.dialog_data["gender"] == "man":
        final_prompt = settings.MAN_PROMPT + prompt
    else:
        final_prompt = settings.LADY_PROMPT + prompt
    await callback.message.answer(f"Промпт для нейросети: {final_prompt} (Для тестового режима)")
    image = await generate_image(prompt=final_prompt)
    image.seek(0)
    final_image = await add_logo_to_image(image)
    image_file = BufferedInputFile(final_image.read(), filename="generated_image.png")
    await dialog_manager.next(show_mode=ShowMode.SEND)
    await callback.message.answer_photo(image_file)


async def handle_result(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["result"] = button.widget_id


