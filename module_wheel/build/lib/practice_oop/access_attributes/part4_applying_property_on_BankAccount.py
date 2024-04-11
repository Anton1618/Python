'''Применение свойств property для соответствия концепции инкапсуляции.

Описание:
- Декорируемое свойство password имеет:
    - геттер - представляет собой вечный валидатор на соответствие пароля и пользовательского ввода, для получения
        доступа к нему.
        Важным моментом является то, что изначально поле _password задается объекту при инициализации, и только затем
        контролируется его управляющим свойством property, иначе, попытка валидации на уже имеющемся пароле не имела бы
        смысла.
        После сохранения начального значения password, property декорирует атрибут, что заменит ссылку на изначальный
        атрибут, ссылкой на управляемое свойство.
        В последующем, это управляемое свойство станет применяться для получения самого пароля, организуя таким образом
        функционал аутентификации пользователя в других методах.
    - сеттер - валидатор корректности переданного значения, включает условия и возбуждения исключений, если переданное
        значение не соответствует заданным условиям.
        Изначально включает геттер пароля для аутентификации пользователя и получения доступа к смене пароля
        Также включает статический метод - валидатор вхождения в словарь уязвимых паролей

- Декорируемое свойство email имеет:
    - геттер - простой метод, возвращающий значение
    - сеттер - валидатор корректности переданного значения, включает условия и возбуждения исключений, если переданное
        значение не соответствует заданным условиям.
        Изначально включает геттер пароля, для аутентификации пользователя и получения доступа к смене почты

- Декорируемое свойство passport имеет:
    - геттер - метод, возвращающий значение.
        Включает геттер пароля для аутентификации пользователя и получения паспортных данных
    - сеттер - метод, запрещающий изменение паспортных данных пользователя
'''
import re
import string


class User:
    def __init__(self, login, email, password, passport):
        self.login = login
        self._email = email
        self._password = password
        self.__passport = passport
    @property
    def passport(self):
        '''Получение паспортных данных клиента'''
        if self.password:
            return self.__passport
    @passport.setter
    def passport(self, new_passport=None):
        '''Изменение паспортных данных клиента'''
        raise AttributeError('Изменение паспортных данных запрещено')

    @property
    def password(self):
        '''Получение пароля. Включена проверка пользователя'''
        while input('Введите пароль: ') != self._password:
            print('Пароль не верен, попробуйте вновь')
        else:
            print('Пароль принят')
            return self._password
    @password.setter
    def password(self, new_password=None):
        '''Изменение пароля. Включена проверка пользователя'''
        if self.password:
            pass
        if not isinstance(new_password, str):
            raise TypeError('Пароль должен включать только латинские буквы, цифры от 0 до 9 и символы !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        if not 6 < len(new_password) < 16:
            raise ValueError('Пароль должен быть не менее 6 символов и не более 16 символов')
        if ' ' in new_password:
            raise ValueError('Пароль не должен включать в себя пробелы')
        if not any([i in f'{string.digits}' for i in new_password]):
            raise ValueError('Пароль должен содержать по крайней мере одну цифру от 0 до 9')
        if not any([i in f'{string.ascii_letters}' for i in new_password]):
            raise ValueError('Пароль должен содержать по крайней мере одну букву латинского алфавита в большом и малом регистрах')
        if not any([i in f'{string.punctuation}' for i in new_password]):
            raise ValueError(f'Пароль должен содержать по крайней мере один специальный символ: {string.punctuation}')
        if self.login in new_password \
                or self.email in new_password \
                or self.login.lower() in new_password \
                or self.login.capitalize() in new_password\
                or self.login.upper() in new_password:
            raise ValueError('Пароль не должен содержать имени пользователя или его почты')
        self.easy_password(new_password)
        self._password = new_password
        print('Пароль изменен')

    @staticmethod
    def easy_password(password):
        '''Применение файла уязвимых сочетаний, для проверки надежности задаваемого пароля'''
        with open('easy_passwords.txt') as f:
            for i in f.readlines():
                if i.replace('\n', '') in password:
                    raise ValueError(f'Пароль включает уязвимую комбинацию: {i}')

    @property
    def email(self):
        '''Получение почты клиента'''
        return self._email
    @email.setter
    def email(self, new_email=None):
        '''Изменение почты. Включена проверка пользователя'''
        if self.password:
            pass
        if not isinstance(new_email, str):
            raise TypeError('Почта должна быть строкой')
        pattern = re.compile(pattern=r'.{1,40}@.{1,10}\.{1,10}')
        if not (match := pattern.search(new_email)):
            raise ValueError('Указанная почта не соответствует формату: user@server.domain')
        self._email = match.string
        print('Почта изменена')


if __name__ == '__main__':
    print(' Инициализация клиента '.center(80, '-'))
    mike = User('Mike', 'mike_email@mail.com', 'hellowordl1*', '34-67-035834')
    print(mike.__dict__)
    # {'login': 'Mike', '_email': 'mike_email@mail.com', '_password': 'hellowordl1*', '_User__passport': '34-67-035834'}
    print()

    print(' Получение и изменение почты '.center(80, '-'))
    print(f'Текущая почта: {mike.email}')
    # Текущая почта: new_mike_email@mail.com
    print()
    print('Изменение почты')
    mike.email = 'new_mike_email@mail.com'
    # Введите пароль: hellowordl1* -> Пароль принят -> Почта изменена
    print()
    print('Получение почты')
    print(f'Новая почта: {mike.email}')
    # Новая почта: new_mike_email@mail.com
    print()
    print()

    print(' Получение и изменение пароля '.center(80, '-'))
    print('Получение пароля')
    print(f'Текущий пароль: {mike.password}')
    # Введите пароль: hellowordl1* -> Пароль принят -> Пароль изменен
    print()
    print('Изменение пароля')
    mike.password = 'hellowordl2*'
    print()
    print('Получение пароля')
    print(f'Текущий пароль: {mike.password}')
    print()
    # Введите пароль: hellowordl2* -> Пароль принят -> Текущий пароль: hellowordl2*
    print()

    print(' Получение и изменение паспортных данных '.center(80, '-'))
    print(f'Текущие паспортные данные: {mike.passport}')
    # Введите пароль: hellowordl2* -> Пароль принят
    print('Изменение паспортных данных (запрещено)')
    # mike.passport = '34-23-235839' # AttributeError: Изменение паспортных данных запрещено
    print()

    print(' Результирующий словарь атрибутов со значениями после всех операций '.center(80, '-'))
    print(mike.__dict__)
    # {'login': 'Mike', '_email': 'new_mike_email@mail.com', '_password': 'hellowordl2*', '_User__passport': '34-67-035834'}
    print()
