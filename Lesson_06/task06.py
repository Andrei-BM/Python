from random import randint

with open('Digits.txt', 'a', encoding='utf-8')as f:
    for _ in range(10):
        f.write(' '.join([str(randint(0, 1000)) for _ in range(30)]))
# Подсчитываем сумму чисел в выбранном файле.
with open('Digits.txt', 'r') as f:
    content = f.read()  # Считываем сразу все данные.
    result = sum([int(i) for i in content.split() if i.isdigit()])  # Разбиваем строку и суммируем данные.

print(f'Сумма чисел: {result}')
