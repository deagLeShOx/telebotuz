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

lang_ru['converter_type'] = 'Выберите режим конвертации'
lang_uz['converter_type'] = 'Konvertatsiya qilish turini tanlang'

lang_ru['langselect'] = "Вы выбрали *Русский язык* \nТеперь выберите режим \U0001F522 \U0001F504"
lang_uz['langselect'] = "Siz *O'zbek tili*ni tanladingiz \nEndi kerakli rejimni tanlang \U0001F522 \U0001F504"

lang_ru['example_bin'] = 'Пример в двоичной системе: `11111100011`'
lang_uz['example_bin'] = 'Ikkilik sanoq sistemasida Namuna: `11111100011`'

lang_ru['example_oct'] = 'Пример в восьмеричной системе: `01234567`'
lang_uz['example_oct'] = 'Sakkizlik sanoq sistemasida Namuna: `01234567`'

lang_ru['example_dec'] = 'Пример в десятичной системе: `0123456789`'
lang_uz['example_dec'] = "O'nlik sanoq sistemasida Namuna: `0123456789`"

lang_ru['example_hex'] = 'Пример в шестнадцатеричной системе: `0123456789ABCDEF`'
lang_uz['example_hex'] = "O'n oltilik sanoq sistemasida Namuna: `0123456789ABCDEF`"

lang_ru['back'] = 'Назад'
lang_uz['back'] = 'Orqaga'

lang_ru['error'] = "Ошибка!\n_для выхода из режима Конвертации пишите_   *Назад*"
lang_uz['error'] = "Xatolik\n_Konvertatsiyalash rejimidan chiqish uchun_  *Orqaga*  _yozing_"

lang_ru['bin'] = 'Введите число в двоичной системе:''\n_для выхода из режима Конвертации пишите_   *Назад*'
lang_uz['bin'] = 'Ikkilik sanoq sistemasida raqam kiriting''\n_Konvertatsiyalash rejimidan chiqish uchun_  *Orqaga*  _yozing_'

lang_ru['dec'] = 'Введите число в десятичной системе:''\n_для выхода из режима Конвертации пишите_   *Назад*'
lang_uz['dec'] = "O'nlik sanoq sistemasida raqam kiriting"'\n_Konvertatsiyalash rejimidan chiqish uchun_  *Orqaga*  _yozing_'

lang_ru['hex'] = 'Введите число в шестнадцатеричной системе''\n_для выхода из режима Конвертации пишите_   *Назад*'
lang_uz['hex'] = "O'n oltilik sanoq sistemasida belgi kiriting"'\n_Konvertatsiyalash rejimidan chiqish uchun_  *Orqaga*  _yozing_'

lang_ru['oct'] = 'Введите число в восьмеричной системе''\n_для выхода из режима Конвертации пишите_   *Назад*'
lang_uz['oct'] = 'Sakkizlik sanoq sistemasida raqam kiriting''\n_Konvertatsiyalash rejimidan chiqish uchun_  *Orqaga*  _yozing_'

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