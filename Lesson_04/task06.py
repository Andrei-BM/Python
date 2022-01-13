# Используем функции count и cycle. Первая - внешний цикл из цифр. Вторая, внутренняя - перебирает слова из фразы.
from itertools import count, cycle
phrase = 'Ave Imperator, morituri te salutant'.split()
for item in count(1):
    if item > 4:
        break
    else:
        print('\n', item, end='.')
        for n, el in enumerate(cycle(phrase)):
            if n >= len(phrase):
                break
            else:
                print(el, end=' ')

