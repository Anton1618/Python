'''
Monostate может применяться в дополнение к singleton, для соблюдения уникальности объекта,
либо применяться самостоятельно, только для соблюдения особого состояния всех объектов данного класса

Предоставляет уникальное состояние для всех объектов класса
В сочетании с singletor, заменяет прочие переданные свойства, теми, что уже установлены
'''
class DataBase:
    '''Предоставляет множество объектов (разные id) с одним единым состоянием'''
    # __instance = None # Только для одного объекта. Также требуется переопределение метода __new__
    __shared_state = {} # Для одного состояния объектов

    # def __new__(cls, *args, **kwargs):
    #     '''Включение паттерна singleton'''
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance

    def __del__(self):
    #   DataBase.__instance = None
        DataBase._shared_state = {}

    def __init__(self, user, psw, port, database=''):
        self.__dict__ = self.__shared_state
        if not self.__shared_state:
            self.user: str = user
            self.psw: str = psw
            self.port: int = port
            self.database: str = database

    def __str__(self):
        return f'Данные установленного соединения: User:{self.user}, Port:{self.port}, ID:{id(self)}'
    def close(self):
        print(f'Закрытие соединения с БД')
        self.__del__()
    def read(self):
        print(f'Чтение данных из БД...')
        print(self.database)
    def write(self, data):
        self.database += data + '\n\n' if type(data) is str else ' '.join(map(str, data)) + '\n\n'
        print(f'Запись данных в БД выполнена')


if __name__ == '__main__':
    print('Инициализация объекта Иван')
    ivan = DataBase('Ivan', 'pypy10', 80)
    print(ivan)
    print()

    print('Инициализация объекта Антон')
    anton = DataBase('Anton', 'abc10', 90)
    print(anton)
    print()

    print('Инициализация объекта Лера')
    lera = DataBase('Lera', 'qwerty19', 40)
    print(lera)
    print()

    print('Изменение состояния одного объекта влияет и на другие')
    anton.port = 500
    print(ivan)
    print(anton)
    print(lera)

