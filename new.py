# keyboard_driver = types.ReplyKeyboardMarkup(resize_keyboard=True)
# buttons = ["Водитель"]
# buttons_client = ["Пассажир"] 
# keyboard_driver.add(*buttons, *buttons_client)
# await message.answer("Вы пассажир или водитель?", reply_markup=get_keyboard())

#    Datacode_one = {
#     't_user_id': message.from_user.id,
#     }

#     response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check', data=Datacode_one)
#     answer2 = jsonpickle.decode(response2.text)
#     print(answer2)
#     if answer2['code'] == 401 or answer2['code'] == 404:
#         # await message.answer("Ваша авторизация не действительнf! \n/register")
#         await message.answer("Введите номер телефона для авторизации \nПример: 992986660110")
#         await FCMAdmin_regis.next()
#     if answer2['code'] == 200:
#         keyboard_driver = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         buttons = ["Водитель"]
#         buttons_client = ["Пассажир"] 
#         keyboard_driver.add(*buttons, *buttons_client)
#         await message.answer("Вы пассажир или водитель?", reply_markup=get_keyboard())
#         await state.finish()








# import logging

# from aiogram import Bot, Dispatcher
# from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
# from aiogram.utils import executor
# from aiogram.dispatcher.filters import Text
# from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
# from create_bot import dp, bot

# from config import TOKEN

# # API_TOKEN = '' uncomment and insert your telegram bot API key here

# # Configure logging
# logging.basicConfig(level=logging.INFO)



# start_kb = ReplyKeyboardMarkup(resize_keyboard=True,)
# start_kb.row('Navigation Calendar', 'Dialog Calendar')


# # starting bot when user sends `/start` command, answering with inline calendar
# @dp.message_handler(commands=['start'])
# async def cmd_start(message: Message):
#     await message.reply('Pick a calendar', reply_markup=start_kb)


# @dp.message_handler(Text(equals=['Navigation Calendar'], ignore_case=True))
# async def nav_cal_handler(message: Message):
#     await message.answer("Please select a date: ", reply_markup=await SimpleCalendar().start_calendar())


# # simple calendar usage
# @dp.callback_query_handler(simple_cal_callback.filter())
# async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
#     selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
#     if selected:
#         await callback_query.message.answer(
#             f'You selected {date.strftime("%d/%m/%Y")}',
#             reply_markup=start_kb
#         )


# @dp.message_handler(Text(equals=['Dialog Calendar'], ignore_case=True))
# async def simple_cal_handler(message: Message):
#     await message.answer("Please select a date: ", reply_markup=await DialogCalendar().start_calendar())


# # dialog calendar usage
# @dp.callback_query_handler(dialog_cal_callback.filter())
# async def process_dialog_calendar(callback_query: CallbackQuery, callback_data: dict):
#     selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
#     if selected:
#         await callback_query.message.answer(
#             f'You selected {date.strftime("%d/%m/%Y")}',
#             reply_markup=start_kb
#         )


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


    # await bot.send_message(
    #     id_all,
    #     md.text(
    #         md.text('🕵🏼 Я #Водитель'),
    #         md.text('🏢 Откуда: #'+data['address_from']),
    #         md.text('🏠 Куда: #'+data['address_to']),
    #         md.text('📅 Дата выезда: ', data['date_y']),
    #         md.text('🙋🏻‍♂️ Коль-во: ', data['mesto']),
    #         md.text('💵 Стоимость: ', data['sum_d']) + 'cмн',
    #         md.text('🚙  Марка и модель: ', data['marka']),
    #         md.text('📱 Номер телефона: ', data['phone']),
    #         md.text("@hamrohbot_bot"),
    #         sep='\n',
    #         ),
    #     # reply_markup=markup,
    #     # parse_mode=ParseMode.MARKDOWN
    # )
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # buttons = ["Отправить заявку"]
    # keyboard.add(*buttons) 
    # await message.answer("✅ Ваша заявка отправлена в канал @hamroh_gram, спасибо!", reply_markup=keyboard)
    # await state.finish() ✅ Вы авторизованный человек


# from config import TOKEN 
# from aiogram import Bot, Dispatcher, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.types import Message
# from create_bot import dp, bot


# from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
# from aiogram_dialog.widgets.kbd import Button
# from aiogram_dialog.widgets.text import Const




