'''Класс Point имеет методы:
- move_to - устанавливает значения координат x и y;
    Принимает значения координат от -1000 до 1000 по оси x и по оси y и сохраняет их в экземпляре класса
    Применяется для изменения значения координат точек
    Может применяться при инициализации объекта точки
- get_distance - вычисляет и возвращает расстояние между точками по теореме Пифагора
    Обязательно принимает экземпляр класса Point;
    Если в метод передается НЕ экземпляр класса Poin, то возбуждается исключение с текстом
Имеет необязательные атрибуты:
- FIELDS - список доступных атрибутов для применения
- list_points - список созданных точек
'''

class Point:
    FIELDS = ('x', 'y') # Доступные атрибуты объекта
    list_points = [] # Список для сохранения созданных координат точек
    def __init__(self, x=0, y=0, save=False):
        '''Инициализация с применением метода перемещения точки, но со значениями по умолчанию'''
        self.move_to(x, y)
        if save: # Необязательная возможность сохранения созданных точек
            self.list_points.append((x, y))

    def move_to(self, x, y):
        '''Установка значений координат для точки'''
        self.x = x
        self.y = y

    def get_distance(self, point2):
        '''Вычисление расстояния между точками по теореме Пифагора
        c**2 = a**2 + b**2 --> с = ((y2 - y1)**2 + (x2 - x1)**2)0.5'''
        if not isinstance(point2, Point): # Или point2.__class__.__name__ != 'Point'
            raise ValueError('Аргумент должен объектом класса Point')
        return round(((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2) ** 0.5)

    def __setattr__(self, key, value):
        if key in self.FIELDS and not -1000 < value < 1000:
            raise AttributeError('Точка должна иметь значение от -1000 до 1000')
        self.__dict__[key] = value


if __name__ == '__main__':
    p1 = Point(1, 2, True)
    p2 = Point(4, 6, True)
    print(p1.get_distance(p2))
    p2.move_to(5, 7)
    print(p1.get_distance(p2))
    print(Point.list_points)


