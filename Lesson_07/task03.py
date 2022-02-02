# Вывод на экран и операции с клетками.
class Cell:
    line = 0

    def __init__(self, qty=1):
        self.qty = abs(qty) # Вводим количество через модуль, т.к. не может быть отрицательно количество клеток.

    ''' Если в результате операций получится отрицательное число. Вывод не производим. За это отвечает первое условие.
    Если линия в методе make_order меньше чем количество клеток идём на вывод через 1 цикл, остатка не остаётся.
    Если линия меньше тогда считаем количество циклов и выводим остаток - если есть.'''

    def __str__(self):
        if self.qty > 0:
            if Cell.line >= self.qty:
                self.line = self.qty
            else:
                self.line = Cell.line
            self.cycle = self.qty // self.line # Определяем количество циклов.
            tail = self.qty - (self.line * self.cycle) # Определяем остаток.
            add = f'{chr(42) * tail}\n' if tail != 0 else ''
            out = ''.join([f'{chr(42) * self.line}\n' for _ in range(self.cycle)]) # Формируем строку для вывода.
            return '\r' + out + add
        else:
            return 'Ничего не осталось для вывода.'

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        return Cell(self.qty - other.qty)

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(self.qty // other.qty)

    @staticmethod
    def make_order(length=100):
        Cell.line = length


a = Cell(10)
b = Cell(20)
Cell.make_order(12)
print(a)
print(b)



