'''Метод класса, метод объекта, статический метод.
Способы передачи значений.
Способы создания объекта
Динамический счетчик созданных объектов

Описание:
- Метод класса make_cat применяется как набор установленных шаблонов, для создания объекта по ним в конструкторе класса
- Метод класса increment_count применяется как счетчик созданных от класса объектов
- Метод объекта meow возвращает определенные свойства объекта
- Статический метод get_human_age вычисляет возраст кошки в соответствующий человеку и сохраняет результат в переменную объекта.
Если существует вычисленный результат, то метод возвращает его.
Если произошло изменение значения возраста, то вычисление осуществляется заново.
- Метод объекта human_age - геттер, который применяет статический метод и возвращает на основе его функционала
результат по атрибуту объекта
'''

class BlueCat:
    breed = 'Russian Blue'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__human_age = None
        BlueCat.increment_count()

    def meow(self):
        return f'{self.name} of {self.breed} says: Meow!'

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        # Во время инициализации, в формате вызова класса (nameObj = Class(parameters)) получает набор параметров
        # И возвращает объект на их основе, применяя конструктор класса
        # Обращение к конструктору класса в методе, возможно как через идентификатор класса, так и через ссылку на него
        if name == 'Tom':
            return BlueCat('Tom', 2.3)
        elif name == 'Angela':
            return cls('Angela', 1.2)  # Для атрибутов класса, рекомендуется применение ссылки cls на него,
            # во избежание смены идентификатора и возникновения ошибок в дальнейшем
        return cls('Ginger', 1.8)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not 0 < new_age < 20:
            raise ValueError('Значение должно быть целым положительным числом до 20')
        self._age = new_age
        self.__human_age = None

    @property
    def human_age(self):
        # Применение метода возможно как из класса, так и из метода
        # Для передачи в метод значения, как из класса, так и из объекта, потребуется явная передача ссылки на источник
        age = self.age
        if self.__human_age is None:
            print('Вычисление...')
            self.__human_age = self.get_human_age(age)
        return self.__human_age

    @staticmethod
    def get_human_age(age):
        '''Преобразование возраста кошки в относительный возраст, соизмеримо человеку'''
        # Вызвать метод можно из класса и его экземпляра
        # Для передачи в метод аргументов класса или его экземпляра, потребуется явная передача ссылки на этот объект
        if not 0 < age < 20:
            raise ValueError('Значение должно быть целым положительным числом до 20')
        if 0 < age < 5:
            to_human_age = round(age * 7)
        elif 5 < age < 11:
            to_human_age = round((age - 5) * 4 + 35)
        elif 11 < age < 20:
            to_human_age = round((age - 11) * 3 + 59)
        return to_human_age


if __name__ == '__main__':
    print('Объект Tom инициализируется простой передачей параметров методу __init__')
    tom = BlueCat('Tom', 2)
    print(tom.meow())
    print()

    print('Объект Angela инициализируется путем передачи параметров методу класса make_cat')
    angela = BlueCat.make_cat('Angela')
    print(angela.meow())
    print()

    print('Метод преобразования возраста кошки в человеческий. '
          'Либо вычисляет и возвращает значение, либо возвращает ранее вычисленное значение')
    print('--- Применение метода объекта')
    print(angela.human_age)  # Вычисление и возвращение результата
    print(angela.human_age)  # Возвращение ранее вычисленного результата
    angela.age = 10  # Задание нового значения
    print(angela.human_age)  # Вычисление на новых данных
    print('--- Применение статического метода через класс и через объект')
    print(BlueCat.get_human_age(10))  # Вычисление через класс
    print(angela.get_human_age(10))  # Вычисление через объект
    assert BlueCat.get_human_age(10) == 55
    assert BlueCat.get_human_age(0.1) == 1
    assert BlueCat.get_human_age(1.9) == 13
    # BlueCat.get_human_age(0)  # ValueError: Значение должно быть целым положительным числом до 20
    # BlueCat.get_human_age(-1)  # ValueError: Значение должно быть целым положительным числом до 20
    # BlueCat.get_human_age(20)  # ValueError: Значение должно быть целым положительным числом до 20
    print()

    print('Количество созданных кошек')
    print(BlueCat.count)
    print()