# class MySG(StatesGroup):
#     main = State()


# main_window = Window(
#     Const("Hello, unknown person"),
#     Button(Const("Useless button"), id="nothing"),
#     state=MySG.main,
# )
# dialog = Dialog(main_window)



# @dp.message_handler(commands=["start"])
# async def start(m: Message, dialog_manager: DialogManager):
#     await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)



#  report_data = {}
    
    
#     @dp.message_handler(Command('report'))
#     async def calculate_report(message: types.Message, state: FSMContext):
#         check = message.from_user.id  # проверяем доступ пользователя
#         if check in config.usr_admins:
#             await bot.send_message(chat_id=INFO,
#                                    text=f'🔑 Репорт [{message.from_user.full_name, message.from_user.id}]')
    
    
#             cursor.execute("SELECT * FROM otchet")
#             conn.commit()
    
#             await message.answer(f"\n\n📊 ФОРМИРОВАНИЕ ОТЧЕТА 📊️")
#             try:
#                 await message.answer(f'\n\n💰 В кассе остовалось : {cursor.fetchall()[-1][-3]} ₽')
#             except IndexError:
#                 await message.answer("🪶 ТАБЛИЦА НЕ ПОДКЛЮЧЕНА 🪶")
#                 await bot.send_message(chat_id=INFO, text='🛑 ТАБЛИЦА НЕ ПОДКЛЮЧЕНА!!!')
#                 pass
    
#             await message.answer( f'{tx.instr_1}' )
#             await fsm.Reports.R1.set()
    
#         else:
#             await message.answer('👨🏽‍💻 В разрабоке!')
    
    
#     @dp.message_handler(state=fsm.Reports.R1)
#     async def input_report(message: types.Message, state: FSMContext):
    
#         try:
#             money_in_the_morning = int(message.text)
    
#         except ValueError:
#             await message.answer(f'{tx.err_or_1}')
#             await message.answer(f'{tx.instr_1}')
#             return input_report
    
#         await state.update_data( money_in_the_morning=money_in_the_morning )
#         await message.answer( f'{tx.instr_2}' )
#         await fsm.Reports.R2.set()
    
    
#     @dp.message_handler( state=fsm.Reports.R2 )
#     async def input_report(message: types.Message, state: FSMContext):
    
#         try:
#             proceeds = int(message.text)
    
#         except ValueError:
#             await message.answer(f'{tx.err_or_1}')
#             await message.answer(f'{tx.instr_2}')
#             return input_report
    
#         await state.update_data(proceeds=proceeds)
#         await message.answer(f'{tx.instr_3}')
#         await fsm.Reports.R3.set()
    
    
#     @dp.message_handler( state=fsm.Reports.R3 )
#     async def input_report(message: types.Message, state: FSMContext):
    
#         try:
#             cashless = int(message.text)
    
#         except ValueError:
#             await message.answer(f'{tx.err_or_1}')
#             await message.answer( f'{tx.instr_3}' )
#             return input_report
    
#         await state.update_data(cashless=cashless)
#         await message.answer(f'{tx.instr_4}')
#         await fsm.Reports.R4.set()
    
    
#     @dp.message_handler( state=fsm.Reports.R4 )
#     async def input_report(message: types.Message, state: FSMContext):
    
#         try:
#             collection = int(message.text)
    
#         except ValueError:
#             await message.answer(f'{tx.err_or_1}')
#             await message.answer(f'{tx.instr_4}')
#             return input_report
    
#         await state.update_data(collection=collection)
#         await message.answer(f'{tx.instr_5}')
#         await fsm.Reports.R5.set()
    
    
#     @dp.message_handler( state=fsm.Reports.R5 )
#     async def input_report(message: types.Message, state: FSMContext):
    
#         try:
#             costs = int(message.text)
    
#         except ValueError:
#             await message.answer(f'{tx.err_or_1}')
#             await message.answer(f'{tx.instr_5}')
#             return input_report
    
#         await state.update_data(costs=costs)
#         await message.answer(f'{tx.instr_6}')
#         await fsm.Reports.R6.set()
    
    
#     @dp.message_handler( state=fsm.Reports.R6 )
#     async def input_report(message: types.Message, state: FSMContext):
#         try:
#             fact = int(message.text)
    
#         except ValueError:
#             await message.answer(f'{tx.err_or_1}')
#             await message.answer(f'{tx.instr_6}')
#             return input_report
    
