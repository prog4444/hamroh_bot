import logging

import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
import requests
import jsonpickle
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
import requests
import jsonpickle
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import types, Bot, executor 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from aiogram import Dispatcher
import datetime
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

markupclient = types.ReplyKeyboardRemove()



    

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Опубликовать", callback_data="podver"),
            # types.InlineKeyboardButton(text="Пасcажир", callback_data="client")
        ],
        # [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


my_url = "https://web.gram.tj/api/"

class FCMAdmin_Client(StatesGroup):
    # rol_client = State()
    address_from_client = State()
    address_to_client = State()
    mest_client = State()
    date_y_client = State()
    sum_d_client = State()
    phone_client = State()


# @dp.message_handler(commands="register", state=None)
# async def cm_regis_client(message: types.Message):
#     await FCMAdmin_Client.rol_client.set()


    
# @dp.message_handler(state=FCMAdmin_Client.rol_client)
# async def message_client(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['rol_client'] = message.text
#     await FCMAdmin_Client.next()
#     keyboard_d = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     a2 = ["Душанбе", "Худжанд", "Ашт", "Исфара", "Конибодом", "Мастчох", "Спитамен", "Истаравшан", "Панджакент",  "Зафаробод", "Гончи", "Ойбек"]
#     keyboard_d.add(*a2)
#     await message.answer("📍 Выберите место откуда выезжаете ?", reply_markup=keyboard_d)


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
    
