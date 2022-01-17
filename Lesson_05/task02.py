# Подсчитываем строки и количество слов в строке, в выбранно файле.
counter, n = {}, 0

with open('test.txt', 'r') as f: # Открываем файл для чтения, считываем его по строкам.
    while True:
        content = f.readline()
        if not content:
            break
        else:
            n += 1
            print(content)
            list_n = content.split() # Разбиваем строку для подсчета слов.

            for i in list_n:
                if i == '-' or i == '=': list_n.remove(i) # Добавляем условие, чтобы не считать тире и двоеточия.
            value = len(list_n)
            counter[n] = value # В список добавляем количество слов в строке по порядку их считывания.

print('Количество строк:', n)
for k, v in counter.items():
    print(f'{k} строка: {v} - слов.')