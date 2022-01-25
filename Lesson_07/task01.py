''' Создаём класс "Матрица" '''


class Matrix:

    def __init__(self, list_m): # В методе кроме матрицы добавляем аттрибуты количество строк и символов в строке.
        self.list = list_m
        self.st = len(self.list)
        self.el = len(self.list[0])

    def __str__(self): # Формируем вывод через генератор.
        out = ''.join(['|' + ''.join([f'{el:3}  ' if n != (len(line)-1) else f'{el:3}|\n' for n, el
         in enumerate(line)]) for line in self.list])
        return out

    def __add__(self, other):
        self.L1 = self.list.copy()
        self.M1 = other.list.copy()
        self.strok = max(self.st, other.st)
        self.element = max(self.el, other.el)
        if self.st == other.st and self.el == other.el:
            # Вариант если принимать только равные матрицы.
            S = [[self.L1[l][r] + self.M1[l][r] for r in range(self.el)] for l in range(self.st)]
            return Matrix(S)

        else:
            ''' В таком варианте мы также используем вложенные циклы из количества строк и символов в строке,
                    но перед этим уравниваем матрицы добавляя сначала пустые строки, а потом заполняя их 0-ми.'''
            a = input('Матрицы не равны: всё равно сложить? Введите (Y/N): ')
            if a.lower() == 'y':
                while True:
                    if len(self.L1) == self.strok == len(self.M1):
                        break
                    elif len(self.L1) < self.strok:
                        self.L1.append([])
                    else:
                        self.M1.append([])

                S = []
                for l in range(self.strok):
                    T = []
                    while True:
                        if len(self.L1[l]) == self.element == len(self.M1[l]):
                            break
                        elif len(self.L1[l]) < self.element:
                            self.L1[l].append(0)
                        else:
                            self.M1[l].append(0)
                    T = [(self.L1[l][r] + self.M1[l][r]) for r in range(self.element)]
                    S.append(T)
                return Matrix(S)
            else:
                return None


L = [[31, 22], [37, 43], [51, 86]]
M = [[5, 5, 5, 5], [0, 1, 0, 0]]
N = [[11, 12], [17, 13], [11, 56]]
K = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
a = Matrix(L)
b = Matrix(M)
n = Matrix(N)
k = Matrix(K)
print(a)
print(k)
print(a + n)
c = b + k
print(c)
