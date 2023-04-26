from telebot import types
import telebot
import random

f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
f = open('quotes.txt', 'r', encoding='UTF-8')
quotes = f.read().split('\n')
f.close()

# создаем экземпляр объекта
api_token = ('5991347930:AAFfdsKSEVKHraC2QG4Y7rzvpBqekhdqWz8')
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):

    # добавляем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonA = types.KeyboardButton("Факт")
    buttonB = types.KeyboardButton("Цитата")

    # располагаем кнопки в ряд
    markup.row(buttonA,buttonB)
    bot.send_message(message.chat.id,text='Нажми: \nФакт для получения интересного факта о Python\nЦитата — для получения цитаты',reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):

# если пользователь прислал 'Факт', выдаем ему случайный факт о Python
    if message.text.strip() == 'Факт' :
        answer = random.choice(facts)

# если поьзователь прислал 'Цитата', выдаем умную мысль
    elif message.text.strip() == 'Цитата':
        answer = random.choice(quotes)

# отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)
