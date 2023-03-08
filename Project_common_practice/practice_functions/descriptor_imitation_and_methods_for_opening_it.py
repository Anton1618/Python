from contextlib import contextmanager

class Resource:
    def __init__(self):
        self.opened = False

    def open(self, args):
        self.opened = True
        match args.split():
            case reading as r, *arg if r in ('r', 'rb'):
                self.arg = f'Reading process... {" ".join(arg)}'
            case writing as w, *arg if w in ('w', 'x', 'wb'):
                self.arg = f'Writing process... {" ".join(arg)}'
            case reading_and_writing as rw, *arg if rw in ('r+', 'w+'):
                self.arg = f'Reading and writing... {" ".join(arg)}'
            case _:
                raise ValueError('Unknown argument')

    def close(self):
        print(f'Resource was closed')
        self.opened = False

    def __del__(self):
        if self.opened:
            print('Memory leak detected! Resource was not closed')

    def action(self):
        print(self.arg)



def successful_closure(): # Успешное закрытие дескриптора по окончанию работы с ним
    resource = Resource()
    resource.open('w+ doing something')
    resource.action()
    resource.close()

def unsuccessful_closure(): # Неуспешное закрытие дескриптора по окончанию работы с ним
    resource = Resource()
    resource.open('w+ doing something')
    raise ValueError('Какая то ошибка')
    resource.close()

def try_except_open(): # Обработка в надежной конструкции try/except
    resource = None
    try:
        resource = Resource()
        resource.open('r hello, world!')
        resource.action()
        resource.open('abracadabra') # Намеренный вызов исключения
    except: # Должны быть указаны конкретные исключения
        raise
    finally:
        if resource: # Истинность означает открытие файла
            resource.close()

@contextmanager # Применение декоратора вместе с контекстным менеджером with для вызова
def contextmanager_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource # При задействии, возвращает значение в переменную псевдонима as
    except:
        raise
    finally:
        if resource:
            resource.close()

class ResourceWorker: # Применение класса для открытия файла.
    def __init__(self, *args):
        self.args = args
        self.resource = None # Аналогично проверке на истинность открытия файла выше

    def __enter__(self):
        # Метод, который вызывается при вхождении в контекстный менеджер with
        # Получение данных созданием объекта, на подобии выполнения блока try выше
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource # Вместо yield применяется обычное возвращение объекта для работы

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Аргументами являются: тип исключения, его значение и трейсбек. Если исключение не произойдет - все параметры станут иметь значение None. Если исключение произойдет - параметры станут иметь соответствующие им значения исключения
        # Метод, который вызывается при выходе из контекстного менеджера with
        # Совершение выхода, на подобии выполнения блока finally и except выше
        if self.resource:
            self.resource.close()


if __name__ == "__main__":
    with ResourceWorker('abracadabra') as res:
        res.action()
        raise ValueError
