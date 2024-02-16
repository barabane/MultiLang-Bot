from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def main_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="Добавить слово")
    builder.button(text="Список слов")
    builder.button(text="Проверка знаний")

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def word_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text="Добавить в список", callback_data="add_new_word")
    return builder.as_markup()
