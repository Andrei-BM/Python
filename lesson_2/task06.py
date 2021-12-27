# Ввод данных
sample = []
n = int(input('Сколько позиций: '))
i = 1
while i <= n: # Делаем цикл по количеству позиций
    dict_sample = {'название':'', 'цена':'', 'количество':'', 'ед.':''} # Формируем словарь и заполняем значения
    dict_sample['название'] = input('Название: ')
    dict_sample['цена'] = input('Цена: ')
    dict_sample['количество'] = input('Количество: ')
    dict_sample['ед.'] = input('Единицы измерения: ')
    tuple_sample = (i, dict_sample) # Формируем кортеж
    sample.append(tuple_sample) # Формируем итоговый список.
    i += 1
for unit in sample:
    print(unit)
# Формирование аналитики.
dict_sum = sample[0][1] # Создаем словарь аналитики
for k in dict_sum.keys(): # Заполняем значения
    box = []
    i = 0
    first = False
    for i in range(n): # создавая временный словарь из общего списка.
        dict_temp = sample[i][1]
        value = dict_temp.setdefault(k)
        if first == True and box[0] == value:
            continue
        box.append(value)
        first = True
    dict_sum[k] = box
    print(f'{k:11} {dict_sum[k]}')



