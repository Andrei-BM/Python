
# Функция для суммирования введенных чисел. Вариант №1
# def func_sum():
#     print('Вводите числа разделяя их пробелом. Для завершения программы введите "q"')
#     i = True
#     result = 0
#     while i:
#         temp = input('Список чисел: ').upper().split(' ')
#         for n in range(len(temp)):
#             if temp[n] == 'Q':                      # Условие выхода из цикла
#                 i = False
#             if temp[n].isdigit():                   # Просто проверяем являются ли символы цифрами.
#                 result = result + int(temp[n])
#         print(result)

# func_sum()


# Вариант №2
def func_sum1():
    print('Вводите числа разделяя их пробелом. Для завершения программы введите "q"')
    amount = 0
    i = True
    while i:
        temp = input('Список чисел: ').split(' ')
        temp_n = []                           # Здесь мы проверяем дважды на цифры и на содержание букв.
        for el in temp:                       # Цель пропускать для суммирования отрицательные и дробные числа.
            if el.isdigit():
                temp_n.append(int(el))
            elif not el.isalnum():
                temp_n.append(float(el))
            if el == 'q' or el == 'Q':
                i = False
        print(f'Сумма введенных чисел: {round(sum(temp_n), 2)}')
        amount = round(amount + sum(temp_n), 2)
        print('Общая сумма: ', amount)

func_sum1()

