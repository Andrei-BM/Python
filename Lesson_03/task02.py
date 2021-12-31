# Функция вывода данных анкеты
def person_anket(**kwargs):
    # 1 Вариант.
    for k, v in kwargs.items():
        print(f'{k} - {v}', end=' ')
    # 2 Вариант.
    print(f"\nФамилия - {kwargs['surname']}, Имя - {kwargs['name']},"
          f" Год рождения - {kwargs['year_of_birth']}, Телефон - {kwargs['phone']},"
          f" Эл. почта - {kwargs['email']}, Место жительства - {kwargs['reside']}")

person_anket(name='Alex', surname='Komnin', year_of_birth=1990, reside='Stambul', email='Komnin@box.vi', phone='(123)987-653-21')


