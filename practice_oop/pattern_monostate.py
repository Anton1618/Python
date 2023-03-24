'''
Monostate может применяться в дополнение к singleton, для соблюдения уникальности объекта,
либо применяться самостоятельно, только для соблюдения особого состояния всех объектов данного класса

Предоставляет уникальное состояние для всех объектов класса
В сочетании с singletor, заменяет прочие переданные свойства теми, что уже установлены
'''
class DataBase:
    # __instance = None # Только для одного объекта. Также требуется переопределение метода __new__
    _shared_state = {} # Для одного состояния объектов

    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance

    # def __del__(self):
    #     DataBase.__instance = None

    def __init__(self, user, psw, port, database=''):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            self.user: str = user
            self.psw: int = psw
            self.port: int = port
            self.database: str = database

    def __call__(self):
        return f'Данные установленного соединения: User:{self.user}, Port:{self.port}'
    def close(self):
        print(f'Закрытие соединения с БД')
    def read(self):
        print(f'Чтение данных из БД...')
        print(self.database)
    def write(self, data):
        self.database += data + '\n\n' if type(data) is str else ' '.join(map(str, data)) + '\n\n'
        print(f'Запись данных в БД выполнена')

if __name__ == '__main__':
    db1 = DataBase('Anton', 1234, 80)
    print(f'ID соединения: {id(db1)}', db1())
    db2 = DataBase('Marusya', 101010, 90)
    db3 = DataBase('Lera', 5678, 40)
    print(f'ID соединения: {id(db2)}', db2())
    print(f'ID соединения: {id(db3)}', db3())

