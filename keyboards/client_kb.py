from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Режим_Работы')
b2 = KeyboardButton('Расположение')
b3 = KeyboardButton('Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(b2).add(b3)

