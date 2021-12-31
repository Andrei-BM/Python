# Функция возвращающая сумму двух наибольших аргументов.

# В первом варианте находим наибольшую сумму из 3х возможных сочетаний.
def my_func(x, y, z):
    list_summ = [(x + y), (y + z), (x + z)]
    return print(max(list_summ))
my_func(10,11,10.5)

# Второй вариант
# Здесь "выкидываем" из списка наименьшее число и выводим сумму оставшихся.
def my_func(x, y, z):
    list_d = [x, y, z]
    a = min(list_d)
    a_index = list_d.index(a)
    list_d.pop(a_index)
    return print(list_d[0] + list_d[1])

my_func(1, 10, -10)