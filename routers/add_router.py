from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from fsm.add_state import AddState
from Translator import translate

from keyboards import word_keyboard

router = Router()


@router.message(F.text == 'Добавить слово')
async def add_main_handler(msg: types.Message, state: FSMContext):
    await state.set_state(AddState.new_word)
    await msg.answer("Напишите слово, которое нужно перевести:", reply_markup=word_keyboard())


@router.message(AddState.new_word)
async def new_word_handler(msg: types.Message):
    result = translate(msg.text)

    if result['responseStatus'] != 200:
        await msg.answer("Что-то пошло не так :(")

    await msg.answer(result['responseData']['translatedText'])
