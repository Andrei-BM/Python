# Переводим английские числительные в русские в выбранном файле.
# 1й вариант с использованием модуля  googletrans.
from googletrans import Translator
translator = Translator()


def func_trans(a):

    text = translator.translate(a, dest='ru')
    return text.text

with open('task04.txt', 'r', encoding='utf-8') as f:
    for line in f:
        newline = '' # Создаем новую строку в которую будет складывать полученные значения.
        for el in line.split():
            check = el[1:] if el.startswith('\ufeff') else el[:] # "Выкидываем" символы кодировки.

            if check.encode('ascii', errors='ignore').isalpha(): # Ищем английские слова "в слепую" для этого принудительно
                newline = line.replace(el, func_trans(check))    # кодируем и проверяем результат. Потом переводим.
                break
        with open('new04.txt', 'a', encoding='utf=8') as n:
            n.seek(0)
            n.write(newline)


# 2-й вариант с использованием созданного словаря.
translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

with open('task04.txt', 'r', encoding='utf-8') as f:
    for line in f:
        newline = ''
        for el in line.split():
            el = el[1:] if el.startswith('\ufeff') else el
            if el.lower() in translate.keys(): # Здесь в элементах строки мы ищем совпадения в созданном словаре.
                new_el = translate[el.lower()].capitalize() # Если оно есть добавлем новое значение вместо старого.
                newline = line.replace(el, new_el)
                break

        with open('new04.txt', 'a', encoding='utf=8') as n:
            n.write(newline)
