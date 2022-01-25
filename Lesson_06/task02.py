# Расчёт количества материала для дороги.
class Road:
    # При создании переменной нужно ввести 3 параметра: длина(м), ширина(м), высота(см).
    def __init__(self, lm, wm, hm):
        self._length = lm
        self._width = wm
        self._height = hm

    def calc(self):
        weight = (self._length * self._width * 25 * self._height) / 1000
        return print(f'Создан экземляр со следующими параметрами: длина - {self._length:,}метров,'
              f' ширина - {self._width}метров, толщина покрытия - {self._height}см.\n Масса асфальта: {weight:.1f}т.')


r = Road(100, 5, 5)
r.calc()
p = Road(100000, 5, 5)
p.calc()



