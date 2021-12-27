list_rate = [2, 2, 2, 1, 1]

while True: # Делаем цикл для работы с рейтингом.
    print(f'Текущий рейтинг: {list_rate}')
    new_unit = input('Введите новую цифру рейтинга: (n - для отмены ввода)')
    new_unit = new_unit.lower()
    n, position = 0, 0

    if new_unit == 'n': # Проверяем условие прекращения цикла.
        break
    new_unit = int(new_unit) # Приводим ввод к числу.
    for unit in list_rate: # В цикле ищем есть ли совпадения, если да то каков индекс последнего совпадающего элемента.
        if unit > new_unit or unit == new_unit:
            position = n + 1
        n += 1
    list_rate.insert(position, new_unit) # Вставлем введенный элемент в список, под нужным индексом.
