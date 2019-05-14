import telebot
import re
import math
import secure
from lang import gettr, chooselang
from telebot import types
from time import sleep
from enum import Enum

bot = telebot.TeleBot(secure.Token)
#keyboard1 = telebot.types.ReplyKeyboardMarkup()
#keyboard1.row('Uzbek''\U0001F1FA\U0001F1FF', 'Rus''\U0001f1f7\U0001f1fa')
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
    #markup = types.ReplyKeyboardRemove(selective=False)
    if m.text == 'Uzbek''\U0001F1FA\U0001F1FF':
        chooselang(m.chat.id, "uz")
    elif m.text == 'Rus''\U0001f1f7\U0001f1fa':
        chooselang(m.chat.id, "ru")  
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [gettr(m.chat.id, 'calc'), gettr(m.chat.id, 'converter')]])
    msg = bot.send_message(m.chat.id, gettr(m.chat.id, 'langselect'), parse_mode= 'Markdown', reply_markup=keyboard)
    bot.register_next_step_handler(msg,name)

    #Konverter unicod ''\U0001F504'
    #Kalkulyator unicod \U0001F522
    #Конвертер юникоде \U0001F504
    #Калькулятор юникоде ''\U0001F522''
    
def name(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    if m.text == gettr(m.chat.id, 'calc'):
        bot.send_message(m.chat.id, '`Siz Kalkulyator rejimidasiz`', parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Orqaga']])
        #markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Arifmetik amalni kiriting:', reply_markup=keyboard)
        bot.register_next_step_handler(msg, calculatoruz)
    elif m.text == gettr(m.chat.id, 'converter'):
        bot.send_message(m.chat.id, '`Siz Konverter rejimidasiz`', parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['2 ➝ 10', '10 ➝ 2', '2 ➝ 16', '16 ➝ 2', '10 ➝ 16', '16 ➝ 10','2 ➝ 8', '8 ➝ 2', '10 ➝ 8', '8 ➝ 10', '8 ➝ 16', '16 ➝ 8', "Orqaga" ]])
        msg = bot.send_message(m.chat.id, 'Konvertatsiya qilish turini tanlang', reply_markup=keyboard)
        bot.register_next_step_handler(msg,convertuz)
def name123(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    if m.text == 'Калькулятор''\U0001F522':
        bot.send_message(m.chat.id, '`Вы в режиме Калькулятор`', parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад']])
        #markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите арифметическое выражение:', reply_markup=keyboard)
        bot.register_next_step_handler(msg, calculator)
    elif m.text == 'Конвертер''\U0001F504':
        bot.send_message(m.chat.id, '`Вы в режиме Конвертер`', parse_mode= 'Markdown', reply_markup=markup)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['2 ➝ 10', '10 ➝ 2', '2 ➝ 16', '16 ➝ 2', '10 ➝ 16', '16 ➝ 10','2 ➝ 8', '8 ➝ 2', '10 ➝ 8', '8 ➝ 10', '8 ➝ 16', '16 ➝ 8', "Назад" ]])
        msg = bot.send_message(m.chat.id, 'Выберите режим конвертации', reply_markup=keyboard)
        bot.register_next_step_handler(msg,convert)


# **Системы счисления **
#2 int(msg, 2)
#10 format (int (msg), "b")
#16 format (int (msg), '02x')
#8 format (int (m.text, 8), "b")


#RU

# 2 ➝ 10
def dvds(m):

    if m.text == 'Назад':
        start(m)
        return
    try:
        c = str(int(m.text, 2))
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Введите число в двоичной системе:', reply_markup=markup)
    bot.register_next_step_handler(msg, dvds)

#'10 ➝ 2'
def dsdv(m):

    if m.text == 'Назад':
        start(m)
        return
    try:
        c = format(int (m.text), "b")
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Введите число в десятичной системе:', reply_markup=markup)
    bot.register_next_step_handler(msg, dsdv)

#'2 ➝ 16'
def dvsh(m):

    if m.text == 'Назад':
        start(m)
        return
    try:
        c = format (int (m.text, 2), '0x') 
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Введите число в двоичной системе:', reply_markup=markup)
    bot.register_next_step_handler(msg, dvsh)

#'16 ➝ 2'   
def shdv(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = format (int (m.text, 16), "b") 
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Введите число в шестнадцатеричной системе:', reply_markup=markup)
    bot.register_next_step_handler(msg, shdv)

#'10 ➝ 16', 
def dssh(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = format (int (m.text), '0x')  
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Введите число в десятичной системе:', reply_markup=markup)
    bot.register_next_step_handler(msg, dssh)


#'16 ➝ 10'
def shds(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = str(int (m.text, 16)) 
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Введите число в шестнадцатеричной системе:', reply_markup=markup)
    bot.register_next_step_handler(msg, shds)

#'2 ➝ 8'
def dvvs(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = str(int(m.text, 8))
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Введите число в двоичной системе', reply_markup=markup)
    bot.register_next_step_handler(msg, dvvs)

#'8 ➝ 2'
def vsdv(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = format (int (m.text, 8), "b")
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Введите число в восьмеричной системе', reply_markup=markup)
    bot.register_next_step_handler(msg, vsdv)

#'10 ➝ 8'
def dsvs(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = str (int (m.text, 8))
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Введите число в десятичной системе', reply_markup=markup)
    bot.register_next_step_handler(msg, dsvs)

#'8 ➝ 10'
def vsds(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = str (int (m.text, 8))
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Введите число в восьмеричной системе', reply_markup=markup)
    bot.register_next_step_handler(msg, vsds)

#'8 ➝ 16'
def vssh(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = format (int (m.text, 8), "0x")
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Введите число в восьмеричной системе', reply_markup=markup)
    bot.register_next_step_handler(msg, vssh)

#'16 ➝ 8'
def shvs(m):
    if m.text == 'Назад':
        start(m)
        return
    try:
        c = format (int (m.text, 16), "010")
    except:
        c = "Ошибка"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Введите число в шестнадцатеричной системе', reply_markup=markup)
    bot.register_next_step_handler(msg, shvs)

def back(m):
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
    msg = bot.send_message(m.chat.id, 'Введите арифметическое выражение:', reply_markup=keyboard)
    bot.register_next_step_handler(msg, calculator)

def convert(m):
    if m.text == '2 ➝ 10':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в двоичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, dvds)
    elif m.text == '10 ➝ 2':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в десятичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, dsdv) 
    elif m.text == '2 ➝ 16':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в двоичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, dvsh)
    elif m.text == '16 ➝ 2':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в шестнадцатеричной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, shdv)
    elif m.text == '10 ➝ 16':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в десятичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, dssh)
    elif m.text == '16 ➝ 10':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в шестнадцатеричной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, shds)
    elif m.text == '2 ➝ 8':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в двоичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, dvvs)
    elif m.text == '8 ➝ 2':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в восьмеричной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, vsdv)
    elif m.text == '8 ➝ 10':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в восьмеричной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, vsds)
    elif m.text == '10 ➝ 8':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в десятичной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, dsvs)
    elif m.text == '8 ➝ 16':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в восьмеричной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, vssh)
    elif m.text == '16 ➝ 8':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Введите число в шестнадцатеричной системе:', reply_markup=markup)
        bot.register_next_step_handler(msg, shvs)
    elif m.text == 'Назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Калькулятор''\U0001F522', 'Конвертер''\U0001F504']])
        msg = bot.send_message(m.chat.id, 'Выберите режим' '\U0001F522''\U0001F504', reply_markup=keyboard)
        bot.register_next_step_handler(msg,name)(msg, back)



