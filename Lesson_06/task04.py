# Создаём родительский класс "Car" и подклассы.
from random import randint, choice


class Car:
    dict_direction = {'1': 'направо', '2': 'налево'}

    def __init__(self, name, color, isPolice=False):
        self.name = name
        self.color = color
        self.isPolice = bool(isPolice)
        self.speed = randint(0, 120) # Данный аттрибут к моему удивлению наследуется без прописывания.

    def go(self):
        return print(f'Автомобиль {self.name} цвет {self.color} начал движение.')

    def stop(self):
        return print(f'Автомобиль {self.name} цвет {self.color} остановился.')

    def turn(self):
        i_choice = choice('123')
        return print(
            f'Автомобиль {self.name} повернул {self.dict_direction[i_choice]}') if i_choice == '1' or i_choice == '2' else print(
            f'Автомобиль {self.name} развернулся')

    def show_speed(self):
        show_text = f'Автомобиль {self.name} движется со скоростью: {self.speed}км/ч.'
        return print(show_text)


class TownCar(Car):
    def __init__(self, name, color, isPolice=False):
        super().__init__(name, color, isPolice)

    def show_speed(self): # За основу взята функция родительского класса, к ней добавляем только сравнение.
        super().show_speed()
        if self.speed > 60:
            fol = self.speed - 60
            return print(f'Внимание, превышение скорости на {fol}км/ч!')


class WorkCar(Car):
    def __init__(self, name, color, isPolice=False):
        super().__init__(name, color, isPolice)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            fol = self.speed - 40
            return print(f'Внимание, превышение скорости на {fol}км/ч!')


class PoliceCar(Car):
    def __init__(self, name, color, isPolice=True):
        super().__init__(name, color, isPolice)


b = TownCar('Nissan', 'красный')
c = WorkCar('Man', 'белый')
d = PoliceCar('Mercedes', 'белый')
b.go()
d.go()
b.turn()
d.turn()
c.go()
b.turn()
c.turn()
b.show_speed()
print(b.name, 'Это полицейская машина?', b.isPolice)
b.turn()
d.show_speed()
print(d.name, "Это полицийская машина?", d.isPolice)
c.show_speed()
c.turn()
b.stop()
c.stop()
