import telebot
import re
import math
import secure
from telebot import types
from time import sleep
from enum import Enum

bot = telebot.TeleBot(secure.Token)

@bot.message_handler(commands=['start'])

def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Калькулятор', 'Конвертер']])
    msg = bot.send_message(m.chat.id, 'Выберите режим', reply_markup=keyboard)
    bot.register_next_step_handler(msg,name)
def name(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    if m.text == 'Калькулятор':
        msg = bot.send_message(m.chat.id, 'Вы в режиме Калькулятор', reply_markup=markup)
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите арифметическое выражение:', reply_markup=markup)
        bot.register_next_step_handler(msg, calculator) 
    elif m.text == 'Конвертер':
        bot.send_message(m.chat.id, 'Вы в режиме Конвертер', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['2 ➝ 10', '10 ➝ 2', '2 ➝ 16', '16 ➝ 2', '10 ➝ 16', '16 ➝ 10']])
        msg = bot.send_message(m.chat.id, 'Выберите режим', reply_markup=keyboard)
        bot.register_next_step_handler(msg,name)

def dv(m):
    if m.text == 'Назад':
        start(m)
    return

def calculator(m):
    if m.text == 'Назад':
        start(m)
        return
    s = ""
    try:
        pattern = re.compile("^([-+]*[0-9]*\.?[0-9]+[\/\+\-\*\(\)\^\%]*)*$")
        if pattern.match(m.text):
            s = eval(m.text)
        else:
            s = "В выражении присутствуют запрещённые символы"
    except:
        s = "Ошибка в выражении"
    msg = bot.send_message(m.chat.id, s)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Введите арифметическое выражение:', reply_markup=markup)
    bot.register_next_step_handler(msg, calculator)

def convert(m):

    if m.text == '2 ➝ 10':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в двоичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, dv) 
    elif m.text == '10 ➝ 2':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в десятичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, ds) 

bot.polling()