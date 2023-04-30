'''Реализация хеширования пароля.

Свойство password имеет:
    - сеттер, в котором применяется os.urandom() для генерации 32-байтовой случайной строки в качестве соли хеш-функции.
    Чтобы сгенерировать хэшированный пароль, применяется hashlib.pbkdf2_hmac()
    Сохранение зашифрованного (хешированного) пароля осуществляется в закрытом атрибуте _hashed_password
    Это гарантирует зашифрованное сохранения пароля и его отображение только в таком виде в любом извлекаемом атрибуте
'''
import hashlib
import os

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError('Пароль можно только менять, нельзя смотреть')

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            'sha256', plaintext.encode('utf-8'), salt, 100_000
        )

if __name__ == '__main__':
    jack = User('Jack', 'secret_key')
    print(jack._hashed_password)
    # print(jack.password)  # AttributeError: Пароль можно только менять, нельзя смотреть
    jack.password = 'new_secret'
    print(jack._hashed_password)
