from __future__ import annotations

import logging
import settings
from typing import TYPE_CHECKING

from aiogram_dialog import Dialog, ShowMode, Window
from aiogram.types import ContentType
from aiogram_dialog.widgets.kbd import Button, Column, SwitchTo, Url, Next, Back, SwitchInlineQuery
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.input import TextInput
from bot.dialog import handlers
from bot.states import MainSG



start_dialog = Dialog(
    Window(
        Const(settings.SUBSCRIBE_TEMPLATE),
        Next(text=Const("Уже готово"), on_click=handlers.check_subscribe),
        Url(text=Const("Иду подписываться"), url=Const('https://t.me/vk_dating')),
        state=MainSG.subscribe
    ),
    Window(
        Const(settings.MATCH_PREFERENCES_TEMPLATE),
        Column(
            Next(Const("Парень"), id="man", on_click=handlers.handle_choose_gender),
            Next(Const("Девушка"), id="lady", on_click=handlers.handle_choose_gender),
        ),
        Back(Const("Назад")),
        state=MainSG.choose_gender
    ),
    Window(
        Const(settings.BODY_TYPE_TEMPLATE),
        Column(
            Next(Const("Стройное"), id="slim", on_click=handlers.handle_body_type),
            Next(Const("С приятной полнотой"), id="plump", on_click=handlers.handle_body_type),
            Next(Const("Спортивное"), id="sporty", on_click=handlers.handle_body_type),
        ),
        Back(Const("Назад")),
        state=MainSG.shape
    ),
    Window(
        Const(settings.HAIR_TYPE_TEMPLATE),
        Column(
            Button(Const("Короткие волосы"), id="short_hair", on_click=handlers.handle_hair_style),
            Button(Const("Длинные волосы"), id="long_hair", on_click=handlers.handle_hair_style),
            Button(Const("Кудрявые волосы"), id="curly_hair", on_click=handlers.handle_hair_style),
            Button(Const("Без волос"), id="bald", on_click=handlers.handle_hair_style),
        ),
        Back(Const("Назад")),
        state=MainSG.hair_style
    ),
    Window(
        Const(settings.HAIR_COLOR_TEMPLATE),
        Column(
            Button(Const("Светлые"), id="blonde", on_click=handlers.handle_hair_color),
            Button(Const("Темные"), id="dark", on_click=handlers.handle_hair_color),
            Button(Const("Рыжие"), id="red", on_click=handlers.handle_hair_color),
            Button(Const("Яркие"), id="bright", on_click=handlers.handle_hair_color),
        ),
        Back(Const("Назад")),
        state=MainSG.hair_color
    ),
    Window(
        Const(settings.DATE_STYLE_TEMPLATE),
        Column(
            Button(Const("Элегантный"), id="elegant", on_click=handlers.handle_girl_look),
            Button(Const("Милый"), id="cute", on_click=handlers.handle_girl_look),
            Button(Const("Строгий"), id="strict", on_click=handlers.handle_girl_look),
            Button(Const("Романтичный"), id="romantic", on_click=handlers.handle_girl_look),
        ),
        Button(text=Const("Назад"), id="back", on_click=handlers.back_to_hair_style),
        state=MainSG.girl_look
    ),
    Window(
        Const(settings.DATE_STYLE_TEMPLATE),
        Column(
            Next(Const("Официальный"), id="official", on_click=handlers.handle_man_look),
            Next(Const("Брутальный"), id="brutal", on_click=handlers.handle_man_look),
            Next(Const("Романтичный"), id="romantic_man", on_click=handlers.handle_man_look),
            Next(Const("Расслабленный"), id="relaxed", on_click=handlers.handle_man_look),
        ),
        Button(text=Const("Назад"), id="back", on_click=handlers.back_to_hair_style),
        state=MainSG.man_look
    ),
    Window(
        Const(settings.PERSONALITY_TEMPLATE),
        Column(
            Button(Const("Добрый"), id="kind", on_click=handlers.handle_personality),
            Button(Const("Весёлый"), id="funny", on_click=handlers.handle_personality),
            Button(Const("Застенчивый"), id="shy", on_click=handlers.handle_personality),
            Button(Const("Меланхоличный"), id="melancholic", on_click=handlers.handle_personality),
        ),
        Button(Const("Назад"), id="back", on_click=handlers.back_to_look),
        state=MainSG.character
    ),
    Window(
        Const(settings.SPECIAL_FEATURE_TEMPLATE),
        Column(
            Button(Const("Пирсинг"), id="piercing", on_click=handlers.handle_feature),
            Button(Const("Веснушки"), id="freckles", on_click=handlers.handle_feature),
            Button(Const("Яркий макияж"), id="makeup", on_click=handlers.handle_feature),
        ),
        Back(Const("Назад")),
        state=MainSG.feature_girl
    ),
    Window(
        Const(settings.SPECIAL_FEATURE_TEMPLATE),
        Column(
            Button(Const("Борода"), id="piercing", on_click=handlers.handle_feature),
            Button(Const("Усы"), id="freckles", on_click=handlers.handle_feature),
            Button(Const("Пирсинг"), id="makeup", on_click=handlers.handle_feature),
        ),
        SwitchTo(Const("Назад"), id="back", state=MainSG.character),
        state=MainSG.feature_man
    ),
    Window(
        Const(settings.FINAL_TEMPLATE),
        Button(Const("Давайте скорее!"), id="ready", on_click=handlers.handle_final),
        Button(Const("Назад"), id="back", on_click=handlers.back_to_feature),
        state=MainSG.are_you_ready
    ),
    Window(
        Const(settings.MATCH_GENERATED_TEMPLATE),
        Url(text=Const("Начать знакомиться"), url=Const('https://dating.vk.com/')),
        SwitchInlineQuery(
            Const("Поделиться с друзьями"),
            switch_inline_query=Const("Узнай, как выглядит пара твоей мечты с помощью искусственного интеллекта от VK Знакомств в боте Мэтч GPT: t.me/vk_dating_bot")
        ),
        SwitchTo(Const("Попробовать еще раз"), id='more', state=MainSG.choose_gender),
        state=MainSG.result
    ),
)
