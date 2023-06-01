import telebot
from telebot import types
import wikipedia

bot = telebot.TeleBot('5717757940:AAGUiX7TsetGR6zxflhrmQEh2Fmo9qknZUc')
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Впишіть назву сатті')
@bot.message_handler(content_types=['text'])
def handler_text(message):
    name = message.text
    wikipedia.set_lang("uk")
    if wikipedia.summary(name, chars= 1000):
        answer = wikipedia.summary(name, chars= 1000)
    else:
        answer = 'Такої статті не існує'
    bot.send_message(message.chat.id, answer)

bot.polling()

