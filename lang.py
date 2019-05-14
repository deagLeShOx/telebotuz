lang_ru = {}
lang_uz = {}

lang_ru['calc'] = 'Калькулятор''\U0001F522'
lang_uz['calc'] = 'Kalkulyator''\U0001F522'

lang_ru['select_type'] = "Выберите режим"
lang_uz['select_type'] = "Rejimni tanlang"

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

lang_ru['error'] = "Ошибка"
lang_ru['error'] = "Xatolik"

lang_ru['bin'] = 'Введите число в двоичной системе:'
lang_uz['bin'] = 'Ikkilik sanoq sistemasida raqam kiriting'

lang_ru['dec'] = 'Введите число в десятичной системе:'
lang_uz['dec'] = "O'nlik sanoq sistemasida raqam kiriting"

lang_ru['hex'] = 'Введите число в шестнадцатеричной системе'
lang_uz['hex'] = "O'n oltilik sanoq sistemasida belgi kiriting"

lang_ru['oct'] = 'Введите число в восьмеричной системе'
lang_uz['oct'] = 'Sakkizlik sanoq sistemasida raqam kiriting'

lang_ru['taboo_char'] = "В выражении присутствуют запрещённые символы"
lang_uz['taboo_char'] = "Ifodada taqiqlangan belgilar mavjud"

lang_ru['error_exp'] = "Ошибка в выражении"
lang_uz['error_exp'] = "Ifodada xatolik"


ulang = {}
lang = {}
lang["ru"] = lang_ru
lang["uz"] = lang_uz

def chooselang(id, lang):
    ulang[id] = lang

def gettr(id, const):
    return lang[ulang[id]][const]