#UZ



# 2 ➝ 10
def ikun(m):

    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = str(int(m.text, 2))
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Ikkilik sanoq sistemasida raqam kiriting', reply_markup=markup)
    bot.register_next_step_handler(msg, ikun)

#'10 ➝ 2'
def unik(m):

    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = format(int (m.text), "b")
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, "O'nlik sanoq sistemasida raqam kiriting", reply_markup=markup)
    bot.register_next_step_handler(msg, unik)

#'2 ➝ 16'
def ikuo(m):

    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = format (int (m.text, 2), '0x') 
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Ikkilik sanoq sistemasida raqam kiriting', reply_markup=markup)
    bot.register_next_step_handler(msg, ikuo)

#'16 ➝ 2'   
def uoik(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = format (int (m.text, 16), "b") 
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, "O'n oltilik sanoq sistemasida belgi kiriting", reply_markup=markup)
    bot.register_next_step_handler(msg, uoik)

#'10 ➝ 16', 
def unuo(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = format (int (m.text), '0x')  
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, "O'nlik sanoq sistemasida raqam kiriting", reply_markup=markup)
    bot.register_next_step_handler(msg, unuo)

#'16 ➝ 10'
def uoun(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = str(int (m.text, 16)) 
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, "O'n oltilik sanoq sistemasida belgi kiriting", reply_markup=markup)
    bot.register_next_step_handler(msg, uoun)

