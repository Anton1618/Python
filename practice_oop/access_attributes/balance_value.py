'''Класс Balance предоставляет информацию о валюте и остатке средств на счете.

Объект класса представляет сведения о состоянии счета:
 - поддерживает str и repr отображения
 - поддерживает суммирование, вычитание и сравнения с числовым значением, а также значением другого счета

Атрибуты:
- currency - атрибут, представляющий буквенную аббревиатуру типа валюты. Включает валидатор переданного значения:
    Значение должно быть строкой, иначе возбуждается исключение TypeError
    Значение должно состоять из трех букв, иначе возбуждается исключение ValueError
    Буквенное значение должно быть в верхнем регистре, иначе возбуждается исключение NameError
- balance - атрибут, предоставляющий состояние баланса. Включает валидатор переданного значения:
    Значение должно быть целым или вещественным числом, иначе возбуждается исключение ValueError
'''


class Balance:
    def __init__(self, balance=0, currency='USD'):
        self.currency = currency
        self.balance = balance
    def __repr__(self):
        return f'Balance{id(self)%1000}'
    def __str__(self):
        return f'Баланс {repr(self)} составляет {int(self.balance)} целых {round(self.balance % 1 * 100)} сотых {self.currency}'
    @property
    def currency(self):
        return self._currency
    @currency.setter
    def currency(self, value):
        if not isinstance(value, str):
            raise TypeError('Тип валюты должен быть строкой')
        if len(value) != 3:
            raise ValueError('Должно быть ровно три символа аббревиатуры валюты')
        if not value.isupper():
            raise NameError('Аббревиатура валюты должна быть указана в верхнем регистре')
        self._currency = value
    @currency.deleter
    def currency(self):
        raise ValueError('Атрибут нельзя удалять')

    @staticmethod
    def __validate_balance_type(value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError('Значение должно быть числом')
        return True

    def __validate_currency_type(self, other):
        if self.currency != other.currency:
            raise TypeError('Нельзя производить операции на счетах разных валют')
        return True

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if self.__validate_balance_type(value) and value >= 0:
            self._balance = value
    @balance.deleter
    def balance(self):
        raise ValueError('Атрибут нельзя удалять')

    def __add__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            self._balance += other._balance
        else:
            self.__validate_balance_type(other)
            self._balance += other
        print(f'Пополнение баланса на сумму {other}')

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            if self._balance - other._balance < 0:
                raise ValueError('Недостаточно средств на счете')
            self._balance -= other._balance
        else:
            self.__validate_balance_type(other)
            if self._balance - other < 0:
                raise ValueError('Недостаточно средств на счете')
            self._balance -= other
        print(f'Списание с баланса {other}')
    def __bool__(self):
        return True if bool(self.balance) >= 0 else False
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            return self._balance == other._balance
        self.__validate_balance_type(other)
        return self.balance == other
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            return self._balance != other._balance
        self.__validate_balance_type(other)
        return self.balance != other
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            return self._balance > other._balance
        self.__validate_balance_type(other)
        return self.balance > other
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            return self._balance < other._balance
        self.__validate_balance_type(other)
        return self.balance < other
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            return self._balance > other._balance or self._balance == other._balance
        self.__validate_balance_type(other)
        return self.balance > other or self.balance == other
    def __le__(self, other):
        if isinstance(other, self.__class__):
            self.__validate_currency_type(other)
            return self._balance < other._balance or self._balance == other._balance
        self.__validate_balance_type(other)
        return self.balance < other or self.balance == other


if __name__ == '__main__':
    print(' Попытки инициализации счета, нарушающего условия '.center(80, '-'))
    # w2 = Balance('50', 'USD')  # ValueError: Значение должно быть положительным числом
    # w2 = Balance(50, 'usd')  # NameError: Аббревиатура валюты должна быть указана в верхнем регистре
    # w2 = Balance(50, 'abracadabra')  # ValueError: Должно быть ровно три символа аббревиатуры валюты
    # w2 = Balance(50, 1234)  # TypeError: Тип валюты должен быть строкой
    print()

    print(' Корректная инициализация счетов '.center(80, '-'))
    print('Инициализация пустого счета')
    w1 = Balance()
    print(w1)
    print()

    print('Инициализация счета 50 USD')
    w2 = Balance(50, 'USD')
    print(w2)
    print()

    print(f' Операции со счетом {repr(w2)} '.center(80, '-'))
    w2 + 1350.85
    w2 - 0.55
    w2 - 3.60
    # w2 - 10_000  # ValueError: Недостаточно средств на счете
    print(w2)
    print()

    print(f' Сравнение счетов {repr(w1)}={w1.balance} и {repr(w2)}={w2.balance} '.center(80, '-'))
    # w3 = Balance(currency='AMD')
    # print(w2 > w3)  # TypeError: Нельзя производить операции на счетах разных валют
    assert True == (w2 > w1)
    assert False == (w2 < w1)
    assert True == (w2 >= w1)
    assert False == (w2 <= w1)
    assert False == (w2 == w1)
    assert True == (w2 != w1)
    print('Тесты пройдены')
    print()

    print(f' Сравнение счета {repr(w2)} с числовым значением 0, аналогично {repr(w1)} '.center(80, '-'))
    # print(w2 > 'abracadabra')  # TypeError: Значение должно быть числом
    assert True == (w2 > 0)
    assert False == (w2 < 0)
    assert True == (w2 >= 0)
    assert False == (w2 <= 0)
    assert False == (w2 == 0)
    assert True == (w2 != 0)
    print('Тесты пройдены')
    print()
