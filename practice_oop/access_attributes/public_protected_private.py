'''Атрибуты доступа по соглашению: public, protected, private'''

class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name # Публичный атрибут. Применяется для свободного обращения
        self._balance = balance # Защищенный атрибут. По соглашению не должен применяться вне класса
        self.__passport = passport # Приватный атрибут. По соглашению не должен применяться и изменяться
        # Включает автоматический процесс запутывания имен, но возможное обращение через: _Класс__атрибут

    def account_data(self):
        '''Разрешенный API для обращения к свойствам объекта'''
        return f'Имя: {self.name}\nБаланс: {self._balance}\nПаспортные данные: {self.__passport}'

if __name__ == '__main__':
    account1 = BankAccount('Bob', 100_000, '42-8456')
    print(account1.account_data())
    print(account1.name)
    print(account1._balance)
    print(account1._BankAccount__passport)