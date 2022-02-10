from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_message = '👈 Orqaga'
confirm_message = '✅ Buyurtmani tasdiqlang'
all_right_message = '✅ Hammasi tog\'ri'
cancel_message = '🚫 Bekor qilish'


def confirm_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(confirm_message)
    markup.add(back_message)

    return markup

def back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(back_message)

    return markup

def check_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(back_message, all_right_message)

    return markup

def submit_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(cancel_message, all_right_message)

    return markup

geo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Lokatsiya yuborish", request_location=True)],
    ],
    resize_keyboard=True,
)

phone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqamni yuborish", request_phone=True)],
    ],
    resize_keyboard=True,
)