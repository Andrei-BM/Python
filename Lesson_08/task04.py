''' Программа "Хранилище" создаём активы, помещаем в хранилище. Создаём методы для списания активов из хранилища в другие
подразделения.'''


class Vault:
    vault_dict = {'Money': [], 'Shares': [], 'Bonds': [], 'Options': []} # Для хранения данных используем словарь.
    total_dict = {'Money': 0, 'Shares': 0, 'Bonds': 0, 'Options': 0} # Это словарь статистики он заполняется автоматически.

    ''' Этот метод отображает текущее состояние хранилища. Сначала формирую словарь статистики, затем осущесвляя вывод
    одновременно используя оба словоря.'''
    @staticmethod
    def get_info():
        for k, v in Vault.total_dict.items():
            Vault.total_dict[k] = sum([value['quantity'] * value['price'] for value in Vault.vault_dict[k]])
        out = ''.join([f'{k} : {v}\n' + ''.join([f'{value}\n' for value in Vault.vault_dict[k]]) for k, v in Vault.total_dict.items()])
        return print(out)

    ''' Метод send списывает активы из класса Vault(Хранилище) принимает 3 параметра объект списания, количество, назначение
        При работе метода осуществляется проверка параметра qty на формат, а также соотвествия его количеству актива в хранилище. '''
    @staticmethod
    def send(obj, qty, dst):
        if type(qty) is int and qty > 0:
            stat = obj.stat.copy()
            for value in Vault.vault_dict[obj.key]:
                if value['name'] == obj.name and value['quantity'] >= qty:
                    value['quantity'] = value['quantity'] - qty
                    stat['quantity'] = qty
                    dst.vault_dict[obj.key].append(stat)
                elif value['name'] == obj.name and value['quantity'] < qty:
                    print(f'Такое количество в хранилище отсутствует! В наличии: {value["quantity"]}')
                    break
        else:
            print(f'Невозможно выполнить операцию: класс - {obj.key}, объект - {obj.name}, количество - {qty}!')


''' Активы представляют собой объкты созданные в своих классах, родительским классом которых является Assets.
Классы наследники используют метод родительского класса 'send_in' для перемещения созданных объектов в хранилище.
Для создания объектов используются данные в формате строки.'''


class Assets:
    param_list = []

    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    @staticmethod
    def send_in(self):
        if self.stat:
            Vault.vault_dict[self.key].append(self.stat)
        else:
            pass

    @staticmethod
    def make_list(info):
        try:
            Assets.param_list = [el if el.isalpha() else float(el) for el in info.split()]
        except ValueError as err:
            print(err)
        else:
            return Assets.param_list


class Money(Assets):
    ''' Экземпляры каждого класса создаются используя метод make_unit, не увидел возможности сделать этот метод общим
    для всех наследуемых классов, т.к. разные классы имеют разное количество аттрибутов класса. Поэтому общим является
    часть метода - создание списка параметров. Сразу в блоке инициализации запускается метод отправляющий актив в
    хранилище.'''
    def __init__(self, name, qty):
        super().__init__(name, qty, price=None)
        self.total = qty
        self.stat = {self.name: self.qty}
        self.key = 'Money'
        self.send_in(self)

    @classmethod
    def make_unit(cls, info):
        cls.make_list(info)
        n, q = Assets.param_list
        return cls(n, q)


class Shares(Assets):
    def __init__(self, name, qty, price, dividends):
        super().__init__(name, qty, price)
        self.dividends = dividends
        self.stat = {'name': self.name, 'quantity': self.qty, 'price': self.price, 'dividends': self.dividends}
        self.key = 'Shares'
        self.send_in(self)

    @classmethod
    def make_unit(cls, info):
        cls.make_list(info)
        if Assets.param_list and len(Assets.param_list) == 4:
            n, q, v, d = Assets.param_list
            return cls(n, q, v, d)
        else:
            return print("Создание объекта невозможно.")


class Bonds(Assets):
    def __init__(self, name, qty, price, dividends, term):
        super().__init__(name, qty, price)
        self.dividends = dividends
        self.term = term
        self.key = 'Bonds'
        self.stat = {'name': self.name, 'quantity': self.qty, 'price': self.price, 'dividends': self.dividends,
                     'term': self.term}
        self.send_in(self)

    @classmethod
    def make_unit(cls, info):
        cls.make_list(info)
        n, q, v, d, t = Assets.param_list
        return cls(n, q, v, d, t)


class Options(Assets):
    def __init__(self, name, qty, price, term):
        super().__init__(name, qty, price)
        self.term = term
        self.key = 'Options'
        self.stat = {'name': self.name, 'quantity': self.qty, 'price': self.price, 'term': self.term}
        self.send_in(self)

    @classmethod
    def make_unit(cls, info):
        cls.make_list(info)
        n, q, v, t = Assets.param_list
        return cls(n, q, v, t)


''' Это классы - "Потребители" куда активы перемещаются из "Хранилища".'''


class StockExchange:
    vault_dict = {'Money': [], 'Shares': [], 'Bonds': [], 'Options': []}


class Bank:
    vault_dict = {'Money': [], 'Shares': [], 'Bonds': [], 'Options': []}



# A1 = 'cash 10000'
# A2 = 'deposit 5000'
# A3 = 'margin 7000'
S1 = 'XXX 200 19 0'
S2 = 'YYY 300 15 5'
B1 = 'OFS 300 10 12 180'
B2 = 'RUS 500 8 10 120'
# O1 = 'RTSCall 2 500 90'
# a1 = Money.make_unit(A1)
# a2 = Money.make_unit(A2)
# a3 = Money.make_unit(A3)
s1 = Shares.make_unit(S1)
s2 = Shares.make_unit(S2)
b1 = Bonds.make_unit(B1)
b2 = Bonds.make_unit(B2)
# o1 = Options.make_unit(O1)

Vault.get_info()
Vault.send(s1, 190, StockExchange)
Vault.send(b2, 500, Bank)
Vault.get_info()
print('Items in StockExchange:', StockExchange.vault_dict)
print('Items in Bank:', Bank.vault_dict)