#         await state.update_data(fact=fact)
#         report_data = await state.get_data()
    
    
#         async def start_report(report_data):
#             money_in_the_morning = int(report_data['money_in_the_morning'])
#             proceeds = int(report_data['proceeds'])
#             cashless = int(report_data['cashless'])
#             collection = int(report_data['collection'])
#             costs = int(report_data['costs'])
#             fact = int(report_data['fact'])
#             cash_1 = proceeds - cashless                                # высчитываем наличку
#             cash_2 = proceeds - cashless - collection - costs           # Остаток после инкс и доп расход
#             kassa = money_in_the_morning + cash_2                       # формируем кассу
    
    
    
    
    
#     ####################################################################################################
    
#             form = f""" 
#     🗓 {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}\n
#     🔺        ОТЧЕТ        🔻\n
#     ↦ Выручка: {proceeds} ₽
#     ↦ Безнал: {cashless} ₽
#     ↦ Наличными: {cash_1} ₽
#     ↦ Инкассации:{collection} ₽
#     ↦ Доп. расходы:{costs} ₽
#     ↦ Факт: {fact}₽
    
#             """
#     ####################################################################################################
    
    
    
#             # Проверка по кассе
#             if fact == kassa:
    
#                 await message.answer(f'{form}\nВ кассе: {str( kassa )}₽\nКасса ровная! シ ')
    
#                 await bot.send_message(chat_id=INFO,
#                                        text=f'{form}\nВ кассе: {str( kassa )}₽\n'
#                                        f'Касса ровная! シ ')
    
    
#             elif fact > kassa:
    
#                 await message.answer(
#                     f'{form}\nВ кассе {str( fact )}₽ '
#                     f'\nДолжно быть {str( kassa )}₽\n'
#                     f'Сумма больше на {str( fact - kassa )}₽')
    
#                 await bot.send_message(chat_id=INFO,
#                                        text=f'{form}\nВ кассе {str( fact )}₽ '
#                                        f'\nДолжно быть {str( kassa )}₽\nСумма '
#                                        f'больше на {str( fact - kassa )}₽')
    
    
    
#             else:
#                 await message.answer(
#                     f'{form}\nВ кассе {str( fact )}₽ '
#                     f'\nДолжно быть {str( kassa )}₽.\n'
#                     f'Не хватает {str( kassa - fact )}₽')
    
    
    
#                 await bot.send_message(chat_id=INFO,
#                                        text = f'{form}\nВ кассе {str( fact )}₽ '
#                                        f'\nДолжно быть {str( kassa )}₽.\n'
#                                        f'Не хватает {str( kassa - fact )}₽')
    
    
#             priz = 9000
#             difference = priz - proceeds
    
    
    
#             if proceeds >= priz:
#                 await message.answer('🏆 ПРЕМИЯ 🥇:\n\nУраа... '
#                                      'Вам положена премия 500₽ за '
#                                      'хорошую работу! 🎊🎉🎈\n')
#                 await message.answer('🤑')
    
    
#             elif proceeds >= priz - 1000:
#                 await message.answer(f'🥈 ПРЕМИЯ 🥈:\n\n🚖Вам положенно Такси в обе стороны! 🚖\n'
#                                      f'До 🏆 не хватило {str( difference )} ₽  🤬 😭\n')
    
# ==================================================================================================================

# from aiogram import Bot, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import Dispatcher, FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.utils import executor
# from pyautogui import *
# from pyqiwip2p import QiwiP2P
# from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime
# import Qiwi_Token
# import random


# p2p = QiwiP2P(auth_key=Qiwi_Token.P2P_Qiwi_Token) #Токен Киви кошелька

# file = "GTA5 game.jpg"
# bot = Bot(token="#####", parse_mode=types.ParseMode.HTML)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)



# class BuyState(StatesGroup):  #Машинное состояние
#     Buy_CM = State()

# @dp.message_handler(commands=["start"])
# async def start_message(message: types.Message):
#     await message.answer("Привет, вы попали в магазин\n<b>Telegram Games</b>\n"
#         "Где вы можете купить игру GTA5 Online\nнажав команду <b>/buy</b> ")

# @dp.message_handler(commands=["help"])
# async def help_message(message: types.Message):
#     await message.answer("Наберите команду <b>/buy</b>\nЧтобу купить товар")

