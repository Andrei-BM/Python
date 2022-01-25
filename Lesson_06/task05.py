# Создаём родительский класс и подклассы со своими методами.
class Stationery:
    def __init__(self, name):
        self.name = name

    def draw(self):
        return print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        return print(f"Это запуск отрисовки класса 'Pen'. Объект - {self.name}")


class Pencil(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        return print(f"Это запуск отрисовки класса 'Pencil'. Объект - {self.name}")


class Handle(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        return print(f"Это запуск отрисовки класса 'Handle'. Объект - {self.name}")


a = Pen('Ручка')
a.draw()
b = Pencil('Карандаш')
b.draw()
c = Handle('Маркер')
c.draw()
