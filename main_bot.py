from aiogram.utils import executor
from create_bot import dp
# from regis_user import me_regis

from client_regis import me_regis_client
from driver_regis import me_regis_driver
from aiogram import types
from aiogram import types, Bot, executor 
from create_bot import dp, bot
import logging
import datetime
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
import requests
import jsonpickle
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from aiogram import Dispatcher
from client_regis import FCMAdmin_Client
markupclient = types.ReplyKeyboardRemove()

my_url = "https://web.gram.tj/api/"

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Водитель", callback_data="driver"),
            types.InlineKeyboardButton(text="Пасcажир", callback_data="client")
        ],
        # [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def setup_bot_commands(_):
    bot_commands = [
        types.BotCommand(command="/back", description="Начать заново"),
        types.BotCommand(command="/start", description="Запустить бота"),
        # types.BotCommand(command="/chat", description="set bot for free chat")
    ]
    await bot.set_my_commands(bot_commands)


class FCMAdmin(StatesGroup):
    address_from = State()
  

class FCMAdmin_regis(StatesGroup):
    nomer = State()
    code = State()
    


async def on_startup(_):
    print("Онлайн")


@dp.message_handler(commands='back', state=None)
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def handler(message: types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")
   

@dp.message_handler(commands="start")
async def cm_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Подать заявку"]
    keyboard.add(*buttons)
    await message.answer( 'Чтобы найти пассажира или водителя выберите "Подать заявку"', reply_markup=keyboard)
   


@dp.message_handler(lambda message: message.text == "Подать заявку")
async def registration_z(message: types.Message, state=FSMContext):
    Datacode_one = {
    't_user_id': message.from_user.id,
    }

    response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check', data=Datacode_one)
    answer2 = jsonpickle.decode(response2.text)
    print(answer2)
    if answer2['code'] == 401 or answer2['code'] == 404:
        # await message.answer("Ваша авторизация не действительнf! \n/register")
        await message.answer("Введите номер телефона для авторизации \nПример: 992986660110", reply_markup=markupclient)
        await FCMAdmin_regis.next()
    if answer2['code'] == 200:
        keyboard_driver = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Водитель"]
        buttons_client = ["Пассажир"] 
        keyboard_driver.add(*buttons, *buttons_client)
        await message.answer("Вы пассажир или водитель?", reply_markup=get_keyboard())
        await state.finish()


@dp.message_handler(state=FCMAdmin_regis.nomer)
async def text_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nomer'] = message.text
        if len(data['nomer']) == 992:
            return data['nomer'][0] == '9' and data['nomer'][1] == '9' and data['nomer'][2] == '2'

        Data = {
            't_user_id': message.from_user.id,
            't_chat_id': message.chat.id,
            'phone' : data['nomer']
        }

        response0 = requests.post(f'{my_url}v1/telegram-bot/auth/registers/', data=Data)
        answer0 = jsonpickle.decode(response0.text)
        if answer0['code'] == 200:
            await message.answer("Введите код который отправлен по указанному номеру ?", reply_markup=markupclient)
            await FCMAdmin_regis.next()
            print(answer0)
        elif answer0['code'] == 403:
            await message.answer("Этот номер телефона уже используется!")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Отправить заявку"]
            keyboard.add(*buttons)
            await bot.send_message(message.from_user.id,
                                    'Вы можете подать заявку на поиск водителя или пассажира для совместной поездки',
                                    reply_markup=keyboard) 
            await state.reset_state(with_data=false)
        else:
            await message.answer("Номер должен содержать: 992 ", reply_markup=markupclient)  
       
     

  
   
@dp.message_handler(state=FCMAdmin_regis.code)
async def text_message_all(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['code'] = message.text

    Datacode = {
    't_user_id': message.from_user.id,
    't_chat_id': message.chat.id,
    'sms_code' : data['code']
    }

    response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check-code', data=Datacode)
    answer2 = jsonpickle.decode(response2.text)
    print(answer2)
    if answer2['code'] == 200:
        # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # buttons = ["Подать заявку"]
        # keyboard.add(*buttons)
        await message.answer("Вы успешно зарегистрировались", reply_markup=markupclient)
        await message.answer("Вы пассажир или водитель?", reply_markup=get_keyboard())
    await state.finish() 
    if answer2['code'] == 422:
        await message.answer("Неверный код", reply_markup=markupclient)
        return
        await state.finish()

    
 
    
   
 

@dp.callback_query_handler(lambda c: c.data in ["driver", "client"])
async def vote_up_cb_handler(callback_query: types.CallbackQuery):
    driver = callback_query.data
    if driver == "driver":
        await FCMAdmin.address_from.set()
        keyboard_c = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)            
        a1 = ["Душанбе", "Худжанд", "Ашт", "Тошкант", "Исфара", "Конибодом", "Мастчох", "Спитамен", "Истаравшан", "Панджакент", "Зафаробод", "Гончи", "Ойбек"]
        keyboard_c.add(*a1)
        await bot.send_message(callback_query.from_user.id, f'📍 Выберите место откуда выезжаете ?', reply_markup=keyboard_c)
    elif driver == "client":
        await FCMAdmin_Client.address_from_client.set()
        keyboard_c = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)            
        a1 = ["Душанбе", "Худжанд", "Ашт", "Исфара", "Тошкант", "Конибодом", "Мастчох", "Спитамен", "Истаравшан", "Панджакент", "Зафаробод", "Гончи", "Ойбек"]
        keyboard_c.add(*a1)
        await bot.send_message(callback_query.from_user.id, f'📍 Выберите место откуда выезжаете ?', reply_markup=keyboard_c)
        
    

# # me_regis_client(dp)
# me_regis(dp)




    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=[on_startup, setup_bot_commands],)


