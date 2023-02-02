import logging

import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
import requests
import jsonpickle
import logging




import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
import requests
import jsonpickle
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from aiogram.utils.callback_data import CallbackData
from aiogram import Dispatcher
import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
markupd = types.ReplyKeyboardRemove()

my_url = "https://web.gram.tj/api/"

start_kb = ReplyKeyboardMarkup(resize_keyboard=True,)
start_kb.row('Navigation Calendar', 'Dialog Calendar')


def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Опубликовать", callback_data="drivergram"),
            # types.InlineKeyboardButton(text="Пасcажир", callback_data="client")
        ],
        # [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


class FCMAdmin(StatesGroup):
    rol = State()
    address_from = State()
    address_to = State()
    mest = State()
    date_y = State()
    marka = State()
    sum_d = State()
    phone = State()



# @dp.message_handler(commands="start")
# async def cm(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Отправить заявку"]
#     keyboard.add(*buttons)
#     await bot.send_message(message.from_user.id,
#                            'Привет 👋, здесь Вы можете подать заявку на поиск водителя или пассажира для совместной поездки',
#                            reply_markup=keyboard)
    
  

# @dp.message_handler(lambda message: message.text == "Отправить заявку", state=None)
# async def registration_driver(message: types.Message):
#     await FCMAdmin.rol.set()
#     keyboard_driver = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Водитель"]
#     buttons_client = ['Поссажир'] 
#     keyboard_driver.add(*buttons).add(*buttons_client)
#     await message.answer("Вы пассажир или водитель?", reply_markup=keyboard_driver)

    

# @dp.message_handler(state=FCMAdmin.rol)
# async def text_message(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['rol'] = message.text
#     await FCMAdmin.next()
#     keyboard_c = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)            
#     a1 = ["Душанбе", "Худжанд", "Ашт", "Исфара", "Конибодом", "Мастчох", "Спитамен", "Истаравшан", "Панджакент", "Зафаробод", "Гончи", "Ойбек"]
#     keyboard_c.add(*a1)
#     await message.answer("📍 Выберите место откуда выезжаете ?", reply_markup=keyboard_c)

