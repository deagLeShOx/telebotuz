import telebot
import re
import math
import secure
from lang import gettr, chooselang
from telebot import types
from time import sleep
from enum import Enum

bot = telebot.TeleBot(secure.Token)
#Флаг Узбекистана '\U0001F1FA\U0001F1FF'
#Флаг России  '\U0001f1f7\U0001f1fa'

@bot.message_handler(commands=['start'])
def start_message(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Uzbek''\U0001F1FA\U0001F1FF', 'Rus''\U0001f1f7\U0001f1fa']])
    msg = bot.send_message(m.chat.id, '\U0001F1FA\U0001F1FF''Tilni tanlang' '\n''\U0001f1f7\U0001f1fa' 'Выберите язык', reply_markup=keyboard)
    bot.register_next_step_handler(msg,send_text)

@bot.message_handler(content_types=['text'])
def send_text(m):

    if m.text == 'Uzbek''\U0001F1FA\U0001F1FF':
        chooselang(m.chat.id, "uz")
    elif m.text == 'Rus''\U0001f1f7\U0001f1fa':
        chooselang(m.chat.id, "ru")  
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'calc'), gettr(m.chat.id, 'converter'),]])
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'langselect'), parse_mode= 'Markdown', reply_markup=keyboard)
    bot.register_next_step_handler(msg,name)
    #Конвертер юникоде \U0001F504
    #Калькулятор юникоде ''\U0001F522''
    
def name(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    if m.text == gettr(m.chat.id, 'calc'):
        bot.send_message(m.chat.id, gettr(m.chat.id, 'calc_mod'), parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'back')]])
        #markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'calc_ae'), reply_markup=keyboard)
        bot.register_next_step_handler(msg, calculator)
    elif m.text == gettr(m.chat.id, 'converter'):
        bot.send_message(m.chat.id, gettr(m.chat.id, 'converter_mod'), parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['2 ➝ 10', '10 ➝ 2', '2 ➝ 16', '16 ➝ 2', '10 ➝ 16', '16 ➝ 10','2 ➝ 8', '8 ➝ 2', '10 ➝ 8', '8 ➝ 10', '8 ➝ 16', '16 ➝ 8', gettr(m.chat.id, 'back')]])
        msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'converter_type'), reply_markup=keyboard)
        bot.register_next_step_handler(msg, convert)

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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'bin'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'dec'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'bin'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'hex'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'dec'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'hex'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'bin'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'oct'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'dec'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'oct'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'oct'), parse_mode = 'Markdown', reply_markup=markup)
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'hex'), parse_mode = 'Markdown', reply_markup=markup)
    bot.register_next_step_handler(msg, shvs)



def back(m):
    if m.text == gettr(m.chat.id, 'back'):
        bot.send_message(m.chat.id, gettr(m.chat.id, ''))
        send_text(m)
        return

def calculator(m):
    if m.text == gettr(m.chat.id, 'back'):
        #bot.send_message(m.chat.id, gettr(m.chat.id, ''))
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
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'calc_ae'), reply_markup=keyboard)
    bot.register_next_step_handler(msg, calculator)

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

bot.polling()