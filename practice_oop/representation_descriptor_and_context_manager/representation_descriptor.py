class DescriptorResource:
    def __init__(self):
        self.opened = False
    def open(self, file, mode=None):
        if not mode: mode = 'r'
        self.opened = True
        match mode:
            case reading as r if r in ('r', 'rb'):
                self.arg = 'R'
            case writing as w if w in ('w', 'x', 'wb'):
                self.arg = 'W'
            case reading_and_writing as rw if rw in ('r+', 'w+'):
                self.arg = 'RW'
            case _:
                raise ValueError('Unknown argument')
    def close(self):
        print(f'Resource was closed')
        self.opened = False
    def __del__(self):
        if self.opened:
            print('Memory leak detected! Resource was not closed')
    def action(self):
        if self.arg == 'R':
            print('Reading process...')
        if self.arg == 'W':
            print('Writing process...')
        if self.arg == 'RW':
            print('Reading and writing process...')


def simple_handling(*args):
    '''Простая обработка дескриптора'''
    resource = DescriptorResource()
    resource.open(*args)
    resource.action()
    resource.close()

# Обработка дескриптора в конструкции try/except/finally для гарантированного закрытия дескриптора
def try_except_finally_handling(*args):
    '''Обработка дескриптора конструкцией try/except/finally'''
    resource = DescriptorResource()
    try:
        resource.open(*args)
        resource.action()
    except:
        raise
    finally:
        if resource:
            resource.close()

if __name__ == '__main__':
    print('# Небезопасная обработка дескриптора. Успешное закрытие дескриптора')
    simple_handling('file.txt')
    print()

    # print('# Небезопасная обработка дескриптора. Закрытие дескриптора небыло произведено')
    # simple_handling('file.txt', 'abracadabra')
    # print()

    print('# Успешное закрытие дескриптора, несмотря на возникновение ошибки в конструкции try/except/finally')
    try_except_finally_handling('file.txt', 'abracadabra')
    print()
