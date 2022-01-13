# Формируем список факториалов числа от 1 до введенного.
from math import factorial


def fact_gen(n):
    yield from (factorial(i) for i in range(1, n + 1)) # Используем функцию из модуля 'math'


n = input('Число? ')
try:
    n = abs(int(n))
except (TypeError, ValueError):
    print('Неверный ввод!')
else:
    for el in fact_gen(n): print(el, end=' ')


# 2-й вариант Получаем значения используя операции внутри цикла.
def fact_fun(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


for el in fact_fun(6): print(el, end=' ')
