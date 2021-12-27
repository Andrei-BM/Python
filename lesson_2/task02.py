# Смена значений элементов.
print('Введите элементы списка.')
iteration = int(input('Количество элементов в списке: '))
list01 = []
while iteration: #Запращиваем элементы списка.
    item = input()
    list01.append(item)
    iteration -= 1
n = 0 # для определения индекса вводим переменную.
print(f'Вы ввели: {list01}')
for unit in list01[1::2]: #Перебираем нечетные элементы.
    list01[n + 1], list01[n] = list01[n], list01[n+1]
    n += 2
print(f'Результат: {list01}')
