'''Сравнение обращения и взаимодействия с первичными атрибутами, пользовательскими методами и property-свойствами'''
'''Вся логика обработки данных в методах опускается и демонстрируются только способы обращения'''
'''Для атрибутов, декорируемых с помощью символа (@), данная демонстрация носит лишь ознакомительный характер
Корректным станет являться именование изначальных атрибутов аналогично управляемым свойствам
Это позволяет:
- применять управляемые свойства, при инициализации экземпляра класса (неактуально, при зависимости от уже установленных);
- избежать дополнительных уязвимостей, связанных с наличием дополнительных атрибутов, как незащищенных точек доступа'''


class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self._balance = balance
        self.__passport = passport


    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    def del_name(self):
        del self._name
    # Property атрибуты:
    # name = property()
    # name = name.getter(get_name)
    # Две строки выше эквивалентны записи: name = property(get_name)
    name = property(get_name)
    name = name.setter(set_name)
    name = name.deleter(del_name)


    def get_balance(self):
        return self._balance
    def set_balance(self, new_balance):
        self._balance = new_balance
    def del_balance(self):
        del self._balance
    # Property параметры:
    # Могут быть записаны в одну строку, без явного указания параметров
    # balance = property(get_balance, set_balance, del_balance, 'Документации по атрибуту balance')
    # Могут быть записаны с явным указанием параметров
    balance = property(
        fget=get_balance,
        fset=set_balance,
        fdel=del_balance,
        doc='Документации по атрибуту balance'
    )


    @property
    def passport(self):
        return self.__passport
    @passport.setter
    def passport(self, new_passport):
        self.__passport = new_passport
    @passport.deleter
    def passport(self):
        del self.__passport


if __name__ == '__main__':
    print(' Прямое обращение к первоначальным атрибутам '.center(120, '-'))
    ilya = BankAccount('Ilya', 1000, '23-439501')
    print('Объект:', ilya.__dict__)
    print('Получение данных')
    print(ilya._name)
    print(ilya._balance)
    print(ilya._BankAccount__passport)
    print('Изменение данных')
    ilya._name = 'test-name'
    ilya._balance = 'test-balance'
    ilya._passport = 'test-passport'
    print(ilya.__dict__)
    print('Удаление данных')
    del ilya._name
    del ilya._balance
    del ilya._BankAccount__passport
    print(ilya.__dict__)
    print()
    print()


    print(' Применение пользовательских методов '.center(120, '-'))
    lera = BankAccount('Valeria', 1000, '14-464219')
    print('Объект:', lera.__dict__)
    print('Получение данных')
    print(lera.get_name())
    print(lera.get_balance())
    print(lera.passport)  # Атрибут декорирован, обращение может осуществляться либо напрямую к атрибуту, либо через
    # публичный property атрибут (управляемое свойство)
    print('Изменение данных')
    lera.set_name('test-name')
    lera.set_balance('test-balance')
    lera.passport = 'test-passport'  # Атрибут декорирован, присвоение может осуществляться либо напрямую в атрибут,
    # либо через публичный property атрибут (управляемое свойство)
    print(lera.__dict__)
    print('Удаление данных')
    lera.del_name()
    lera.del_balance()
    del lera.passport  # Атрибут декорирован, удаление может осуществляться либо напрямую над атрибутом,
    # либо над публичным property атрибутом (управляемым свойством)
    print(lera.__dict__)
    print()
    print()


    print(' Применение property-методов - управляемых свойств над атрибутами '.center(120, '-'))
    mike = BankAccount('Mikel', 1000, '42-610927')
    print('Объект:', mike.__dict__)
    print('Получение данных')
    print(mike.name)
    print(mike.balance)
    print(mike.passport)
    print('Изменение данных')
    mike.name = 'test-name'
    mike.balance = 'test-balance'
    mike.passport = 'test-passport'
    print(mike.__dict__)
    print('Удаление данных')
    del mike.name
    del mike.balance
    del mike.passport
    print(mike.__dict__)
    print()
    print()

