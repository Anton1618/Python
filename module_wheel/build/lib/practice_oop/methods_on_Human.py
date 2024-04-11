'''Метод класса, метод объекта, статический метод. Изменение атрибутов в зависимости от мутабельности значения

Описание:
- Инициализация объекта с атрибутами, которые либо переданны в параметрах,
либо установлены явным присвоением дефолтных свойств класса

- Id элементов, которые не были переданы в параметрах, при инициализации объекта,
станут совпадать с явно заданными дефолтными значениями класса,
что станет отражено рядом с результатом по ним от справочного метода objectInfo

- Изменение атрибутов. При изменении атрибутов в объекте, которые относятся к классу,
    - переопределение неизменяемых атрибутов приведет к созданию нового локального атрибута,
    - переопределение изменяемых атрибутов приведет к изменению атрибутов, что отразиться на всех объектах класса
'''

class Human:
    job = 'unemployed'
    personal_property = ['house']
    defaultName = 'no_name'
    defaultSecondName = 'no_second_name'
    defaultLastName = 'no_last_name'
    count = 0 # Счетчик созданных экземпляров класса

    def __init__(self, **kwargs):
        '''Явное создание персональных атрибутов объекта, на основе параметров, либо дефолтных значениях класса'''
        self.name = kwargs['name'] if 'name' in kwargs else self.__class__.defaultName
        self.secondName = kwargs['second_name'] if 'second_name' in kwargs else self.__class__.defaultSecondName
        self.lastName = kwargs['last_name'] if 'last_name' in kwargs else self.__class__.defaultLastName
        self.increment_count() # Благодаря возможности ссылки-self обращаться к свойствам и методам класса, применяется метод класса

    @classmethod
    def make_object(cls, *args):
        '''Метод класса.
        Во время инициализации в формате вызова класса (nameObj = Class(parameters)) получает набор параметров
        И возвращает объект на их основе, применяя конструктор класса'''
        if 'Feodosiy' in args:
            return cls(name='Feodosiy', second_name='Chackiy')
        elif 'Mary' in args:
            return cls(name='Mary', last_name='Petrovna')
        elif 'Frank' in args:
            return cls(name='Frank', second_name='Bulrich')
        return cls(name='defaultMethodName', second_name='defaultMethodSecondName', last_name='defaultMethodLastName')

    @classmethod
    def increment_count(cls):
        '''Class Method - метод класса.
        Счетчик объектов, увеличивающий своё значение, при создании нового объекта'''
        cls.count += 1

    @classmethod
    def classInfo(cls):
        '''Class Method - метод класса.
        Справочный метод, выводящий названия дефолтных атрибутов класса и их id'''
        print(f'Default attributes of the Human class and their id:')
        print(f'Class attr name: {(val:=cls.defaultName)} | id: {id(val)}',
              f'Class attr second_name: {(val:=cls.defaultSecondName)} | id: {id(val)}',
              f'Class attr last_name: {(val:=cls.defaultLastName)} | id: {id(val)}',
              sep='\n')

    def objectInfo(self):
        '''Instance Method - обычный метод экземпляра
        Спарвочный метод, выводящий названия установленных атрибутов объекта и их id'''
        print(f'{id(self)} object attributes set and their id:')
        print(f'Object attr name: {(val:=self.name)} | id: {id(val)} {"(default)" if val == self.__class__.defaultName else ""}',
              f'Object attr second_name: {(val:=self.secondName)} | id: {id(val)} {"(default)" if val == self.__class__.defaultSecondName else ""}',
              f'Object attr last_name: {(val:=self.lastName)} | id: {id(val)} {"(default)" if val == self.__class__.defaultLastName else ""}',
              sep='\n')


if __name__ == '__main__':
    print(Human.classInfo())
    print()

    print('Ivan object initialization')
    ivan = Human(name='Ivan', second_name='Ivanov')
    print(f'All objects count: {Human.count}')
    print(ivan.objectInfo())
    print()

    print('Maksim object initialization')
    maksim = Human(last_name='Maksimovich')
    print(f'All objects count: {Human.count}')
    print(maksim.objectInfo())
    print()

    print('Overriding an immutable attribute')
    ivan.job = 'employed' # Переопределение в классе неизменяемого атрибута
    print(f'New personal attribute in the object: {ivan.job}') # приведет к созданию у объекта личного атрибута с установленным значением
    print(f'The former class attribute remains unchanged: {Human.job}') # Не приведет к изменению этих атрибутов в классе
    print(f'and another class objects: {maksim.job}') # и других объектах
    print()

    print('Overriding a mutable attribute')
    ivan.personal_property.extend(('car', 'motobike')) # Переопределение в классе изменяемого атрибута,
    print(f'The class has a changed attribute: {Human.personal_property}') # приведет к изменению данного атрибута в классе
    print(f'and all objects of the class: {maksim.personal_property}') # а также динамическому обновлению этого атрибута во всех экземплярах класса
    print()

    print('Initiating an object though a constructor')
    print('Frank object initialization')
    frank = Human(name='Frank')
    print(f'All objects count: {Human.count}')
    print(frank.objectInfo())

