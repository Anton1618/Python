'''Дескриптор Integer применяется для проверки типа значения Point3D

Демонстрируется два принципа написания проекта: с применением дескриптора и без него
'''


class Point3D:
    '''Класс применяет property атрибуты'''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Координата со значениями {self.x}:{self.y}:{self.z}'

    @staticmethod
    def __veryfi_coord(coord):
        if type(coord) != int:
            raise ValueError('Координата должна быть целым числом')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, other):
        self.__veryfi_coord(other)
        self._x = other

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, other):
        self.__veryfi_coord(other)
        self._y = other

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, other):
        self.__veryfi_coord(other)
        self._z = other


class Integer:
    '''Класс проверки на корректность значения, как универсальный интерфейс, применяемый для всех значений атрибутов'''
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)  # аналогично instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f'__set__: {self.name} = {value}')
        self.__veryfi_coord(value)
        setattr(instance, self.name, value)  # аналогично instance.__dict__[self.name] = value

    @staticmethod
    def __veryfi_coord(coord):
        if type(coord) != int:
            raise ValueError('Координата должна быть целым числом')


class ReadIntX:
    '''Non-data дескриптор
    Демонстрирует, что данные дескрипторы имеют тот же приоритет доступа, что и обычные атрибуты класса'''
    def __set_name__(self, owner, name):
        self.name = '_x'
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class NewPoint3D:
    '''Класс в котором определен единый интерфейс проверки значения соответствующими дескрипторами'''
    # Дескрипторы данных
    x = Integer()
    y = Integer()
    z = Integer()
    # Дескриптор не данных класса ReadIntX
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Координата со значениями {self.x}:{self.y}:{self.z}'


if __name__ == '__main__':
    print(' Без применения дескриптора '.center(80, '-'))
    print('Класс применяет громоздкое определение property атрибутов')
    pt1 = Point3D(1, 2, 3)
    print(pt1.__dict__)  # {'_x': 1, '_y': 2, '_z': 3}
    print(pt1)  # Координата со значениями 1:2:3
    # pt2 = Point3D('1', 2, 3)  # ValueError: Координата должна быть целым числом
    print()

    print(' C применением дескриптора '.center(80, '-'))
    print('Класс применяет лаконичное и короткое определение проверки для всех атрибутов')
    pt3 = NewPoint3D(1, 2, 3)
    # __set__: _x = 1
    # __set__: _y = 2
    # __set__: _z = 3
    print(pt3)
    # pt4 = NewPoint3D('1', 2, 3) |# ValueError: Координата должна быть целым числом
    print()

    print(' Демонстрация приоритета доступа дескриптора non-data к атрибутам класса '.center(80, '-'))
    print('Значение атрибута xr = 1, потому что атрибут _x = 1')
    print(pt3.xr, pt3.__dict__)  # 1 {'_x': 1, '_y': 2, '_z': 3}
    print('Дескриптор не включает сеттера, но если ему присвоить значение, то он станет новым атрибутом объекта')
    pt3.xr = 5
    print('А при обращении к данному атрибуту, будет возвращено установленное значение, как если бы это был обычной '
          'атрибут, а не дескриптор')
    print('Что указывает на то, что приоритет доступа к локальному свойству xr, точно такой же, как и к дескриптору'
          'не данных xr')
    print('Значение атрибута было найдено в локальной области, поэтому поиск остановился и было выведено его значение')
    print(pt3.xr, pt3.__dict__)  # 5 {'_x': 1, '_y': 2, '_z': 3, 'xr': 5}
    print()

    print('Если в классе ReadInX будет определен метод __set__, что следовательно создаст из него дескриптор данных'
          'И установить значение напрямую в словарь атрибутов экземпляра класса\n'
          'То при обращении к атрибуту xr, будет взято не локальное значение атрибута xr, а дескриптор данных')
    print('Это происходит потому что приоритет обращения к дескриптору данных выше, чем к локальным атрибутам'
          'экземпляра класса')
    pt3.__dict__['xr'] = 100
    print(pt3.xr, pt3.__dict__)  # 5 {'_x': 5, '_y': 2, '_z': 3, 'xr': 100}