#'2 ➝ 8'
def iksa(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = str(int(m.text, 8))
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Ikkilik sanoq sistemasida raqam kiriting', reply_markup=markup)
    bot.register_next_step_handler(msg, iksa)

#'8 ➝ 2'
def saik(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = format (int (m.text, 8), "b")
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Sakkizlik sanoq sistemasida raqam kiriting', reply_markup=markup)
    bot.register_next_step_handler(msg, saik)

#'10 ➝ 8'
def unsa(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = str (int (m.text, 8))
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, "O'nlik sanoq sistemasida raqam kiriting", reply_markup=markup)
    bot.register_next_step_handler(msg, unsa)

#'8 ➝ 10'
def saun(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = str (int (m.text, 8))
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Sakkizlik sanoq sistemasida raqam kiriting', reply_markup=markup)
    bot.register_next_step_handler(msg, saun)

#'8 ➝ 16'
def sauo(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = format (int (m.text, 8), "0x")
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, 'Sakkizlik sanoq sistemasida raqam kiriting', reply_markup=markup)
    bot.register_next_step_handler(msg, sauo)

#'16 ➝ 8'
def uosa(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    try:
        c = format (int (m.text, 16), "010")
    except:
        c = "Xatolik"
    msg = bot.send_message(m.chat.id, c)
    markup = bot.send_message(m.chat.id, "O'n oltilik sanoq sistemasida belgi kiriting", reply_markup=markup)
    bot.register_next_step_handler(msg, uosa)

def backuz(m):
    if m.text == 'Orqaga':
        startuz(m)
        return

def calculatoruz(m):
    if m.text == 'Orqaga':
        startuz(m)
        return
    s = ""
    try:
        pattern = re.compile("^([-+]*[0-9]*\.?[0-9]+[\/\+\-\*\(\)\^\%]*)*$")
        if pattern.match(m.text):
            s = eval(m.text)
        else:
            s = "Ifodada taqiqlangan belgilar mavjud"
    except:
        s = "Ifodada xatolik"
    msg = bot.send_message(m.chat.id, s)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(m.chat.id, 'Arifmetik ifoda kiriting:', reply_markup=keyboard)
    bot.register_next_step_handler(msg, calculatoruz)


#'Ikkilik sanoq sistemasida raqam kiriting:'
#'Sakkizlik sanoq sistemasida raqam kiriting:'
#"O'nlik sanoq sistemasida raqam kiriting:"
#"O'n oltilik sanoq sistemasida belgi kiriting:"
def convertuz(m):
    if m.text == '2 ➝ 10':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Ikkilik sanoq sistemasida raqam kiriting:', reply_markup=markup)
        bot.register_next_step_handler(msg, ikun)
    elif m.text == '10 ➝ 2':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, "O'nlik sanoq sistemasida raqam kiriting:", reply_markup=markup)
        bot.register_next_step_handler(msg, unik) 
    elif m.text == '2 ➝ 16':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Ikkilik sanoq sistemasida raqam kiriting:', reply_markup=markup)
        bot.register_next_step_handler(msg, ikuo)
    elif m.text == '16 ➝ 2':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, "O'n oltilik sanoq sistemasida belgi kiriting:", reply_markup=markup)
        bot.register_next_step_handler(msg, uoik)
    elif m.text == '10 ➝ 16':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, "O'nlik sanoq sistemasida raqam kiriting:", reply_markup=markup)
        bot.register_next_step_handler(msg, unuo)
    elif m.text == '16 ➝ 10':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, "O'n oltilik sanoq sistemasida belgi kiriting:", reply_markup=markup)
        bot.register_next_step_handler(msg, uoun)
    elif m.text == '2 ➝ 8':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Sakkizlik sanoq sistemasida raqam kiriting:', reply_markup=markup)
        bot.register_next_step_handler(msg, iksa)
    elif m.text == '8 ➝ 2':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Sakkizlik sanoq sistemasida raqam kiriting:', reply_markup=markup)
        bot.register_next_step_handler(msg, saik)
    elif m.text == '8 ➝ 10':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Sakkizlik sanoq sistemasida raqam kiriting:', reply_markup=markup)
        bot.register_next_step_handler(msg, saun)
    elif m.text == '10 ➝ 8':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, "O'nlik sanoq sistemasida raqam kiriting:", reply_markup=markup)
        bot.register_next_step_handler(msg, unsa)
    elif m.text == '8 ➝ 16':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, 'Sakkizlik sanoq sistemasida raqam kiriting:', reply_markup=markup)
        bot.register_next_step_handler(msg, sauo)
    elif m.text == '16 ➝ 8':
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(m.chat.id, "O'n oltilik sanoq sistemasida belgi kiriting:", reply_markup=markup)
        bot.register_next_step_handler(msg, uosa)
    elif m.text == 'Orqaga':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Kalkulyator''\U0001F522', 'Konverter''\U0001F504']])
        msg = bot.send_message(m.chat.id, 'Rejimni tanlang''\U0001F522''\U0001F504', reply_markup=keyboard)
        bot.register_next_step_handler(msg,nameuz)(msg, backuz)
bot.polling()