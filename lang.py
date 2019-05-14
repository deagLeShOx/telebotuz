lang_ru = {}
lang_uz = {}

lang_ru['calc'] = 'Калькулятор''\U0001F522'
lang_uz['calc'] = 'Kalkulyator''\U0001F522'

lang_ru['calc_mod'] = '`Вы в режиме Калькулятор`'
lang_uz['calc_mod'] = '`Siz Kalkulyator rejimidasiz`'

lang_ru['calc_ae'] = 'Введите арифметическое выражение:'
lang_uz['calc_ae'] = 'Arifmetik amalni kiriting:'

lang_ru['converter'] = 'Конвертер''\U0001F504'
lang_uz['converter'] = 'Konverter''\U0001F504'

lang_ru['converter_mod'] = '`Вы в режиме Конвертер`'
lang_uz['converter_mod'] = '`Siz Konverter rejimidasiz`'

lang_ru['converter_type'] = 'Konvertatsiya qilish turini tanlang'
lang_uz['converter_type'] = 'Выберите режим конвертации'

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