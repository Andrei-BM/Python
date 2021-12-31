# Функция выполняющая деление x на y

def func_divide(x, y):

    try:
        x = int(x)
        y = int(y)
        result = x / y
    except (ZeroDivisionError, ValueError) as f:
        print(f)
    else:
        return print(f'Результат деления: {result:.2}')
    finally:
        print('Конец')

func_divide(input('x: '), input('y: '))