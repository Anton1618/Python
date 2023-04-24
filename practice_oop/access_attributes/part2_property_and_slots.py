'''Доступ к атрибутам ч2. Применение сеттеров и геттеров декоратора property

Описание:
-- Производится установка правил в специальных геттерах и сеттерах декоратора property
-- Осуществляется применение атрибута __slots__ для оптимизации памяти и исключения возможности добавления новых атрибутов
Определения:
- Сеттер (устанавливает, от слова set) — это метод, который изменяет значение поля.
- Геттер (получает, от слова get) — это метод, который возвращает значение поля.
Применяются только при необходимости задания определенной логики, т.е. для определения правил получения и изменения
атрибутов
'''

# Требуется определенная логика задания правил установки значений
# - Обязательное наличие имени объекта - атрибут name
# - Значение возраста объекта должно находиться в диапазоне от 1 до 15 не включительно
# - Исключение возможности создания новых атрибутов

from pympler.asizeof import asizeof
from sys import getsizeof


class Human:
    '''Атрибут заменяет словарь атрибутов в объекте, автоматически создавая дескриптор для каждого атрибута с
    определением этих методов, следовательно, сокращая размер занимаемой памяти по сравнению со словарем, а также
    исключением возможности его изменить'''
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Установка публичных геттеров для получения через них соответствующих защищенных значений атрибутов
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # Установка публичных сеттеров для получения через них соответствующих защищенных значений
    @name.setter
    def name(self, value):
        if not value:
            raise AttributeError('Name cannot be empty')
        self._name = value

    @age.setter
    def age(self, value):
        if value not in range(1, 15):
            raise AttributeError('Age should be in 1-15')
        self._age = value

    # Обращение к свойству осуществляется через публичный идентификатор, а не имя метода
    def __repr__(self):
        return f'Это человек по имени {self.name}, ему {self.age}лет'


if __name__ == '__main__':
    print('Благодаря наличию сеттеров и геттеров property, соблюдается:\n'
          '- Корректность значений, при создании объекта,\n'
          '- Корректность значений, при изменении значения по прямому обращению к атрибуту объекта,\n'
          'Благодаря наличию статического атрибута класса - __slots__ со списком разрешенных атрибутов:\n'
          '- Производится оптимизация памяти,\n'
          '- Исключается возможность создания нового атрибута, как по прямому обращению к объекту, так и через словарь '
          'свойств')
    # tom = Human('Tom', 1000)  # AttributeError: Age should be in 1-15
    tom = Human('Tom', 1)
    # tom.age = 1000  # AttributeError: Age should be in 1-15
    tom.age = 5
    # tom.age2 = 1000 # AttributeError: Only allowed ('name', 'age')
    # tom.__dict__['age'] = 1000 # AttributeError: 'Human' object has no attribute '__dict__'.
    print(tom)
    print()

    print('Сравнение веса объектов с атрибутом свойств __slots__ и с дефолтным атрибутом словаря свойств __dict__')
    print('Objets attributes Tom')
    print([f'{i} - {getattr(tom, i)}' for i in tom.__slots__])
    print(f'The weight object with the __slots__ attribute:\n'
          f'getsizeof: {getsizeof(tom)}\n'
          f'asizeof: {asizeof(tom)}')
    print()


    class Human2(Human): pass


    angela = Human2('Angela', 3)
    print('Objets attributes Angela')
    print([f'{i} - {getattr(angela, i)}' for i in angela.__slots__])
    print(f'The weight object with default attribute dictionary:\n'
          f'getsizeof: {getsizeof(angela)}\n'
          f'asizeof: {asizeof(angela)}''')
    print()
