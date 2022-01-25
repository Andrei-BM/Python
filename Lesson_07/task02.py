from abc import ABC, abstractmethod


class Clothing(ABC):
    __list = []

    @abstractmethod
    def calculation(self, size):
        pass

    @abstractmethod
    @staticmethod
    def total():
        pass


class Suit(Clothing):
    __list = []

    def __init__(self, size):
        self.calculation = size  # У объекта класса будет один аттрибут - количество ткани.

    @property
    def calculation(self):  # Вывод значения атрибута осуществляем с помощью декоратора.
        return self.__calculation

    @calculation.setter  # Устанавливаем аттрибут используюя формулу расчета, также добавляем значение в список класса
    def calculation(self, size):
        self.__calculation = round(2 * size + 0.3, 2)
        Suit.__list.append(self.calculation)
        print(self.calculation)

    @staticmethod
    def total():  # Здесь мы получаем сумму всех значений по классу.
        value = round(sum(Suit.__list), 2)
        return print(f'Общее количество ткани по классу: Костюм - {value}')

    def __add__(self, other):  # Также можно складывать объекты друг с другом.
        self.first = self.calculation
        self.second = other.calculation
        return round((self.first + self.second), 2)


class Coat(Clothing):
    __list = []

    def __init__(self, size):
        self.calculation = size

    @property
    def calculation(self):
        return self.__calculation

    @calculation.setter
    def calculation(self, size):
        self.__calculation = round((size / 6.5 + 0.5), 2)
        Coat.__list.append(self.calculation)
        print(self.calculation)

    @staticmethod
    def total():
        value = round(sum(Coat.__list), 2)
        return print(f'Общее количество ткани по классу: Пальто - {value}')

    def __add__(self, other):
        self.first = self.calculation
        self.second = other.calculation
        return round((self.first + self.second), 2)


a = Suit(48)
b = Coat(390)
print(a + b)
