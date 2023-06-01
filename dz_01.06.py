import telebot
from telebot import types
import wikipedia
import requests

bot = telebot.TeleBot('5717757940:AAGUiX7TsetGR6zxflhrmQEh2Fmo9qknZUc')
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Впишіть назву сатті')
@bot.message_handler(content_types=['text'])
def handler_text(message):
    name = message.text
    wikipedia.set_lang("uk")
    response = requests.get('https://uk.wikipedia.org/wiki/' + name)
    if response.status_code == 200:
        if wikipedia.summary(name, chars=1000):
            answer = f"Ось інформація, яку вдалося знайти:\n\n" \
                     f"{'https://uk.wikipedia.org/wiki/' + name}\n\n" \
                     f"{wikipedia.summary(name, chars=1000)}\n\nПродовження за посиланням:\n\n" \
                     f"{'https://uk.wikipedia.org/wiki/' + name}"

        else:
            answer = 'Сталася помилка у виконанні.'
    else:
        answer = f'Статті з назвою "{name}" не знайдено.'
    bot.send_message(message.chat.id, answer)

bot.polling()

