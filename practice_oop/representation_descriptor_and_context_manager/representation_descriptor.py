class DescriptorResource:
    database = 'Первоначальные данные'
    def __init__(self):
        self.opened = False

    def open(self, args):
        self.opened = True
        match args:
            case reading as r if r[1] in ('r', 'rb'):
                print()
                self.arg = f'Reading process... {" ".join(r)}'
            case writing as w if w[1] in ('w', 'x', 'wb'):
                self.arg = f'Writing process... {" ".join(r)}'
            case reading_and_writing as rw if rw[1] in ('r+', 'w+'):
                self.arg = f'Reading and writing... {" ".join(r)}'
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

# Успешное закрытие дескриптора по окончанию работы с ним
def successful_closure():
    resource = Resource()
    resource.open('w+ doing something')
    resource.action()
    resource.close()

# Дескриптор не был закрыт, при возникновении исключения
def unsuccessful_closure():
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
