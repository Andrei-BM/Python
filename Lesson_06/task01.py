# Программа светофор:
from time import sleep, monotonic
from termcolor import cprint


class TrafficLight:
    __color = ('красный', "желтый", "зелёный")
    # Для запуска используем 4 переменных, данные в сек.: r - время красного сигнала, '
    # 'y - время желтого сигнала, g - время зелёного сигнала светофора, t - время работы по умолчанию (20)')

    def __init__(self):
        self.color = TrafficLight.__color[:]

    def running(self, r, y, g, t=20):
        start = monotonic()
        on_off = ('Светофор включен:', 'Светофор выключен:')
        list_sign = [('*' * 164) for _ in range(10)]
        while monotonic() - start < t: # Создаём цикл для работы в установленное время.
            if self.color[0] == 'красный': # Задаём проверку на правильный сигнал.
                print(f'\r{on_off[0]} Горит {self.color[0].upper()} цвет. Движение запрещено!', end=' ')
                cprint(f'{list_sign}', 'red', 'on_red', end='')
                sleep(r)

            if self.color[1] == 'желтый':
                print(f'\r{on_off[0]} Горит {self.color[1].upper()} цвет.', end=' ')
                cprint(f'{list_sign}', 'yellow', 'on_yellow', end='')
                sleep(y)

            if self.color[2] == 'зелёный':
                print(f'\r{on_off[0]} Горит {self.color[2].upper()} цвет. Движение разрешено!', end=' ')
                cprint(f'{list_sign}', 'green', 'on_green', end='')
                sleep(g)

            else:
                print(f'\r{on_off[1]} ОШИБКА! {list_sign}', end=' ')
                break
        print(f'\r{on_off[1]}', end=' ')
        cprint(f'{list_sign}', end='')


tl = TrafficLight()
tl.running(7, 2, 7)
