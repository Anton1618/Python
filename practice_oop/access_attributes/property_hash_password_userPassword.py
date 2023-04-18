'''Инициализатор класса User принимает в качестве аргументов имя пользователя и пароль и сохраняет их в
атрибут .name и в свойство .password соответственно.
 Мы используем свойство для управления тем как ваш класс обрабатывает входной пароль
 Метод получения вызывает AttributeError всякий раз когда пользователь пытается получить текущий пароль
 Это превращает .password в атрибут-свойство только для записи

 В методе установки .password применяется os.urandom() для генерации 32-байтовой случайной строки в качестве соли хеш-функции.
 Чтобы сгенерировать хэшированный пароль, используем hashlib.pbkdf2_hmac()
 Затем вы сохраняете полученный хэшированный пароль в закрытом атрибуте ._hashed_password
Это гарантирует, что вы никогда не сохраните открытый текстовый пароль в каком либо извлекаемом атрибуте'''

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
    print(jack.password)
    jack.password = 'new_secret'
    print(jack._hashed_password)
