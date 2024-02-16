from aiogram.fsm.state import State, StatesGroup


class AddState(StatesGroup):
    new_word = State()

