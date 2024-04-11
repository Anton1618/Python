'''Singleton (Одиночка) - порождающий шаблон проектирования в однопоточном приложении, гарантирующий,
что в один момент времени, может существовать только один экземпляр некоторого класса
При этом, класс предоставляет глобальную точку доступа к этому определенному экземпляру из любого участка системы

Во время создания очередного объекта, еще до его инициализации, осуществляется проверка на существование экземпляра
по данному классу, и если объект существует, то он замещает своей ссылкой "новый созданный" объект
'''


class DataBase:
    '''Предоставляет один объект (единственно возможный id в системе) с одним состоянием'''
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, user, psw, port, database=''):
        self.user: str = user
        self.psw: int = psw
        self.port: int = port
        self.database: str = database

    def __del__(self):
        DataBase.__instance = None

    def close(self):
        print(f'Закрытие соединения с БД')
    def __str__(self):
        return f'Данные установленного соединения: User:{self.user}, Port:{self.port}, ID:{id(self)}'
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
