print('Введите строку, разделяйте элементы пробелами.')
list01 = input("Вводите:") # Запрашиваем строку.
list_new = list01.split(' ') # Разделяем строку на элементы.
n = 1 # Вводим переменную для нумерации.
for unit in list_new:
    print(f'{n}. {unit.title()[:11]}') # Индексом ограничиваем длину в 10 символов.
    n +=1