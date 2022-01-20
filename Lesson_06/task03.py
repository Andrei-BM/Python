# Запись работников.
class Worker:
    # Прописываем аттрибуты при создании экземпляра класса.

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(wage=float(input('Размер зарплаты: ')), bonus=float(input('Размер премии: ')))


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return print(self.surname, self.name)

    def get_total_income(self):
        sum_income = self._income['wage'] + self._income['bonus']
        return print(f'Общий доход: {sum_income:.2f} у.е.')


ab = Worker('Andrei', 'Johnson', 'manager')
print(ab.name, ab.surname, ab.position, ab._income)
ac = Position('Alex', 'Comnin', 'manager')
af = Position('Ashley', 'Farrel', 'supervisor')
ac.get_full_name()
ac.get_total_income()
af.get_full_name()
af.get_total_income()
