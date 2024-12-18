from aiogram.fsm.state import State, StatesGroup


class MainSG(StatesGroup):
    start = State()
    subscribe = State()
    choose_gender = State()
    choose_age = State()
    shape = State()
    hair_style = State()
    hair_color = State()
    girl_look = State()
    man_look = State()
    character = State()
    feature_girl = State()
    feature_man = State()
    are_you_ready = State()
    result = State()
    invite = State()