@dp.message_handler(state=FCMAdmin_Client.address_from_client)
async def message_driver(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address_from_client"] = message.text
    await FCMAdmin_Client.next()  
    keyboard_e = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a3 = ["Душанбе", "Худжанд", "Ашт",  "Тошкант", "Исфара", "Конибодом", "Мастчох", "Спитамен", "Истаравшан", "Панджакент",
             "Зафаробод", "Гончи", "Ойбек"]
    keyboard_e.add(*a3)
    await message.answer("📍 Выберите место куда поедете ?", reply_markup=keyboard_e)
    

@dp.message_handler(state=FCMAdmin_Client.address_to_client)
async def message_driver_one(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address_to_client"] = message.text
    await FCMAdmin_Client.next()  
    keyboard_m = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    a6 = ["1", "2", "3", "4", "5", "6"]
    keyboard_m.add(*a6)
    await message.answer("💺 Сколько мест Вам нужно ?", reply_markup=keyboard_m)


@dp.message_handler(lambda message: message.text not in ["1", "2", "3", "4", "5", "6"], state=FCMAdmin_Client.mest_client)
async def process_seats_invalid(message: types.Message):
    return await message.reply("Пожалуйста укажите число от 1 до 6")


@dp.message_handler(state=FCMAdmin_Client.mest_client)
async def message_driver_one(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["mesto_client"] = message.text
    await FCMAdmin_Client.next()
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


# @dp.callback_query_handler(simple_cal_callback.filter(), state=FCMAdmin_Client.date_y_client)
# async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict, state=FSMContext):
#     selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
#     await callback_query.message.answer(f'Вы выбрали {date.strftime("%Y-%m-%d")}')
#     async with state.proxy() as data:
#         data["date_y_client"] = date.strftime("%Y-%m-%d")
#         Datacode_driverj = {
#             't_user_id': callback_query.from_user.id,
#             'start_date' : data['date_y_client'],  
#         }
#         response_driver = requests.post(f'{my_url}v1/telegram-bot/trip', data=Datacode_driverj)
#         answer_driver = jsonpickle.decode(response_driver.text)
#         print(answer_driver)
#         if answer_driver['code'] == 422:
#             await callback_query.message.answer("В поле дата начала должна быть датой больше сегодня", reply_markup=await SimpleCalendar().start_calendar())
#         elif answer_driver['code'] == 200:
#             await FCMAdmin_Client.next()
#             await callback_query.message.answer(" 💵 Введите цену ? ", reply_markup=markupclient)
    # reply_markup=types.ReplyKeyboardRemove()


@dp.message_handler(state=FCMAdmin_Client.date_y_client)
async def message_driver_one(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["date_y_client"] = message.text
    await FCMAdmin_Client.next() 
    await message.answer(" 💵 Введите цену?", reply_markup=markupclient)



@dp.message_handler(state=FCMAdmin_Client.sum_d_client)
async def message_driver_one(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data["sum_d_client"] = message.text
        await FCMAdmin_Client.next()
        Datacode_one = {
        't_user_id': message.from_user.id,
        }
        global answer2
        response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check', data=Datacode_one)
        answer2 = jsonpickle.decode(response2.text)
        id_all = -770555118
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('🕵🏼 Я #Пассажир'),
                md.text('🏢 Откуда: #'+data['address_from_client']),
                md.text('🏠 Куда: #'+data['address_to_client']),
                md.text('📅 Дата выезда: ', data['date_y_client']),
                md.text('🙋🏻‍♂️ Кол-во: ', data['mesto_client']),
                md.text('💵 Стоимость: ', data['sum_d_client']) + 'cмн',
                md.text('📱 Номер телефона: ', answer2['result']['phone']),
                md.text("@hamroh_gram_bot"),
                sep='\n',
                ),
                reply_markup=get_keyboard(),
            # reply_markup=markup,
            # parse_mode=ParseMode.MARKDOWN
        )
        await FCMAdmin_Client.next()
    else:
        await message.reply("Пожалуйста укажите число")


@dp.callback_query_handler(lambda c: c.data in ["podver"])
async def vote_up_cb_handler(callback_query: types.CallbackQuery, state=FSMContext):
    driver = callback_query.data
    async with state.proxy() as data:
        id_all = -770555118
        if driver == "podver":
            Datacode_driver = {
                't_user_id': callback_query.from_user.id,
                'type' : 'passenger',
                'from_city' : data['address_from_client'],
                'to_city' : data['address_to_client'],
                'start_date' : data['date_y_client'],
                'seat_count' : data['mesto_client'],
                'price' : data['sum_d_client'],
                'auto_number' : answer2['result']['phone']
            }
            response_driver = requests.post(f'{my_url}v1/telegram-bot/trip', data=Datacode_driver)
            answer_driver = jsonpickle.decode(response_driver.text)
            if answer_driver['code'] == 200:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                buttons = ["Подать заявку"]
                keyboard.add(*buttons)
                await bot.send_message(callback_query.from_user.id, "✅ Ваша заявка отправлена в канал @hamroh_gram, спасибо! ", reply_markup=keyboard)
                await bot.send_message(
                id_all,
                md.text(
                    md.text('🕵🏼 Я #Пассажир'),
                    md.text('🏢 Откуда: #'+data['address_from_client']),
                    md.text('🏠 Куда: #'+data['address_to_client']),
                    md.text('📅 Дата выезда: ', data['date_y_client']),
                    md.text('🙋🏻‍♂️ Кол-во: ', data['mesto_client']),
                    md.text('💵 Стоимость: ', data['sum_d_client']) + 'cмн',
                    md.text('📱 Номер телефона: ', answer2['result']['phone']),
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
        #             md.text('🕵🏼 Я #Пассажир'),
        #             md.text('🏢 Откуда: #'+data['address_from_client']),
        #             md.text('🏠 Куда: #'+data['address_to_client']),
        #             md.text('📅 Дата выезда: ', data['date_y_client']),
        #             md.text('🙋🏻‍♂️ Коль-во: ', data['mesto_client']),
        #             md.text('💵 Стоимость: ', data['sum_d_client']) + 'cмн',
        #             md.text('📱 Номер телефона: ', data['phone_client']),
        #             md.text("@hamrohbot_bot"),
        #             sep='\n',
        #         ),
        # # reply_markup=markup,
        # # parse_mode=ParseMode.MARKDOWN
        #     )
        #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     buttons = ["Подать заявку"]
        #     keyboard.add(*buttons)
        #     await bot.send_message(callback_query.from_user.id, "✅ Ваша заявка отправлена в канал @hamroh_gram, спасибо! ", reply_markup=keyboard)
        #     await state.finish()
       
    
 

    # id_all = -770555118
    # Datacode_driver = {
    # 't_user_id': message.from_user.id,
    # 't_chat_id': message.chat.id,
    # 'type' : 'passenger',
    # 'from_city' : data['address_from_client'],
    # 'to_city' : data['address_to_client'],
    # 'start_date' : data['date_y_client'],
    # 'seat_count' : data['mesto_client'],
    # 'price' : data['sum_d_client'],
    # 'auto_number' : data['phone_client']
    # }

    # response_driver = requests.post(f'{my_url}v1/telegram-bot/trip', data=Datacode_driver)
    # answer_driver = jsonpickle.decode(response_driver.text)
    # if answer_driver['code'] == 200:
    #     await message.answer("✅ Ваша заявка отправлена в канал @hamroh_gram, спасибо!")
    #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     buttons = ["Отправить заявку"]
    #     keyboard.add(*buttons)
    #     await bot.send_message(message.from_user.id,
    #                         'Чтобы найти пассажира или водителя выберите подать заявку',
    #                         reply_markup=keyboard)
    #     await bot.send_message(
    #     id_all,
    #     md.text(
    #         md.text('🕵🏼 Я #Пассажир'),
    #         md.text('🏢 Откуда: #'+data['address_from_client']),
    #         md.text('🏠 Куда: #'+data['address_to_client']),
    #         md.text('📅 Дата выезда: ', data['date_y_client']),
    #         md.text('🙋🏻‍♂️ Коль-во: ', data['mesto_client']),
    #         md.text('💵 Стоимость: ', data['sum_d_client']) + 'cмн',
    #         md.text('📱 Номер телефона: ', data['phone_client']),
    #         md.text("@hamrohbot_bot"),
    #         sep='\n',
    #         ),
    #     # reply_markup=markup,
    #     # parse_mode=ParseMode.MARKDOWN
    # )
    # elif answer_driver['code'] == 422:
    #     # await message.answer("✅ Ваша заявка отправлена в канал @hamroh_gram, спасибо!\n🔍 Для поиска попутчика перейдите в @hamroh_gram.\nИспользуйте навигационные тэги #пассажир или #водитель.")
    #     await message.answer("Ваша заявка не опубликована обратитесь к @Gram_tj")
    #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     buttons = ["Отправить заявку"]
    #     keyboard.add(*buttons)
    #     await bot.send_message(message.from_user.id,
    #                         'Чтобы найти пассажира или водителя выберите подать заявку',
    #                         reply_markup=keyboard)
    # print(answer_driver)
    # await state.finish()

def me_regis_client(dp: Dispatcher):
    dp.register_message_handler(message_driver, state="*")
    