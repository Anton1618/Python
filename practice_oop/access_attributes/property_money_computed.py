'''Класс Money преобразующий аргументы долларов и центов в общее количество центов, атрибут - total_cents
- Свойство геттер dollars возвращает количество имеющихся долларов в результате деления нацело на 100 (целое количество доллраров из 100 центов)
 Например, 101.99//100 = 101
- Свойство геттер cents возвращает количество имеющихся центов в результате деления по остатку на 100 (количество центов в долларе)
 Например, 101.99%100 = 99
- Свойство сеттер dollars принимает целое положительное число - количество долларов.
Прибавляет полученное значение в атрибут total_cents,
при этом изменяя только значение долларов и не изменяя значение центов
- Свойство сеттер cents аналогично, принимает целое положительно число и прибавляет значение в total_cents,
при этом не изменяя значение долларов
'''


class Money:
    def __init__(self, dollars, cents):
        '''Общая сумма центов состоит из долларов умноженных на 100 и суммированных центов'''
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        '''Значение долларов как целочисленное деление общей суммы центов'''
        return self.total_cents // 100

    @property
    def cents(self):
        '''Значение центов как остаток от деления на целый доллар из общей суммы центов'''
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, value):
        '''
        Изменение значения долларов
        Проверка включает в себя соответствие целому положительному числу
        Новое значение состоит из:
        - Полученного значения долларов, которое умножается на 100 для представления суммой центов.
        - Прибавления текущего значения центов из геттера центов.
        '''
        if isinstance(value, int) and value >= 0:
            self.total_cents += value*100 + self.cents
        else:
            raise ValueError('Значение должно быть целым положительным числом')

    @cents.setter
    def cents(self, value):
        '''
        Изменение значения центов (аналогично сеттеру доллара)
        Проверка включает в себя соответствие целому числу от 0 до 100
        Новое значение состоит из:
        - Текущего значения долларов из геттера долларов, которое умножается на 100 для представления суммой центов.
        - Полученного значения центов, которое прибавляется.
        '''
        if isinstance(value, int) and value >= 0:
            if value > 100:
                self.total_cents += (self.dollars * 100) + (value // 100 * 100) + (value % 100)
            else:
                self.total_cents += self.dollars * 100 + value
        else:
            raise ValueError('Значение должно быть целым положительным числом')

    def __str__(self):
        return f'Ваш баланс составляет: {self.dollars} долларов {self.cents} центов'


if __name__ == '__main__':
    client1 = Money(10, 80)
    print(client1)
    client1.cents = 20
    print(client1)
    client1.dollars = 79
    print(client1)


