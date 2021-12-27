# Проверка классов элементов, содержащихся в строке.
list_01 = [10, 'word', False, 2.789, None, 'Alex', -15, 0b100, 0o37, 0x1F, True, complex(7, 9), [1, 2, 3, 'start'], {1:'Yes', 2:'No'}, ('one', 'two', 'three'), {'tangerin', 'kiwi', 'mango'}]

for n, item in enumerate(list_01, 1):
    print(f'{n}. {item:} - {type(item)}')
# Конец программы.

