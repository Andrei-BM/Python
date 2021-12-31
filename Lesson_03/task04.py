# Возводим число x в степень y
def func_rate1(x, y):
    return print(x ** y)
func_rate1(0.5,-3)
# Во втором варианте мы просто перемножаем число в цикле равном степени, далее 1 делим на число.
def func_rate2(x,y):
    y = abs(y)
    c = x
    while y > 1:
        x *= c
        y -= 1
    return print(1/x)

func_rate2(int(input('x: ')), int(input('y: ')))
