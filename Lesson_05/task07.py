# Из выбранного файла содержащего список фирм с данными создаем новый файл в формате json по заданным параметрам.
import json

av_prof, D = {}, {}
with open('firms.txt', 'r', encoding='utf-8') as f:
    for line in f:
        L = line.split()
        if len(L) > 1:
            # Исходим из того, что мы знаем в каком порядке записаны данные. Т.к. название может быть из нескольих слов
            # идём с конца списка и создаём словарь - Название : финансовый результат.
            D[str(' '.join(L[:-3])).replace('"', '')] = int(L[-2]) - int(L[-1])  #
profit = [el for el in D.values() if el > 0] # Создаём список если фин. результат прибыль.
av_prof['average_profit'] = round(sum(profit) / len(profit), 1)
with open('firms.json', 'w', encoding='utf-8') as f: # Записываем данные.
    json.dump([D, av_prof], f)

print(D, av_prof)
