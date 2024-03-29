'''Реализация методов сравнения.

__eq__(self, other)		==	(equals) Равенство
__ne__(self, other)		!=	(not equal) Неравенство
__lt__(self, other)		<	(less than) Меньше
__gt__(self, other)		>	(greatest than) Больше
__le__(self, other)		<=	(less or equal) Меньше или равно
__ge__(self, other)		>=	(greatest or equal) Больше или равно

Интерпретатор автоматически вызывает противоположные операции при сравнении,
поэтому, минимально возможное переопределение методов включает в себя определение:
равно __eq__, больше __gt__ и меньше или равно __le__ на их основе

Метод равно __eq__ автоматически реализует обратный ему метод - неравенство __ne__.
А метод больше __gt__ автоматически реализует обратный ему метод - меньше __lt__
В последующем, их комбинация позволяет в упрощенном виде реализовать метод меньше или равно __le__,
который в свою очередь автоматически реализует обратную ему реализацию - больше или равно __ge__
'''


class Rectangle:
    '''Класс реализует получение площади прямоугольника.
    Реализованы методы сравнения с другими объектами данного класса,
    что позволяет осуществлять сравнение площадей этих прямоугольников'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        '''Проверка на равенство, также автоматически реализует обратную проверку на неравенство'''
        print('__eq__ call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        '''Проверка на меньше, также автоматически реализует обратную проверку на больше'''
        print('__lt__ call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        if isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        '''Проверка на меньше или равно, также автоматически реализует обратную проверку на больше или равно'''
        return self < other or self == other


if __name__ == '__main__':
    r1 = Rectangle(4, 6)
    r2 = Rectangle(2, 3)
    r3 = Rectangle(2, 3)
    print('Строгое сравнение разных прямоугольников')
    'Вызывает __lt__ call'
    print(r1 < r2)  # False
    print()
    'Также вызывает __lt__ call'
    print(r1 > r2)  # True
    print()

    print('Нестрогое сравнение разных прямоугольников')
    'Вызывает __lt__ call и __eq__ call'
    print(r1 <= r2)  # False
    print()
    'Вызывает только __lt__ call'
    print(r1 >= r2)  # True
    print()

    print('Сравнение на равенство разных прямоугольников и одинаковых прямоугольников')
    'Вызывает __eq__ call'
    print(r1 == r2)  # False
    print()
    'Вызывает __eq__ call'
    print(r2 == r3)  # True
    print()

    print('Сравнение на НЕравенство разных прямоугольников и одинаковых прямоугольников')
    'Вызывает __eq__ call'
    print(r1 != r2)  # True
    print()
    'Вызывает __eq__ call'
    print(r2 != r3)  # False
    print()