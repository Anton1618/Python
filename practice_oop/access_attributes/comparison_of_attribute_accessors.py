'''Методы __getattribute__, __setattr__, __delattr__ и __getattr__.

Демонстрация методов, которые станут задействованы в операциях над атрибутами
'''

'''Бесконечная рекурсия
При использовании методов, если в них происходит обращение к атрибуту самого объекта, то это может приводить к
бесконечному циклу вызовов'''
class Recursive:
    def __setattr__(self, name, value):
        self.name = value

obj = Recursive()
# obj.x = 5  # RecursionError: maximum recursion depth exceeded


'''Во время обращения к целевому атрибуту, чтобы избежать бесконечной рекурсии, к нему требуется обращение не напрямую.
Для этого, к атрибуту рекомендуется обращение через метод родительского класса, вызывая функцию `super()`
Также, демонстрируется возможность обращения к атрибуту не через метод родителя, а через словарь объекта, ввиду того,
что не каждый родительский класс имеет целевые методы, ровно как и словарь атрибутов в объекте, если в классе 
определен атрибут __slots__'''
class FixedRecursive:
    def __setattr__(self, name, value):
        print(f'__setattr__ called for {name}')
        # Обращение к методу родительского класса
        # super().__setattr__(name, value)

        # Обращение к словарю атрибутов объекта
        self.__dict__[name] = value

    def __getattribute__(self, item):
        print(f'__getattribute__ called for {item}')
        # Обращение к методу родительского класса
        return super().__getattribute__(item)

        # Обращение к словарю атрибутов объекта невозможно, ввиду бесконечной рекурсии.
        # Команда превращает обращение `self.__dict__[item]` в бесконечный вызов атрибута `self.item`
        # return self.__dict__[item]

    def __getattr__(self, item):
        '''Метод применяется только если __getattribute__ не смог получить атрибут объекта
        Следовательно, реализует логику обращения к несуществующим атрибутам объекта'''
        print(f'__getattr__ called for {item}')
        # Обращение к методу родительского класса не имеет смысла
        # return super().__getattr__(item)
        # Возвращаемые данные
        # <class 'AttributeError'>
        # 'super' object has no attribute '__getattr__'

        return f'Атрибут {item} не определен'

    def __delattr__(self, item):
        print(f'__delattr__ called for {item}')
        # Обращение к методу родительского класса
        # super().__delattr__(item)

        # Обращение к словарю атрибутов объекта
        del self.__dict__[item]


if __name__ == '__main__':
    obj = FixedRecursive()
    print(' Установка атрибута через присвоение '.center(80, '-'))
    obj.attr1 = 'hello'
    # __setattr__ called for attr1
    # __getattribute__ called for __dict__
    print()

    print(' Установка атрибута через setattr '.center(80, '-'))
    setattr(obj, 'attr2', 'world')
    # __setattr__ called for attr2
    # __getattribute__ called for __dict__
    print()

    print(' Обращение к атрибуту через getattr '.center(80, '-'))
    print(getattr(obj, 'attr1'))
    # __getattribute__ called for attr1
    # hello
    print()

    print(' Обращение к атрибуту через hasattr '.center(80, '-'))
    print(hasattr(obj, 'attr2'))
    # __getattribute__ called for attr2
    # True
    print()

    print(' Обращение к несуществующему атрибуту '.center(80, '-'))
    print(getattr(obj, 'abracadabra', 'То самое долгожданное запасное значение'))
    # __getattribute__ called for abracadabra
    # __getattr__ called for abracadabra
    # Атрибут abracadabra не определен
    print()

    print(' Удаление атрибута функцией delattr '.center(80, '-'))
    delattr(obj, 'attr1')
    # __delattr__ called for attr1
    # __getattribute__ called for __dict__
    print()

    print(' Удаление атрибута оператором del '.center(80, '-'))
    del obj.attr2
    # __delattr__ called for attr2
    # __getattribute__ called for __dict__
    print()

    print(' Получение всех публичных атрибутов объекта '.center(80, '-'))
    print([i for i in dir(obj) if not i.startswith('_')])
    # __getattribute__ called for __dict__
    # __getattribute__ called for __class__
    # []
    print()
