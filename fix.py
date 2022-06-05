# @bot.callback_query_handler(func=lambda call: True)
# def reggame(message):
#     option = ['Камень', 'Ножницы', 'Бумага']
#     global game
#     global value
#     value = random.choice(option)
#     game = message.text
#     if game == 'Камень':
#         if value == 'Камень':
#             bot.send_message(message.chat.id, 'Ничья')
#         if value == 'Ножницы':
#             bot.send_message(message.chat.id, 'Вы победили, я поставил ножницы')
#         if value == 'Бумага':
#             bot.send_message(message.chat.id, 'Вы проиграли , я поставил бумагу')
#     if game == 'Ножницы':
#         if value == 'Камень':
#             bot.send_message(message.chat.id, 'Вы проиграли , я поставил камень')
#         if value == 'Ножницы':
#             bot.send_message(message.chat.id, 'Ничья')
#         if value == 'Бумага':
#             bot.send_message(message.chat.id, 'Вы выиграли , я поставил бумагу')
#     if game == 'Бумага':
#         if value == 'Камень':
#             bot.send_message(message.chat.id, 'Вы выиграли , я поставил камень')
#         if value == 'Ножницы':
#             bot.send_message(message.chat.id, 'Вы проиграли , я поставил ножницы')
#         if value == 'Бумага':
#             bot.send_message(message.chat.id, 'Ничья')
#
#
# elif ms_text == "Камень":
# bot.register_next_step_handler(message, reggame)
#
# elif ms_text == "Ножницы":
# bot.register_next_step_handler(message, reggame)
#
# elif ms_text == "Бумага":
# bot.register_next_step_handler(message, reggame)


# elif ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# btn1 = types.KeyboardButton("Развлечения")
# btn3 = types.KeyboardButton("Управление")
# back = types.KeyboardButton("Помощь")
# markup.add(btn1, btn3, back)
# bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)
#
# elif ms_text == "Развлечения" or ms_text == "Вернуться в Развлечения":
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# btn1 = types.KeyboardButton("Фото топовых японцев")
# btn2 = types.KeyboardButton("Прислать анекдот")
# btn3 = types.KeyboardButton("Игры")
# back = types.KeyboardButton("Вернуться в главное меню")
# markup.add(btn1, btn2, btn3, back)
# bot.send_message(chat_id, text="Развлечения", reply_markup=markup)
#
# elif ms_text == "Игры" or ms_text == "Вернуться в игры":
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# btn1 = types.KeyboardButton("Камень, ножницы, бумага")
# bnt2 = types.KeyboardButton("Лабиринт")
# btn3 = types.KeyboardButton("Вернуться в Развлечения")
# markup.add(btn1, bnt2, btn3)
# bot.send_message(chat_id, text="Игры", reply_markup=markup)
#
# elif ms_text == "Камень, ножницы, бумага":
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# btn1 = types.KeyboardButton("Камень")
# btn2 = types.KeyboardButton("Ножницы")
# btn3 = types.KeyboardButton("Бумага")
# back = types.KeyboardButton("Вернуться в игры")
# markup.add(btn1, btn2, btn3, back)
# bot.send_message(chat_id, text="Камень, ножницы, бумага", reply_markup=markup)
#
# elif ms_text == "Фото топовых японцев":
# IGM1 = open("PHOTO/Japan1.jpg", 'rb')
# IGM2 = open("PHOTO/Japan2.jpg", 'rb')
# IGM3 = open("PHOTO/Japan3.jpg", 'rb')
# IGM4 = open("PHOTO/Japan4.jpg", 'rb')
# IGM5 = open("PHOTO/Japan5.jpg", 'rb')
# IGM6 = open("PHOTO/Japan6.jpg", 'rb')
# IGM7 = open("PHOTO/Japan7.jpg", 'rb')
# IGM8 = open("PHOTO/Japan8.jpg", 'rb')
# IGM9 = open("PHOTO/Japan9.jpg", 'rb')
# IGM10 = open("PHOTO/Japan10.jpg", 'rb')
# IGM11 = open("PHOTO/Japan11.jpg", 'rb')
# JAPAN = [IGM4, IGM3, IGM2, IGM1, IGM5, IGM6, IGM7, IGM8, IGM9, IGM10, IGM11]
# ALLJAPAN = choice(JAPAN)
# bot.send_photo(chat_id, ALLJAPAN, )
#
# elif ms_text == "Прислать анекдот":  # .............................................................................
# AN1 = ["Жалоба наркомана:\
#                                                                                             – С утра маковой росинки во рту не было…"]
# AN2 = ["Сидит мужик зимой в туалете. Ну сидит, сидит, вдруг как заорет:\
#                                                                                             – Вот дура, заставила двое кольсон надеть!"]
# AN3 = ["– Помогите, насилуют!\
#                                                                                             Подбежали, помогли."]
#
# AN4 = ["– Знаешь, почему я заплакала? – спрашивает жена мужа, выходя из универмага.\
#                                                                                             – Знаю, но у меня таких денег нет."]
#
# AN5 = ["– Вам следует спать на левом боку.\
#                                                                                             – Это невозможно! Мой муж говорит во сне а я не слышу левым ухом."]
#
# AN6 = ["Чапай с Петькой в бане моются. Петька ему спину трет:\
#                                                                                             – О, Василий Иванович, – майка! А вы говорили – потерялась!.."]
#
# AN7 = ["На АТС:\
#                                                                                                                     – За связь без брака!"]
#
# AN8 = [" Папа, дай мне денег, я хочу сходить в зоопарк на удава посмотреть.\
#                                                                                                         – Возьми лупу и сходи в сад на червяка посмотри."]
#
# AN9 = ["– Доктор, у меня после вашего лекарства все наружу выворачивает.\
#                                                                                                         – Ничего удивительного,лекарство–то наружное."]
#
# AN10 = ["Девушка рассказывает подругам:\
#                                                                                             – Мужик у меня, девчата, настоящий зверь!\
#                                                                                                 Порода – сексуальный ленивец…"]
# ALLAN = [AN1, AN2, AN3, AN4, AN5, AN6, AN7, AN8, AN9, AN10]
# ALLAN = choice(ALLAN)
# bot.send_message(chat_id, text=ALLAN)
#
# elif ms_text == "Управление":  # ...................................................................................
# bot.send_message(chat_id, text="еще не готово...")
#
# elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
# bot.send_message(chat_id, "Автор: Andrei Tregubenko")
# key1 = types.InlineKeyboardMarkup()
# btn1 = types.InlineKeyboardButton(text="Страница автора", url="https://t.me/F1DRAW1")
# key1.add(btn1)
# img = open('PHOTO/AUTHOR.png', 'rb')
# bot.send_photo(message.chat.id, img, reply_markup=key1)
#










#changes



#lol