# Подсчитываем сумму чисел в выбранном файле.
with open('Digits.txt', 'r') as f:
    content = f.read() # Считываем сразу все данные.
    result = sum([int(i) for i in content.split() if i.isdigit()]) # Разбиваем строку и суммируем данные.

print(f'Сумма чисел: {result}')
