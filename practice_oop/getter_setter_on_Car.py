'''Построение простых геттеров, сеттеров

get_price - геттер стоимости. Значение зависит от наличия скидки
set_discount - сеттер скидки. Значение, применяемое в геттере окончательной стоимости автомобиля
get_purchase_types - геттер способа оплаты. Метод класса, возвращающий доступные способы оплаты для объектов данного класса. Применяется в 
инициализаторе, для проверки параметра "способа оплаты" и следовательно возможности совершения покупки 
'''


class Car:
    PURCHASE_TYPES = ('LEASE', 'CASH')
    
    @classmethod
    def get_purchase_types(cls):
        return cls.PURCHASE_TYPES
    
    def __init__(self, maker, model, colour, price, purchase_type):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price
        if not purchase_type in self.__class__.PURCHASE_TYPES:
            raise ValueError(f'{purchase_type} is not a valid purchase')
        else:
            self.purches_type = purchase_type

    def __repr__(self):
        return f'{self.maker}:id{id(self)%1000}'
    def __str__(self):
        return f'{repr(self)} {self.colour} colour, price {self.get_price()}'

    def get_price(self):
        '''Геттер стоимости автомобиля.
        Изначально проверяет наличие скидки и если она присутствует, то возвращает соответствующую стоимость'''
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price

    def set_discount(self, amount):
        '''Сеттер скидки'''
        self._discount = amount


if __name__ == '__main__':
    car1 = Car('BMW', 'i8', 'white', 50000, 'LEASE')
    print(f'Инициализация автомобиля, приобритенного в лизинг: {car1}')
    # car2 = Car('Mercedes', 'C-class', 'black', 28500, 'CRYPT')
    # print(f'Попытка инициализации автомобиля, во время приобритенния за крипту: {car2}')
    print()