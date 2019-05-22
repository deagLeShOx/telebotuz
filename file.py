import telebot
import re
import math
import secure
from lang import gettr, chooselang
from telebot import types
from time import sleep
from enum import Enum

bot = telebot.TeleBot(secure.Token)

@bot.message_handler(commands=['start'])
def start_message(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Uzbek''\U0001F1FA\U0001F1FF', 'Rus''\U0001f1f7\U0001f1fa']])
    msg = bot.send_message(m.chat.id, '\U0001F1FA\U0001F1FF''Tilni tanlang' '\n''\U0001f1f7\U0001f1fa' 'Выберите язык', reply_markup=keyboard)
    bot.register_next_step_handler(msg,send_text)


@bot.message_handler(content_types=['text'])
def help(m):
    bot.send_message(m.chat.id, '\U0001f1f7\U0001f1fa''Введите /start для начала\n\U0001F1FA\U0001F1FF''Boshlash uchun /start komandasini yozing')


def send_text(m):
    if m.text == 'Uzbek''\U0001F1FA\U0001F1FF':
        chooselang(m.chat.id, "uz")
    elif m.text == 'Rus''\U0001f1f7\U0001f1fa':
        chooselang(m.chat.id, "ru")  
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'calc'), gettr(m.chat.id, 'converter'), gettr(m.chat.id, 'trigonometry'), gettr(m.chat.id, 'square')]])
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'langselect'), parse_mode= 'Markdown', reply_markup=keyboard)
    bot.register_next_step_handler(msg,name)

    
def name(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    if m.text == gettr(m.chat.id, 'calc'):
        bot.send_message(m.chat.id, gettr(m.chat.id, 'calc_mod'), parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'calc_ae'), reply_markup=keyboard)
        bot.register_next_step_handler(msg, calculator)
    elif m.text == gettr(m.chat.id, 'converter'):
        bot.send_message(m.chat.id, gettr(m.chat.id, 'converter_mod'), parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['2 ➝ 10', '10 ➝ 2', '2 ➝ 16', '16 ➝ 2', '10 ➝ 16', '16 ➝ 10','2 ➝ 8', '8 ➝ 2', '10 ➝ 8', '8 ➝ 10', '8 ➝ 16', '16 ➝ 8', gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'converter_type'), reply_markup=keyboard)
        bot.register_next_step_handler(msg, convert)
    elif m.text == gettr(m.chat.id, 'trigonometry'):
        bot.send_message(m.chat.id, gettr(m.chat.id, 'trig_mod'), parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'cos'), gettr(m.chat.id, 'sin'), gettr(m.chat.id, 'tg'), gettr(m.chat.id, 'ctg')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'trig_ae'), reply_markup=keyboard)
        bot.register_next_step_handler(msg, trig)
    elif m.text == gettr(m.chat.id, 'square'):
        bot.send_message(m.chat.id, gettr(m.chat.id, 'square_ae'), parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'square_mod'), parse_mode= 'Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, square)


# 2 ➝ 10
def dvds(m):

    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = str(int(m.text, 2))
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, dvds)

#'10 ➝ 2'
def dsdv(m):

    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text), "b")
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, dsdv)

#'2 ➝ 16'
def dvsh(m):

    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text, 2), "0x") 
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, dvsh)

#'16 ➝ 2'   
def shdv(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text, 16), "b") 
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, shdv)

#'10 ➝ 16', 
def dssh(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text), "0x")
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, dssh)

#'16 ➝ 10'
def shds(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = str(int (m.text, 16))
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, shds)

#'2 ➝ 8'
def dvvs(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text, 2), "0")
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, dvvs)

#'8 ➝ 2'
def vsdv(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text, 8), "b")
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, vsdv)

#'10 ➝ 8'
def dsvs(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text), "0o")
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, dsvs)

#'8 ➝ 10'
def vsds(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = str(int(m.text, 8))
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, vsds)

#'8 ➝ 16'
def vssh(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text, 8), "0x")
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, vssh)

