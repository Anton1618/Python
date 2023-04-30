'''Класс Wallet реализует присвоение значений атрибутам долларов и центов в кошельке пользователя

Атрибут total_cents:
- Свойство геттер dollars возвращает количество имеющихся долларов в результате деления нацело на 1 (количество
долларов, как целая часть, составляющая каждые 100 центов)
Например, 101.99 // 1 = 101
- Свойство геттер cents возвращает количество имеющихся центов в результате деления по остатку на 100 (количество
центов в долларе, как вещественная часть, составляющая остаток от целой части)
 Например, 101.99 % 1 = 0.99
- Свойство сеттер dollars принимает положительное целое или вещественное число - количество долларов.
Присваивает полученное значение в атрибут dollars,
при этом изменяя только значение долларов, при этом не изменяя значение центов
- Свойство сеттер cents аналогично, принимает положительно целое или вещественное число - количество центов.
Присваивает полученное значение в атрибут cents, при этом не изменяя значение долларов
'''


class Wallet:
    def __init__(self, money=None):
        if money is None:
            self.dollars = 0
            self.cents = 0
        if self.__validate(money):
            self.dollars = money
            self.cents = money

    def __str__(self):
        return f'Ваш баланс составляет: {self.dollars} долларов {self.cents} центов'
    def __validate(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
            raise ValueError('Значение должно быть положительным числом')
        return True
    @property
    def dollars(self):
        return self._dollars
    @dollars.setter
    def dollars(self, money):
        if self.__validate(money):
            self._dollars = money // 1
    @property
    def cents(self):
        return self._cents
    @cents.setter
    def cents(self, money):
        if self.__validate(money):
            self._cents = round(money % 1, 2)


if __name__ == '__main__':
    print(' Класс Wallet с установкой значений для атрибутов '.center(120, '-'))
    print('Инициализация кошелька с заданным количеством долларов и центов')
    client1 = Wallet(20.8)
    print(client1)
    print()

    print('Присвоение значения центов - 0.20')
    client1.cents = 0.20
    print(client1)
    print()

    print('Присвоение значения долларов - 79.0')
    client1.dollars = 79.0
    print(client1)
    print()
