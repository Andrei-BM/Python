# Из файла содержащего список сотрудников с зарплатой:
# - создаём словарь содержий сотрудников с з\п менее 20 000;
# - рассчитываем среднюю зарплату всех сотрудников. Для подсчета используем функцию mean из модуля statistics

from statistics import mean

dict_e = {}

with open('Employees.txt', 'r', encoding='utf-8') as f:
    while True:
        content = f.readline()
        if not content:
            break
        else:
            item = content.split()
            dict_e[item[0]] = item[1] # Так как мы знаем, в каком порядке записаны данные, просто создаём словарь всех сотрудников.
dict_small = {k: v for k, v in dict_e.items() if int(v) < 20000} # Создаём словарь содержащий список сотрудников с заданным условием.
list_s = [int(v) for v in dict_e.values()] # Создаём список с зарплатой.
print(f'Средняя зарплата: {mean(list_s):.2f}')
print('Сотрудники с зарплатой менее 20 000:')
for k, v in dict_small.items():
    print(f'{k} - {v}')
