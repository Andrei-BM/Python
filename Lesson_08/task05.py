class ComplexDigit:
    ''' Создаём собственный класс "Комплексные числа". В метод инициализации передаём два параметра: действительную и
    мнимую часть. Эти параметры получаем из метода set_digit в который передаём данные в виде строки. '''
    def __init__(self, d, i):
        self.digit = d
        self.mnim = i
        self.complex = (d, i)

    @classmethod
    def set_digit(cls, info):
        L = info.split()
        try:
            d = int(L[0])
            s = L[1]

            if s == '-':
                i = int(''.join(s + L[2][:-1] if L[2][:-1] else '1'))
            else:
                i = int(L[2][:-1]) if L[2][:-1] else 1
        except ValueError:
            print("Ошибка ввода.")
        else:
            return cls(d, i)
    ''' В методе сложения последовательно суммируем первый и вторые члены кортежа получая действительную и мнимую часть
     соответственно. '''
    def __add__(self, other):
        first = self.complex
        second = other.complex
        L = tuple(map(sum, zip(first, second)))
        d, i = L
        return ComplexDigit(d, i)
    ''' Для отображения данных перегружаем метод str. Для чего определяем знак мнимой части и создаём его в виде
    отдельного элемента строки. '''
    def __str__(self):
        sign = "+" if self.complex[1] > 0 else '-'
        return f'({self.complex[0]} {sign} {abs(self.complex[1])}i)'
    ''' В методе умножения, для урощения просто записываем данные по формуле перемножения мнимых чисел, также получая
    кортеж из двух частей: действительной и мнимой. '''
    def __mul__(self, other):
        first = self.complex
        second = other.complex
        d, i = ((first[0] * second[0] + (-1 * first[1] * second[1])), (first[0] * second[1] + first[1] * second[0]))
        return ComplexDigit(d, i)


a = ComplexDigit.set_digit('3 + i')
b = ComplexDigit.set_digit('2 - 3i')
print(a.complex, b.complex)
c = a + b
print(c)
print(a * b)
