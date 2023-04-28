'''Рассматриваются атрибуты доступа.

Обращение, изменение и удаление атрибутов, а также их поведение, при наследовании.
Все принципы относятся как к полям в классе и его экземпляре, так и их методам.
- public - публичный. По умолчанию, все объекты в Python являются публичными
- _protected - защищенный. Сигнализирует, что атрибут не подлежат изменению и применению вне логики класса, обращение
осуществляется внутри класса и во всех его производных классах.
- __private - приватный или частный. Сигнализирует, что атрибут не подлежит изменению и импортированию, обращение
осуществляется только внутри класса.
Призван исключить случайную перезапись наследуемого атрибута. На уровне интерпретатора, автоматически будет запущен
процесс запутывания имен (Name Mangling).
Идентификатор будет замен на _<наименование класса атрибута>__<предыдущее наименование атрибута>
Таким образом, при наследовании, в конечном объекте будут присутствовать обе реализации атрибута

Применение стороннего модуля accessify для введения невозможности обращения к защищенным и приватным атрибутам
'''
from accessify import protected, private


class A:
    public = 1
    _protected = 2
    __private = 3
    def __init__(self, public, protected, private):
        self.public = public
        self._protected = protected
        self.__private = private


class B(A):
    def __init__(self, public, protected, private):
        super().__init__(public, protected, private)
        self.public = public
        self._protected = protected
        self.__private = private


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_val(self):
        return self.x, self.y
    def _set_val(self, x, y):
        self.x, self.y = x, y
    def __del_val(self):
        del self.x, self.y


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_val(self):
        return self.x, self.y
    @protected
    def _set_val(self, x, y):
        self.x, self.y = x, y
    @private
    def __del_val(self):
        del self.x, self.y


if __name__ == '__main__':
    print(' Получение и изменение статических атрибутов класса A '.center(120, '-'))
    a = A('public_valueA', 'protected_valueA', 'private_valueA')
    print('Отображение текущих значений атрибутов в классе:')
    print({key: val for key, val in a.__class__.__dict__.items() if key in ('public', '_protected', '_A__private')})
    # {'public': 1,
    # '_protected': 2,
    # '_A__private': 3}
    print()

    print('Все атрибуты могут быть вызваны и изменены, как через сам класс, так и через его объект')
    print('Изменение значений для каждого атрибута класса. Состав:')
    a.__class__.public = 10
    a.__class__._protected = 20
    a.__class__._A__private = 30
    print({key: val for key, val in a.__class__.__dict__.items() if key in ('public', '_protected', '_A__private')})
    # {'public': 10,
    # '_protected': 20,
    # '_A__private': 30}
    print()


    print(' Наследование с сохранением изначальных значений приватных атрибутов класса B '.center(120, '-'))
    print('Цель приватных атрибутов - не допущение случайного переопределения при наследовании')
    b = B('public_valueB', 'protected_valueB', 'private_valueB')
    print('Процесс запутывания имен позволил сохранить первичное значение класса родителя')
    print(f'Значение приватного атрибута в классе родителе:\n'
          f'{b._A__private=},\n'  # b._A__private='private_valueB'
          f'Значение приватного атрибута в производном классе:\n'
          f'{b._B__private=}')  # b._B__private='private_valueB'
    print()


    print(' Доступ к методам класса и его экземпляра '.center(120, '-'))
    print('Доступ к методам классов и их экземпляров, по умолчанию, аналогичен получению доступа к их полям')
    p1 = Point1(1, 2)
    print({key: val for key, val in p1.__dict__.items()})  # {'x': 1, 'y': 2}
    print('Применение публичного метода для отображения состава объекта:')
    print(p1.get_val())  # (1, 2)
    print('Применение защищенного метода для установки новых значений для каждого атрибута объекта. Состав:')
    p1._set_val(10, 20)
    print({key: val for key, val in p1.__dict__.items() if key in ('x', 'y')})  # {'x': 10, 'y': 20}
    print('Применение приватного метода для удаления значений объекта. Состав:')
    p1._Point1__del_val()
    print({key: val for key, val in p1.__dict__.items() if key in ('x', 'y')})  # {'x': 10, 'y': 20}
    print()

    print('Применение для методов декораторов private и protected из стороннего модуля accessify')
    print('Применение  декораторов позволяет "наверняка" исключить доступ защищенным и приватным методам')
    p2 = Point2(1, 2)
    print({key: val for key, val in p2.__dict__.items()})
    print('Применение публичного метода для отображения состава объекта:')
    print(p2.get_val())
    print('Защищенные и приватные методы более недоступны для обращения по их идентификаторам и возбуждается исключение')
    # p2._set_val(10, 20)  # accessify.errors.InaccessibleDueToItsProtectionLevelException: Point2._set_val() is inaccessible due to its protection level
    # p2._Point2__del_val()  # accessify.errors.InaccessibleDueToItsProtectionLevelException: Point2.__del_val() is inaccessible due to its protection level


