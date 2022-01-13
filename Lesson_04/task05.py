# Выводим произведение четных элементов списка от 100 до 1000
from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


list_origin = [el for el in range(100, 1001, 2)]
print(reduce(my_func, list_origin))
