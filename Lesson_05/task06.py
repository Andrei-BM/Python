# Из выбранного файла выбираем предметы и суммируем общее количество занятий по каждому предмету.
final, name = {}, ''

with open('lessons.txt', 'r', encoding='utf-8') as f:
    for line in f: # Считываем файл построчно.
        for n, i in enumerate(line, 0):
            start = 1 if line.startswith('\ufeff') else 0
            if line[n] == ':' or line[n] == '-':
                name, line = line[start:n], line[n:] # Т.к. мы знаем, что сначала идут предметы то сначала извлекаем их из строки.
                break
        number = 0
        for el in line.split(): # Остаток строки нарезаем.
            D = [i for i in el if i.isdigit()] # Ищем цифры полученных списках.
            if D:
                number += int(''.join(D)) # В этой переменной мы суммируем цифры собранные из списков.
            D.clear()
        final[name] = number # По результам окончания цикла по каждой строке заносим полученные данные в словарь.

print(final, end=' ')
