'''Доступ к атрибутам через применение пользовательских геттеров и сеттеров,
a также применение функции property, которая задает новое поведение управляемым свойствам

Описание:
- get_email - геттер, возвращающий защищенный атрибут _email, во время выполнения команды obj.attr
- set_email - сеттер, устанавливающий переданную строку как новое значение почты, во время выполнения команды
    obj.attr = value
    Применяет валидатор для проверки корректности переданного значения
'''
import re


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self._email = email
        print(f'Инициирован новый пользователь {self.login}')

    def get_email(self):
        '''Пользовательский геттер'''
        return self._email
    def set_email(self, new_email=None):
        '''Пользовательский сеттер'''
        if not isinstance(new_email, str):
            raise TypeError('Почта должна быть указана строкой')
        pattern = re.compile(pattern=r'.{1,40}@.{1,10}\.{1,10}')
        if not (match := pattern.search(new_email)):
            raise ValueError('Указанная почта не соответствует формату: user@server.domain')
        self._email = match.string
    # Property-атрибуты
    email = property(get_email)
    email = email.setter(set_email)

    # Аналогично, с property-параметрами
    # email = property(
    #     fget=get_email,
    #     fset=set_email,
    # )


if __name__ == '__main__':
    print('Применение пользовательских методов')
    aleksey = UserMail('Aleksey', 'leha1985@mail.com')  # Инициирован новый пользователь Aleksey
    print('Получение почты')
    print(aleksey.get_email())  # leha1985@mail.com
    print('Изменение почты')
    aleksey.set_email('alekseymironov1985@mail.com')
    print('Получение почты')
    print(aleksey.get_email())  # alekseymironov1985@mail.com
    print('Попытка установки некорректного значения')
    # print(aleksey.set_email(111))  # TypeError: Почта должна быть указана строкой
    # print(aleksey.set_email('badmailcom'))  # ValueError: Указанная почта не соответствует формату: user@server.domain
    # print(aleksey.set_email())  # TypeError: Почта должна быть указана строкой
    print()

    print('Применение property-методов')
    petr = UserMail('Petr', 'petrvalerievich1990@mail.com')  # Инициирован новый пользователь Petr
    print('Получение почты')
    print(petr.email)  # petrvalerievich1990@mail.com
    print('Изменение почты')
    petr.email = 'valeryevichpetr1990@mail.com'
    print('Получение почты')
    print(petr.email)  # valeryevichpetr1990@mail.com
    print('Попытка установки некорректного значения')
    # aleksey.email = 111  # TypeError: Почта должна быть указана строкой
    # aleksey.email = 'badmailcom'  # ValueError: Указанная почта не соответствует формату: user@server.domain
    # aleksey.email = None  # TypeError: Почта должна быть указана строкой
    print()