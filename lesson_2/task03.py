# Определяем время года по введеному месяцу.
#Создаем словарь времен года и список для проверки ввода
dict_month = {1:'зима', 2:'весна', 3:'лето', 4:'осень'}
list_month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# Запрашиваем месяц и проверяем ввод
m = False
while m != True:
    month = input('Какой сейчас месяц? (Цифра от 1 до 12)')
    m = True if month in list_month else print('Неверный ввод, попробуйте еще раз!')

# Определяем какое значение словаря выбрать.
month = int(month)
if month == 1 or month == 2 or month == 12:
    print(f'Время года: {dict_month[1]}.')
elif 3 <= month <= 5:
    print(f'Время года: {dict_month[2]}.')
elif 6 <= month <= 8:
    print(f'Время года: {dict_month[3]}.')
else:
    print(f'Время года: {dict_month[4]}.')
