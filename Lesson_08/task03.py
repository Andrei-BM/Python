# Допускаем в ввод списка только числа. Программа прекращается при вводе слова 'all'
''' По условию задачи требовалось допускать дробные и отрицательные числа. Вместо собственной проверки используется
встроенная проверка с обработкой встроенных исключений.'''


class MyError(Exception):
    def __int__(self, text):
        self.text = text


class Int(int):
    @staticmethod
    def check_int(el):
        try:
            type(int(el)) is int
        except ValueError:
            return False
        else:
            your_list.append(int(el))
            return True


class Float(float):
    @staticmethod
    def check_float(el):
        try:
            type(float(el)) is float
        except ValueError:
            return False
        else:
            your_list.append(float(el))
            return True


''' Для проверки были созданны классы Int и Float, вводимое число отправляется на сначала на проверку через метода
класса Int, при отрицательно результате на проверку в класс Float. Если обе проверки неудачны - вызываем собственное
исключение.'''
your_list = []
print('Вводите числа, для окончания ввода введите слово "all"')
while True:
    el = input()
    if el.lower() == 'all':
        break
    else:
        try:
            if Int.check_int(el) or Float.check_float(el): pass
            else:
                raise MyError('Ввод в таком формате недопустим!')
        except MyError as me:
            print('\033[31m', me)
        else:
            print("\033[0mЧисло добавлено.")
        finally:
            pass

print(your_list)

