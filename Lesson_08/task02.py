# Создаём собственное исключение.
class MyError(Exception):
    def __init__(self, text):
        self.text = text


print('Производим деление введенных чисел. Введите числа: \n')
a = int(input())
b = int(input())


try:
    if b == 0: # Т.к. встроенное исключение сработает при делении, вызываем собственное до этого.
        raise MyError('Вы хотите разделить на ноль!')
    c = a / b

except MyError as er:
    print(er)
else:
    print('Результат: ', c)
