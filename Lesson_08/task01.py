''' Вводим в модуль дату в формате строки, в первом методе проверяем данные и создаём объект класса. Во втором методе
проверяем данные на '''


class Date:

    def __init__(self, dd, mm, year):
        self.day = dd
        self.month = mm
        self.year = year
        print(self)

    @classmethod
    def first_method(cls, date):
        try:
            list_method = [int(el) for el in date.split('-')]
        except ValueError:
            print('Данные не в числовом формате!')
        else:
            dd, mm, year = list_method
            if 0 < dd <= 31 and 0 < mm <= 12 and 1900 < year <= 2022:
                return cls(dd, mm, year)
            else:
                return print('Введены неккоректные данные.')

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


a = Date.first_method('25-01-2022')


