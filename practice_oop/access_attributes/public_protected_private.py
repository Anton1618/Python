'''Атрибуты доступа по соглашению: public, protected, private'''


class A:
    public = 1
    _protected = 2
    __private = 3
    def __init__(self):
        self.public = 'public_valueA'
        self._protected = 'protected_valueA'
        self.__private = 'private_valueA'


class B(A):
    def __init__(self):
        super().__init__()
        self.public = 'public_valueB'
        self._protected = 'protected_valueB'
        self.__private = 'private_valueB'


if __name__ == '__main__':
    print(' Класс A '.center(80, '-'))
    a = A()
    print('Отображение текущих значений атрибутов в классе:')
    print(a.__class__.__dict__)
    print()

    print('Все атрибуты могут быть вызваны и изменены, как через сам класс, так и через его объект, несмотря на '
          'установленные ограничения')
    print('Установка новых значений для каждого атрибута')
    a.__class__.public = 10
    a.__class__._protected = 20
    a.__class__._A__private = 30
    print('Отображение теперь измененных атрибутов в классе:')
    print(a.__class__.__dict__)
    print()

    print(' Класс B '.center(80, '-'))
    print('Цель приватных атрибутов - не допущение случайного переопределения при наследовании')
    b = B()
    print('Отображение состава атрибутов в объекте производного класса:')
    print(b.__dict__)
    print('Процесс запутывания имен позволил сохранить первичное значение класса родителя')
    print(f'Значение приватного атрибута в классе родителе: {b._A__private=},\n'
          f'Значение приватного атрибута в производном классе: {b._B__private=}')
    print()

