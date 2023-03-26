from contextlib import contextmanager
from representation_descriptor import DescriptorResource

@contextmanager # Применение декоратора контекстного менеджера
def ContextManagerDecorator(*args):
    resource = None
    try:
        resource = DescriptorResource()
        resource.open(*args)
        yield resource # При задействии, возвращает значение в переменную псевдонима as
    except:
        raise
    finally:
        if resource:
            resource.close()

if __name__ == '__main__':
    print('# Успешное закрытие дескриптора')
    with ContextManagerDecorator('file.txt', 'w+') as res:
        res.action()
    print()

    print('# Закрытие дескриптора, несмотря на возникновение ошибки')
    with ContextManagerDecorator('file.txt', 'abracadabra') as res:
        res.action()
    print()