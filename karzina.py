# l = "v1/telegram-bot/auth/registers/"

# h = "/?t_user_id=1&t_chat_id=2&phone=992927782615"

# global max_id
# r = requests.get(f'{my_URL}t-bot/market-orders?max_id={max_id}', headers=Header)
# r = jsonpickle.decode(r.text)

# Data = {
#     't_user_id': '1',
#     't_chat_id': '77777777',
#     'phone' : '992557772512'
#     }
# response = requests.post(f'{my_URL}auth/login', data=Data)
# answer = jsonpickle.decode(response.text)

# start_kb = ReplyKeyboardMarkup(resize_keyboard=True,)
# start_kb.row('Navigation Calendar', 'Dialog Calendar')

# @dp.message_handler(content_types=["text"], state=FCMAdmin.rol)
# async def text_message(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['rol'] = message.text
#     await FCMAdmin.next()


# async with state.proxy() as data:
#     id_all = -770555118
#     await bot.send_message(id_all, str(data))
# await state.finish()
# await message.answer("Потвердить если ваше данные провелно ?")
# await message.answer("Потвердить если ваше данные провелно ?")
# Remove keyboard


# @dp.message_handler(lambda message: message.text == "Поссажир")
# async def message_client(message: types.Message):
#     ingo1 = message.text
#     keyboard_d = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     a2 = ["Душанбе", "Худжанд", "Ашт", "Исфара", "Конибодом", "Мастчох", "Спитамен", "Истаравшан", "Панджакент",             "Зафаробод", "Гончи", "Ойбек"]
#     keyboard_d.add(*a2)
#     await message.answer("📍 Введите начальную точку маршрута", reply_markup=keyboard_d)