# @dp.message_handler(commands=['buy'])
# async def cmd_buy(message: types.Message):
#     await BuyState.Buy_CM.set() #Запуск состояния оплаты

#     new_bill = p2p.bill(bill_id=random.choice(range(100,99999999)), amount=150, lifetime=0.1)
#     print(new_bill.bill_id, new_bill.pay_url)


#     button1 = types.InlineKeyboardButton(text="К оплате   150,00 RUB", url=new_bill.pay_url)
#     button2 = types.InlineKeyboardButton(text="Отменить", callback_data="Отменить")
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(button1,button2)

    
#     file = "GTA5 game.jpg"
#     photo = types.InputFile(file)
#     await bot.send_photo(message.chat.id,photo=photo,caption=""
#         "<b>Epic Games аккаунт с игрой GTA 5</b>\n"
#         "ПРЕДОСТАВЛЯЕСТЯ смена данных аккаунта + Доступ к почте\n"
#         "Банов в онлайне нет\n"
#         "<u>100% Гарантией Безопасности</u> (Пожизненно)интересуйтесь на все вопросы отвечу.",
#         reply_markup=markup)

#     while True: #Создание цикла
#         #Проверка статуса оплаты
#         if p2p.check(new_bill.bill_id).status == 'PAID': #Проверка, на то - дошла ли оплата до бота. Вслучае положительного ответа, он выполняет данный if.
#             await message.answer("544")
#             break #Завершение цикла
#         elif p2p.check(new_bill.bill_id).status == "EXPIRED": #Делаем проверку, на время оплаты. То есть в случае неоплаты в течении 7-ми минут, цикл прекращается.
#             await message.answer('Мужик, ты че не оплатил?')
#             break #Завершение цикла
#         if p2p.check(new_bill.bill_id).status == 'REJECTED': #Проверка, на то - дошла ли оплата до бота. Вслучае положительного ответа, он выполняет данный if.
#             break #Завершение цикла
#         sleep(5)
#     sleep(0.1) #Спим некое время, чтобы бот не крашнулся.

# @dp.callback_query_handler(text="Отменить", state=BuyState.Buy_CM)
# async def photo_update(call: types.CallbackQuery, state: FSMContext): #При нажатии инлайн кнопки отмены срабатывает код
        
#     photo_update = types.InputMedia(media=types.InputFile(file), caption=""
#     "<b>Epic Games аккаунт с игрой GTA 5</b>\n"
#     "ПРЕДОСТАВЛЯЕСТЯ смена данных аккаунта + Доступ к почте\n"
#     "Банов в онлайне нет\n"
#     "<u>100% Гарантией Безопасности</u> (Пожизненно)интересуйтесь на все вопросы отвечу.")
            
#     await call.message.edit_media(photo_update)
#     await bot.send_message(call.from_user.id,'Вы отменили заказ')
#     p2p.reject(bill_id=new_bill.bill_id)
#     await state.finish()


# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)


# @router.message(Command(commands=["delete"]), state=None)
# async def cmd_delete(message: Message, state: FSMContext):
#     kb = []
#     kb.append([
#         InlineKeyboardButton(
#             text="Выбрать ссылку",
#             switch_inline_query_current_chat="links"
#         )
#     ])
#     kb.append([
#         InlineKeyboardButton(
#             text="Выбрать изображение",
#             switch_inline_query_current_chat="images"
#         )
#     ])
#     await state.set_state(DeleteCommon.waiting_for_delete_start)
#     await message.answer(
#         text="Выберите, что хотите удалить:",
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=kb)
#     )

# @router.inline_query(F.query == "long")
# async def pagination_demo(
#         inline_query: InlineQuery,
# ):
#     # Высчитываем offset как число
#     offset = int(inline_query.offset) if inline_query.offset else 1
#     results = [InlineQueryResultArticle(
#         id=str(item_num),
#         title=f"Объект №{item_num}",
#         input_message_content=InputTextMessageContent(
#             message_text=f"Объект №{item_num}"
#         )
#     ) for item_num in get_fake_results(offset)]
#     if len(results) < 50:
#         await inline_query.answer(
#             results, is_personal=True
#         )
#     else:
#         await inline_query.answer(
#             results, is_personal=True, 
#             next_offset=str(offset+50)
#         )