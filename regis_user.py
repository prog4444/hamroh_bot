# import logging
# import aiogram.utils.markdown as md
# from aiogram.types import ParseMode
# from aiogram import types, Bot, executor 
# from create_bot import dp, bot
# from aiogram.dispatcher import FSMContext
# import requests
# import jsonpickle
# import aiogram.utils.markdown as md
# from aiogram.types import ParseMode
# from aiogram import types, Bot, executor 
# from create_bot import dp, bot
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
# from aiogram.utils.callback_data import CallbackData
# from aiogram import Dispatcher



# my_url = "https://web.gram.tj/api/"

# class FCMAdmin_regis(StatesGroup):
#     nomer = State()
#     code = State()

# @dp.message_handler(commands="register", state=None)
# async def cm_regis(message: types.Message, state=FSMContext):
#     await FCMAdmin_regis.nomer.set()
#     Datacode_one = {
#     't_user_id': message.from_user.id,
#     }
#     response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check', data=Datacode_one)
#     answer2 = jsonpickle.decode(response2.text)
#     print(answer2)
#     if answer2['code'] == 200:
#         await message.answer("✅ Вы авторизованы")
#         # await state.finish()
#         keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         buttons = ["Подать заявку"]
#         keyboard.add(*buttons)
#         await bot.send_message(message.from_user.id,'Вы можете подать заявку на поиск водителя или пассажира для совместной поездки', reply_markup=keyboard) 
#     await state.finish()
#     if answer2['code'] == 401 or answer2['code'] == 404:
#         await message.answer("Введите номер телефона для авторизации \nПример: 992986660110")
#         await FCMAdmin_regis.next()
        
       
    


# @dp.message_handler(state=FCMAdmin_regis.nomer)
# async def text_message(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['nomer'] = message.text
#         if len(data['nomer']) == 992:
#             return data['nomer'][0] == '9' and data['nomer'][1] == '9' and data['nomer'][2] == '2'

#         Data = {
#             't_user_id': message.from_user.id,
#             't_chat_id': message.chat.id,
#             'phone' : data['nomer']
#         }

#         response0 = requests.post(f'{my_url}v1/telegram-bot/auth/registers/', data=Data)
#         answer0 = jsonpickle.decode(response0.text)
#         if answer0['code'] == 200:
#             await message.answer("Введите код который отправлен по указанному номеру ?")
#             await FCMAdmin_regis.next()
#             print(answer0)
#         elif answer0['code'] == 403:
#             await message.answer("Этот номер телефона уже используется!")
#             keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             buttons = ["Отправить заявку"]
#             keyboard.add(*buttons)
#             await bot.send_message(message.from_user.id,
#                                     'Вы можете подать заявку на поиск водителя или пассажира для совместной поездки',
#                                     reply_markup=keyboard) 
#             await state.finish()
#         else:
#             await message.answer("Номер должен содержать: 992 ")  
       
     

  
   
# @dp.message_handler(state=FCMAdmin_regis.code)
# async def text_message_all(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['code'] = message.text

#     Datacode = {
#     't_user_id': message.from_user.id,
#     't_chat_id': message.chat.id,
#     'sms_code' : data['code']
#     }

#     response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check-code', data=Datacode)
#     answer2 = jsonpickle.decode(response2.text)
#     print(answer2)
#     if answer2['code'] == 200:
#         await message.answer("Вы успешно зарегистрировались")
#     elif answer2['code'] == 422:
#         await message.answer("Неверный код")
#         return
#         await state.finish()

    
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Подать заявку"]
#     keyboard.add(*buttons)
#     await bot.send_message(message.from_user.id,
#                            'Чтобы найти пассажира или водителя выберите подать заявку',
#                            reply_markup=keyboard)
#     await state.finish() 
    
   
# def me_regis(dp: Dispatcher):
#     dp.register_message_handler(cm_regis, commands='register', state=None)
  
# @dp.message_handler(content_types=["text"], state=FCMAdmin.code)
# async def text_message(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['code'] = message.text
        
#     Datacode = {
#     't_user_id': message.from_user.id,
#     't_chat_id': message.chat.id,
#     'sms_code' : data['code']
#     }

#     response2 = requests.post(f'{my_url}v1/telegram-bot/auth/check-code', data=Datacode)
#     answer2 = jsonpickle.decode(response2.text)
#     print(answer2)
#     await message.answer(answer2['message'])
#     await state.finish()
#     await message.answer("Ок")\

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


