from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишите ему:\nhttps://t.me/ItalianPastaBot')


# @dp.message_handler(commands=['Режим_работы'])
async def pasta_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 10:00 до 22:00')


# @dp.message_handler(commands=['Расположение'])
async def pasta_pace_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Шеболдаева, 4/4')


# @dp.message_handler(commands=['Меню'])
async def pasta_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pasta_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pasta_pace_command, commands=['Расположение'])
    dp.register_message_handler(pasta_menu_command, commands=['Меню'])