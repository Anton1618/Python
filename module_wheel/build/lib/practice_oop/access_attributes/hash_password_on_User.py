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
        self._hashed_password = hashlib.pbkdf2_hmac('sha256', plaintext.encode('utf-8'), salt, 100_000)


if __name__ == '__main__':
    jack = User('Jack', 'secret_key')
    print(jack._hashed_password)  # b'C,\x02[\x90\xe8&-;\xf3oD:\x06|\xc9+\xfe\xd6\xd6Hbn\x93\xcbHd\xdc\xf3\x9a\x87\x17'
    # print(jack.password)  # AttributeError: Пароль можно только менять, нельзя смотреть
    jack.password = 'new_secret'
    print(jack._hashed_password)  # b'Y\xfb]\xe3\xa1\xa2r\xbb\xeb\xde8^\xd2y\xf7R\xe0"{6\xa6\xaaS\xfax\r\xa9\xc7~\xdc\xb7\x11'
