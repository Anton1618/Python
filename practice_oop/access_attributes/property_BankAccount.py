'''Доступ к атрибутам через применение пользовательских геттеров и сеттеров,
a также применение функции property, которая задает новое поведение управляемым свойствам

Описание:
Представлены три атрибута, которые имеют персональные методы для их обработки
Атрибут _name декорирован сахаром @ и может (должен) иметь идентификатор, соответствующий управляемым свойствам
для применения их функционала при инициализации. Но в последующем, атрибут имеет запрет на изменение в управляемом
свойстве, поэтому, при изначальной инициализации, указан под другим именем, что позволяет устанавливать любое значение,
которое в дальнейшем уже будет контролироваться управляющим свойством
- Обращение к первоначальным атрибутам напрямую
- Применение пользовательских методов на объектах
- Применение property-методов на объектах
'''

# Требуется задание определенной логики для установки значений
# - Значение баланса должно являться числом и не опускаться ниже ноля
# - К атрибутам можно обратиться как по их изначальным идентификаторам, так и по предоставленным публичным аналогам
# из методов обработчиков


class BankAccount:
    def __init__(self, name, passport, balance=0):
        self._name = name
        self._balance = balance
        self.__passport = passport
        print(f'Инициирование клиента {self.name} {self.__passport}')

    # Для атрибута name установлено свойство только получать значение, либо удалять, но не изменять
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        raise ValueError('Изменение имени запрещено')
    @name.deleter
    def name(self):
        del self._name


    # Для атрибута passport установлены запрещающие свойства получения, установки и удаления атрибута
    def get_passport(self):
        raise ValueError('Получение паспортных данных запрещено')
    def set_passport(self, value):
        raise ValueError('Изменение паспортных данных запрещено')
    def del_passport(self):
        raise ValueError('Удаление паспортных данных запрещено')
    passport = property()
    passport = passport.getter(get_passport)
    passport = passport.setter(set_passport)
    passport = passport.deleter(del_passport)

    # Для атрибута balance установлены свойства получения, установки, удаления и документирование атрибута
    def get_balance(self):
        return self._balance
    def set_balance(self, value):
        if value < 0:
            print(f'Списание средств со счета на сумму: {value}')
        if value > 0:
            print(f'Пополнение счета на сумму: {value}')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        if self._balance + value < 0:
            raise ValueError('Недостаточно средств на счете ')
        self._balance += value
    def del_balance(self):
        del self._balance
    balance = property(
        fget=get_balance,
        fset=set_balance,
        fdel=del_balance,
        doc='Баланс клиента банка')


if __name__ == '__main__':
    print('Применение изначальных атрибутов на объекте Maksim')
    maksim = BankAccount('Maksim', '2343-582947', 1_000)
    print('Присвоение значения атрибуту balance осуществляется напрямую, без задействия методов обработки и вопреки '
          'установленным правилам')
    maksim._balance = 1_000
    maksim._balance = -1_300
    print(f'Баланс: {maksim._balance}')
    print(f'Удаление атрибута balance')
    del maksim._balance
    print(maksim.__dict__)
    print()

    print('Применение пользовательских методов на объекте Vasiliy')
    vasiliy = BankAccount('Vasiliy', '2354-345964', 1_000)
    vasiliy.set_balance(1_000)
    vasiliy.set_balance(-1300)
    print(f'Баланс: {vasiliy.get_balance()}')
    print(f'Удаление атрибута balance')
    vasiliy.del_balance()
    print(vasiliy.__dict__)
    print()

    print('Применение property-методов на объекте Petr')
    petr = BankAccount('Petr', '3455-235903', 1_000)
    petr.balance = 1000
    petr.balance = -150
    print(f'Баланс: {petr.balance}')
    print(f'Удаление атрибута balance')
    del petr.balance
    print(petr.__dict__)
    print()



