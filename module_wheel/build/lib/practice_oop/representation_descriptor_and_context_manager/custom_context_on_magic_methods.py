from representation_descriptor import DescriptorResource
class ContextManagerMethods:
    def __init__(self, *args):
        self.args = args
    def __enter__(self):
        self.resource = DescriptorResource()
        self.resource.open(*self.args)
        return self.resource
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()

if __name__ == '__main__':
    print('# Закрытие дескриптора, без возникновения ошибок')
    with ContextManagerMethods('file.txt', 'w+') as f:
        f.action()
    print()

    print('# Закрытие дескриптора, несмотря на возникновение ошибки')
    with ContextManagerMethods('file.txt', 'r+') as f:
        f.action()
        raise ValueError('Stop')
    print()