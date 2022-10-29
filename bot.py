
import re
import telebot
from telebot import types
bot = telebot.TeleBot("token")


pattern = "(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})"
@bot.message_handler(commands=['start', 'домики'])
def start(message):
    mess = f'Здравствуйте! Хотите узнать подробнее о курсе "Домики" 🏘️?'
    bot.send_message(message.chat.id,mess,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Узнать о курсе')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Кликните на кнопку ниже", reply_markup=markup)
@bot.message_handler()
def start(message):
    global user_data
    user_data = []
    lid_message = f'С вами свяжется мой помощник и расскажет все о курсе. Напишите ваш номер телефона'
    sent_get_message = bot.send_message(message.chat.id,lid_message,parse_mode='html')
    bot.register_next_step_handler(sent_get_message ,  get_user_phone)
@bot.message_handler()
def get_user_phone(message):
    global user_phone, pattern
    if re.fullmatch(pattern, message.text):
        get_user_name(message)
    else:
        msg = bot.send_message(message.chat.id, "Напишите номер в формате 8XXXXXXXXXX")
        bot.register_next_step_handler(msg,  get_user_phone)

def get_user_name(message):
            get_name = bot.send_message(message.chat.id,'Напишите ваше имя',parse_mode='html')
            user_phone = message.text
            user_data.append( user_phone )
            bot.register_next_step_handler(get_name,  say_bye)

def say_bye(message):
            bot.send_message(message.chat.id,'До свидания, с вами свяжется специалист',parse_mode='html')
            user_name = message.text
            user_data.append(user_name)
            print(user_data)


    




bot.infinity_polling()


    
