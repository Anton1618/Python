'''
Singleton (Одиночка) - порождающий шаблон проектирования в однопоточном приложении, гарантирующий,
что в один момент времени, может существововать только один экземпляр некоторого класса
При этом, класс предоставляет глобальную точку доступа к этому определенному экземпляру из любого участка системы
'''
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port, database=''):
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