#'16 ➝ 8'
def shvs(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        c = format(int (m.text, 16), "0o") 
    except:
        c = gettr(m.chat.id, 'error')
    msg = bot.send_message(m.chat.id, c)
    bot.register_next_step_handler(msg, shvs)


#Назад
def back(m):
    if m.text == gettr(m.chat.id, 'back'):
        bot.send_message(m.chat.id, gettr(m.chat.id, ''))
        send_text(m)
        return


#Калькулятор
def calculator(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    s = ""
    try:
        pattern = re.compile("^([-+]*[0-9]*\.?[0-9]+[\/\+\-\*\(\)\^\%]*)*$")
        if pattern.match(m.text):
            s = eval(m.text)
        else:
            s = gettr(m.chat.id, 'taboo_char')
    except:
        s = gettr(m.chat.id, 'error_exp')
    msg = bot.send_message(m.chat.id, s)
    bot.register_next_step_handler(msg, calculator)


#Конвертер
def convert(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    if m.text == '2 ➝ 10':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'bin'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_bin'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dvds)
    elif m.text == '10 ➝ 2':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'dec'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_dec'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dsdv) 
    elif m.text == '2 ➝ 16':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'bin'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_bin'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dvsh)
    elif m.text == '16 ➝ 2':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'hex'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_hex'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, shdv)
    elif m.text == '10 ➝ 16':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'dec'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_dec'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dssh)
    elif m.text == '16 ➝ 10':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'hex'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_hex'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, shds)
    elif m.text == '2 ➝ 8':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'bin'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_bin'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dvvs)
    elif m.text == '8 ➝ 2':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'oct'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_oct'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, vsdv)
    elif m.text == '8 ➝ 10':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'oct'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_oct'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, vsds)
    elif m.text == '10 ➝ 8':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'dec'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_dec'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dsvs)
    elif m.text == '8 ➝ 16':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'oct'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_oct'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, vssh)
    elif m.text == '16 ➝ 8':
        bot.send_message(m.chat.id, gettr(m.chat.id, 'hex'), parse_mode='Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_hex'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, shvs)
    elif m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return


#cos Функция
def cosFoo(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        d = math.cos (float(m.text))
    except:
        d = gettr(m.chat.id, 'error_cos')
    msg = bot.send_message(m.chat.id, d)
    bot.register_next_step_handler(msg, cosFoo)

#sin Функция
def sinFoo(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        d = math.sin (float(m.text))
    except:
        d = gettr(m.chat.id, 'error_sin')
    msg = bot.send_message(m.chat.id, d)
    bot.register_next_step_handler(msg, sinFoo)

#tg Функция
def tgFoo(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        d = math.tg(float(m.text))
    except:
        d = gettr(m.chat.id, 'error_tg')
        msg = bot.send_message(m.chat.id, d)
        bot.register_next_step_handler(msg, tgFoo)

#ctg Функция
def ctgFoo(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        d = math.ctg(float(m.text))
    except:
        d = gettr(m.chat.id, 'error_ctg')
        msg = bot.send_message(m.chat.id, d)
        bot.register_next_step_handler(msg, ctgFoo)


def trig(m):
    if m.text == gettr(m.chat.id, 'cos'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_cos'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, cosFoo)
    elif m.text == gettr(m.chat.id, 'sin'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_sin'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sinFoo)
    elif m.text == gettr(m.chat.id, 'tg'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_tg'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, tgFoo)
    elif m.text == gettr(m.chat.id, 'ctg'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'example_ctg'), parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sinFoo)



#Квадратное уравнение
def square(m):
    if m.text == gettr(m.chat.id, 'back'):
        send_text(m)
        return
    try:
        a, b, c = map(int, m.text.split())
        if a == 0:
            if b == 0 and c != 0:
                q = gettr(m.chat.id, 'square_no_solutions')
            else:              
                q = str(-c/b)
        else:    
            D = b*b-4*a*c
            if D<0:
                q = gettr(m.chat.id, 'square_no_solutions')
            elif D == 0:
                q = str(-b/(2*a))
            else:
                dis = math.sqrt(D)
                x1 = (-b + dis)/(2*a)
                x2 = (-b - dis)/(2*a)
                q = "x1 = "+str(x1)+"\nx2 = "+str(x2)
    except:
        q = gettr(m.chat.id, 'error_square')
    msg = bot.send_message(m.chat.id, q)
    bot.register_next_step_handler(msg, square)

bot.polling()