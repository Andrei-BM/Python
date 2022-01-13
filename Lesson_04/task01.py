# Функция расчета заработной платы. Работает в командной строке. Проверка на ввод количества элементов и их тип.
from sys import argv
try:
    name, h, rate, bonus = argv
except ValueError:
    print('Требуется ввести 3 показателя: количество часов, ставка и премия')
else:
    def func_salary(h, rate, bonus):
        try:
            print(f'Количество часов: {h}, ставка: {rate}, премия: {bonus}')
            h, rate, bonus = int(h), int(rate), int(bonus)
        except ValueError:
            print('Введены неверные данные.')
        else:
            return print('Итого = ', (h * rate) + bonus) if h >= 0 and rate >= 0 else print('Введены неверные данные.')


    func_salary(argv[1], argv[2], argv[3])
