'''Построение композиции из взаимодействия классов для создания объекта автомобиля

Класс Constructor - класс конструктора автомобиля.
Применяется как сторонний механизм, не связанный с логикой остальных классов.

Класс DealerCar - класс, реализующий покупку автомобиля.
Проверяет данные на корректность.
Отправляет запрос в Constructor на создание автомобиля.
Вносит дополнительные атрибуты, сравнимые с получением чека.

Car - класс пользователя, как результат покупки, через который осуществляется передача данных для их обработки в
последующих классах. Предоставляет атрибуты для взаимодействия с автомобилем
'''
from datetime import datetime


class Constructor:
    def __init__(self, maker, model, **kwargs):
        self.maker = maker
        self.model = model
        self.construct_time = datetime.now()
        self.identifier = id(self) % 1000
        self.colour = kwargs['colour'] if kwargs.get('colour') else 'white'
        self.gas_tank_volume = kwargs['gas_tank_volume'] if kwargs.get('gas_tank_volume') else 2.0


class DealerCar:
    '''Класс, реализующий дилера, продающего автомобили'''
    PURCHASE_TYPES = ('LEASE', 'CASH')
    MAKER = ('BMW', 'Nissan', 'Mercedes')

    @classmethod
    def get_purchase_types(cls):
        return cls.PURCHASE_TYPES

    def __init__(self, maker, model, price, purchase_type, **kwargs):
        if maker not in self.__class__.MAKER:
            raise ValueError(f'{maker} not available at the moment')
        self.maker = maker
        if not purchase_type or purchase_type not in self.__class__.PURCHASE_TYPES:
            raise ValueError(f'{purchase_type} should be one of {self.__class__.PURCHASE_TYPES}')
        self.purchase_type = purchase_type
        self.price = price - (price * kwargs['discount']) if kwargs.get('discount') else price
        self.model = model
        self.dealer_car = Constructor(self.maker, self.model, **kwargs)

    def sale(self):
        self.dealer_car.price = self.price
        self.dealer_car.purchase_type = self.purchase_type
        self.dealer_car.sale_time = datetime.now()
        return self.dealer_car


class Car:
    '''Класс результирующего объекта автомобиля с атрибутами для взаимодействия'''
    def __init__(self, maker, model, price, purchase_type='CASH', **kwargs):
        car = DealerCar(maker, model, price, purchase_type, **kwargs).sale()
        self.maker = getattr(car, 'maker')
        self.model = getattr(car, 'model')
        self.price = getattr(car, 'price')
        self.purchase_type = getattr(car, 'purchase_type')
        self.colour = getattr(car, 'colour')
        self.gas_tank_volume = getattr(car, 'gas_tank_volume')
        self.construct_time = getattr(car, 'construct_time')
        self.identifier = getattr(car, 'identifier')
        self.condition = False
        self.gasoline = 0

    def __repr__(self):
        return f'{self.maker}:id{self.identifier}'

    def __str__(self):
        return f'{repr(self)} | color: {self.colour}, price: {self.price}'

    def engine_on(self):
        if self.condition:
            return 'Нельзя запустить уже запущенный двигатель'
        self.condition = True
        return 'Двигатель запущен'

    def engine_off(self):
        if not self.condition:
            return 'Нельзя заглушить уже заглушенный двигатель'
        self.condition = False
        return 'Двигатель заглушен'

    def refueling(self):
        """Показатели количества топлива и заправленности"""
        return f'{self.gasoline / self.gas_tank_volume:.2%}'

    def add_refueling(self, value):
        '''Пополнение бака топливом'''
        if value < 0:
            return 'Количество топлива для заправки не может быть отрицательным значением'
        if not self.gasoline + value <= self.gas_tank_volume:
            return f'Бак будет переполнен {value}л топлива, уточните количество топлива и повторите'
        self.gasoline += value
        print(f'Бак пополнен на {value}л бензина')
        return f'Заправленность: {self.refueling()}'

    def info(self):
        """Вывод текущей комплектации автомобиля"""
        print('Комплектация текущего автомобиля:')
        return (
            f'Название: {self.maker}\n'
            f'Модель: {self.model}\n'
            f'Цвет: {self.colour}\n'
            f'Объем бензобака: {self.gas_tank_volume}\n'
            f'Количество бензина: {self.gasoline}\n'
            f'Заправленность: {self.refueling()}\n'
        )


if __name__ == '__main__':
    print(' Инициализация автомобилей и вывод данных по ним '.center(120, '-'))
    car1 = Car('BMW', 'i8', 50000, 'LEASE', colour='white', gas_tank_volume=3.5)
    print(f'Приобретен в лизинг: {car1}')
    car2 = Car('Nissan', 'j10', 24300, 'CASH', colour='green', gas_tank_volume=2.0)
    print(f'Приобретен за наличные: {car2}')
    # car3 = Car('Mercedes', 'C-class', 28500, 'CRYPT', 'black', 2.5)
    # print(f'Приобретен за крипту: {car3}')
    print()

    print(' Различные операции с автомобилем '.center(120, '-'))
    print('Получение информации об автомобиле')
    print(car1.info())
    print('Заправка автомобиля')
    print(car1.add_refueling(4))
    print(car1.add_refueling(2))
    print()
    print('Запуск и выключение двигателя')
    print(car1.engine_on())
    print(car1.engine_on())
    print(car1.engine_off())
    print(car1.engine_off())
    print()



    # print('Автомобильное меню услуг:')
    # while (command := input(
    #                     'Доступные действия:\n'
    #                     f'info - {car1.info.__doc__}\n'
    #                     f'add_refueling - {car1.add_refueling.__doc__}\n'
    #                     f'engine_on - {car1.engine_on.__doc__}\n'
    #                     f'engine_off - {car1.engine_off.__doc__}\n'
    #                     'Ваше действие: ')) != "stop":
    #     if command in dir(car1):
    #         if hasattr(car1, command):
    #             hasattr(car1, command)()
    #         else:
    #             print('Неизвестная команда, повторите')
    #     print()
