import telebot
import requests
from telebot import types

# создаем экземпляр объекта
api_token = ('5991347930:AAFfdsKSEVKHraC2QG4Y7rzvpBqekhdqWz8')
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Хочу ещё котика!")

    # размещаем кнопки в ряд
    markup.row(button)
    bot.send_message(message.chat.id,text='Привет, я бот, который очень любит котиков!\nНапиши мне /send_cat или нажми на кнопку и я отправлю тебе своего друга! )', reply_markup=markup)

# получение ссылки на картинку с котиком
def get_cat():
    try:
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
    except:
        url = get_cat()
    return url

# отправка котиков
@bot.message_handler(commands=['send_cat'])
def send_cat(message):
    bot.send_photo(message.chat.id, photo=get_cat())

# обработчик клавиатуры
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Хочу ещё котика!' :
        send_cat(message)

bot.polling(none_stop=True, interval=0)
