from contextlib import contextmanager


@contextmanager # Применение декоратора контекстного менеджера
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