@dp.message_handler(commands='back', state='*')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def handler(message: types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Подать заявку"]
    keyboard.add(*buttons)
    await bot.send_message(message.from_user.id,
                           'Чтобы найти пассажира или водителя выберите "Подать заявку"',
                           reply_markup=keyboard)

    
@dp.message_handler(state=FCMAdmin.address_from)
async def message_driver(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address_from"] = message.text
    await FCMAdmin.next()  
    keyboard_e = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a3 = ["Душанбе", "Худжанд", "Ашт", "Тошкант", "Исфара", "Конибодом", "Мастчох", "Спитамен", "Истаравшан", "Панджакент",
             "Зафаробод", "Гончи", "Ойбек"]
    keyboard_e.add(*a3)
    await message.answer("📍 Выберите место куда поедете ?", reply_markup=keyboard_e)
    

@dp.message_handler(state=FCMAdmin.address_to)
async def message_driver_one(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address_to"] = message.text
    await FCMAdmin.next()  
    keyboard_m = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    a6 = ["1", "2", "3", "4", "5", "6"]
    keyboard_m.add(*a6)
    await message.answer("💺Сколько свободных мест на авто ?", reply_markup=keyboard_m)


@dp.message_handler(lambda message: message.text not in ["1", "2", "3", "4", "5", "6"], state=FCMAdmin.mest)
async def process_seats_invalid(message: types.Message):
    return await message.reply("Пожалуйста укажите число от 1 до 6")

@dp.message_handler(state=FCMAdmin.mest)
async def message_driver_one(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["mesto"] = message.text
    await FCMAdmin.next()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    tmrtext0 = (datetime.date.today() + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
    tmrtext1 = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    tmrtext2 = (datetime.date.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    tmrtext3 = (datetime.date.today() + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
    tmrtext4 = (datetime.date.today() + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
    tmrtext5 = (datetime.date.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    markup.insert(tmrtext0)
    markup.insert(tmrtext1)
    markup.insert(tmrtext2)
    markup.insert(tmrtext3)
    markup.insert(tmrtext4)
    markup.insert(tmrtext5)  
    await bot.send_message(message.chat.id,"📆 Введите дату поездки ?", reply_markup=markup)

# @dp.callback_query_handler(dialog_cal_callback.filter(), state=FCMAdmin.date_y)
# async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict, state=FSMContext):
#     selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
#     await callback_query.message.answer(f'Вы выбрали {date.strftime("%Y-%m-%d")}')
#     async with state.proxy() as data:
#         data["date_y"] = date.strftime("%Y-%m-%d")
#         Datacode_driverj = {
#             't_user_id': callback_query.from_user.id,
#             'start_date' : data['date_y'],  
#         }
#         response_driver = requests.post(f'{my_url}v1/telegram-bot/trip', data=Datacode_driverj)
#         answer_driver = jsonpickle.decode(response_driver.text)
#         print(answer_driver)
#         if answer_driver['code'] == 422:
#             await callback_query.message.answer("В поле дата начала должна быть датой больше сегодня", reply_markup=await DialogCalendar().start_calendar())
#         elif answer_driver['code'] == 200:
#             await FCMAdmin.next() 
#             await callback_query.message.answer("🚙 Введите марку и модель авто ?", reply_markup=markupd)
            

     

@dp.message_handler(state=FCMAdmin.date_y)
async def message_driver_one(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["date_y"] = message.text
    await FCMAdmin.next() 
    await message.answer("🚙 Введите марку и модель авто ?", reply_markup=markupd)

@dp.message_handler(state=FCMAdmin.marka)
async def message_driver_one(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["marka"] = message.text
    await FCMAdmin.next() 
    await message.answer(" 💵 Стоимость поездки за 1 пассажира?", reply_markup=markupd)

@dp.message_handler(state=FCMAdmin.sum_d)
async def message_driver_one(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data["sum_d"] = message.text
        await FCMAdmin.next()
        Datacode_one = {
        't_user_id': message.from_user.id,
        }
        global answer2
        response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check', data=Datacode_one)
        answer2 = jsonpickle.decode(response2.text)
        
        markup = types.ReplyKeyboardRemove()
        # id_all = -770555118
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('🕵🏼 Я #Водитель'),
                md.text('🏢 Откуда: #'+data['address_from']),
                md.text('🏠 Куда: #'+data['address_to']),
                md.text('📅 Дата выезда: ', data['date_y']),
                md.text('🙋🏻‍♂️ Кол-во: ', data['mesto']),
                md.text('💵 Стоимость: ', data['sum_d']) + 'cмн',
                md.text('🚙  Марка и модель: ', data['marka']),
                md.text('📱 Номер телефона: ', answer2['result']['phone']),
                md.text("@hamroh_gram_bot"),
                sep='\n',
                ),
                reply_markup=get_keyboard(),
            # reply_markup=markup,
            # parse_mode=ParseMode.MARKDOWN
        )

        await FCMAdmin.next()
    else:
        await message.reply("Пожалуйста укажите число")


@dp.callback_query_handler(lambda c: c.data in ["drivergram"])
async def vote_up_cb_handler(callback_query: types.CallbackQuery, state=FSMContext):
    driver = callback_query.data
    async with state.proxy() as data:
        # id_all = -770555118
        # id_all = -1001500877507
        # id_all = -1001717140961
        id_all = -1001645175499
        if driver == "drivergram":
            Datacode_driver = {
                't_user_id': callback_query.from_user.id,
                'type' : 'performer',
                'from_city' : data['address_from'],
                'to_city' : data['address_to'],
                'start_date' : data['date_y'],
                'seat_count' : data['mesto'],
                'price' : data['sum_d'],
                'auto_mark' : data['marka'],
                'auto_number' :  answer2['result']['phone']
            }
            response_driver = requests.post(f'{my_url}v1/telegram-bot/trip', data=Datacode_driver)
            answer_driver = jsonpickle.decode(response_driver.text)
            if answer_driver['code'] == 200:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                buttons = ["Подать заявку"]
                keyboard.add(*buttons)
                await bot.send_message(callback_query.from_user.id, "✅ Ваша заявка отправлена в канал @hamroh_gram, спасибо! ", reply_markup=keyboard)
                await state.finish()
                await bot.send_message(
                id_all,
                md.text(
                    md.text('🕵🏼 Я #Водитель'),
                    md.text('🏢 Откуда: #'+data['address_from']),
                    md.text('🏠 Куда: #'+data['address_to']),
                    md.text('📅 Дата выезда: ', data['date_y']),
                    md.text('🙋🏻‍♂️ Кол-во: ', data['mesto']),
                    md.text('💵 Стоимость: ', data['sum_d']) + 'cмн',
                    md.text('🚙  Марка и модель: ', data['marka']),
                    md.text('📱 Номер телефона: ',  answer2['result']['phone']),
                    md.text("@hamroh_gram_bot"),
                    sep='\n',
                    ),
                # reply_markup=markup,
                # parse_mode=ParseMode.MARKDOWN
            )
            else:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                buttons = ["Подать заявку"]
                keyboard.add(*buttons)
                await bot.send_message(callback_query.from_user.id, "Ваша заявка не опубликована обратитесь к @Gram_tj", reply_markup=keyboard)
                await bot.send_message(callback_query.from_user.id, answer_driver)
            await state.finish()

        #     await bot.send_message(
        #         id_all,
        #         md.text(
        #             md.text('🕵🏼 Я #Водитель'),
        #             md.text('🏢 Откуда: #'+data['address_from']),
        #             md.text('🏠 Куда: #'+data['address_to']),
        #             md.text('📅 Дата выезда: ', data['date_y']),
        #             md.text('🙋🏻‍♂️ Коль-во: ', data['mesto']),
        #             md.text('💵 Стоимость: ', data['sum_d']) + 'cмн',
        #             md.text('🚙  Марка и модель: ', data['marka']),
        #             md.text('📱 Номер телефона: ', data['phone']),
        #             md.text("@hamrohbot_bot"),
        #             sep='\n',
        #         ),
        # # reply_markup=markup,
        # # parse_mode=ParseMode.MARKDOWN
        #     )
        #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     buttons = ["Отправить заявку"]
        #     keyboard.add(*buttons)
        #     await bot.send_message(callback_query.from_user.id, "✅ Ваша заявка отправлена в канал @hamroh_gram, спасибо! ", reply_markup=keyboard)
        #     await state.finish()
    

  





def me_regis_driver(dp: Dispatcher):
    dp.register_message_handler(message_driver, state=address_from)



