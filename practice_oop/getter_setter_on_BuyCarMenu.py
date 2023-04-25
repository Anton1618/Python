'''Построение геттеров, сеттеров, композиции классов и задействие меню взаимодействия с созданным объектом

BuyCar - класс, отвечающий за характеристики создаваемого объекта автомобиля
get_price - геттер стоимости. Значение зависит от наличия скидки
set_discount - сеттер скидки. Значение, применяемое в геттере окончательной стоимости автомобиля
get_purchase_types - геттер способа оплаты. Метод класса, возвращающий доступные способы оплаты для объектов данного
класса. Применяется в инициализаторе, для проверки параметра "способа оплаты" и следовательно, возможности совершения
покупки

Car - объект автомобиль с рядом атрибутов для взаимодействия с его характеристиками
engine_on и engine_off - геттеры
'''


class BuyCar:
    PURCHASE_TYPES = ('LEASE', 'CASH')
    
    @classmethod
    def get_purchase_types(cls):
        return cls.PURCHASE_TYPES
    
    def __init__(self, maker, model, colour, price, gas_tank_volume, purchase_type):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price
        self.gas_tank_volume = gas_tank_volume
        if purchase_type not in BuyCar.PURCHASE_TYPES:
            raise ValueError(f'{purchase_type} is not a valid purchase')
        else:
            self.purchase_type = purchase_type

    def get_price(self):
        '''Геттер стоимости автомобиля.
        Изначально проверяет наличие скидки и если она присутствует, то возвращает соответствующую стоимость'''
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price

    def set_discount(self, amount):
        '''Сеттер скидки'''
        self._discount = amount

    def get_dataCar(self):
        '''Данные отправляемые в другой класс, при композиции объекта'''
        return self.maker, self.model, self.colour, self.price, self.gas_tank_volume


class Car:
    def __init__(self, maker, model, colour, price, gas_tank_volume, purchase_type='CASH'):
        self.maker, self.model, self.colour, self.price, self.gas_tank_volume, *_ = \
            BuyCar(maker, model, colour, price, gas_tank_volume, purchase_type).get_dataCar()
        self.condition = False
        self.refueling = 0

    def __repr__(self):
        return f'{self.maker}:id{id(self)%1000}'

    def __str__(self):
        return f'{repr(self)} {self.colour} colour, price {self.price}'

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

    def get_refueling(self):
        """Показатели количества топлива и заправленности"""
        return f'{self.refueling / self.gas_tank_volume:.2%}'

    def add_refueling(self, value):
        '''Пополнение бака топливом'''
        if value < 0:
            return 'Количество топлива для заправки не может быть отрицательным значением'
        if not self.refueling + value <= self.gas_tank_volume:
            return f'Бак будет переполнен {value}л топлива, уточните количество топлива и повторите'
        self.refueling += value
        print(f'Бак пополнен на {value}л бензина')
        return f'Заправленность: {self.get_refueling()}'

    def info(self):
        """Вывод комплектации текущего автомобиля"""
        print('Комплектация текущего автомобиля:')
        return (
            f'Название: {self.maker}\n'
            f'Модель: {self.model}\n'
            f'Цвет: {self.colour}\n'
            f'Объем бензобака: {self.gas_tank_volume}\n'
            f'Количество бензина: {self.refueling}\n'
            f'Заправленность: {self.get_refueling()}\n'
        )


if __name__ == '__main__':
    print(' Инициализация автомобиля '.center(120, '-'))
    print('Доступное совершение покупки автомобиля в лизинг')
    car1 = Car('BMW', 'i8', 'white', 50000, 2.3, 'LEASE')
    print(f'Приобретен в лизинг: {car1}')
    print()
    print('Недоступное совершение покупки автомобиля за криптовалюту')
    # car2 = Car('Mercedes', 'C-class', 'black', 28500, 2.3, 'CRYPT')
    # print(f'Приобретен за крипту: {car2}')
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
    #             getattr(car1, command)()
    #         else:
    #             print('Неизвестная команда, повторите')
    #     print()
