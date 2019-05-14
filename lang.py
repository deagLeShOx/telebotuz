lang_ru = {}
lang_uz = {}

lang_ru['calc'] = 'Калькулятор''\U0001F522'
lang_uz['calc'] = 'Kalkulyator''\U0001F522'

lang_ru['converter'] = 'Конвертер''\U0001F504'
lang_uz['converter'] = 'Konverter''\U0001F504'

lang_ru['langselect'] = "Вы выбрали *Русский язык* \nТеперь выберите режим \U0001F522 \U0001F504"
lang_uz['langselect'] = "Siz *O'zbek tili*ni tanladingiz \nEndi kerakli rejimni tanlang \U0001F522 \U0001F504"

lang_ru['back'] = 'Назад'
lang_uz['back'] = 'Orqaga'

lang_ru['error'] = 'Ошибка'
lang_ru['error'] = 'Xatolik'

lang_ru['dvds'] = 'Введите число в двоичной системе:'
lang_uz['dvds'] = 'Ikkilik sanoq sistemasida raqam kiriting'

ulang = {}
lang = {}
lang["ru"] = lang_ru
lang["uz"] = lang_uz

def chooselang(id, lang):
    ulang[id] = lang

def gettr(id, const):
    return lang[ulang[id]][const]