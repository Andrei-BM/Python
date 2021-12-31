# Пользователь вводит строку - вывод строки где каждое слово с заглавной буквы.
def int_func(sample):
    if sample.isascii() and sample.isalpha():
        print(sample.capitalize())
    else:
        print('Просили только латинские символы!')
int_func(input('Enter a word: '))

# 2ой вариант без использования функций строки
# Создаем функцию для проверки слова
def check_func(x):
    check_list = [33, 44, 46, 58, 59, 63] # Список символов пунктуации
    for i in x:
        code = ord(i)                         # Переводим символы в цифры кодировки
        if code in range(97, 123) or code in check_list: # Проверяем есть ли в слове хоть один неверный символ.
            pass
        else:
            x = None                                     # Если есть возвращаем None и прерываем цикл.
            break
    return x
# Сама функция для изменения букв в словах фразы.
def int_func():
    sample = input('Введите фразу: ').split(' ') # Запрашиваем фразу и переводим ее в строку.
    for unit in sample:
        unit = check_func(unit)                   # Проверяем слова нашей встроенной функцией, если соответствует - печатаем.
        print(unit.capitalize(), end=' ') if unit else ''
int_func()











