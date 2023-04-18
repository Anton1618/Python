class Car_showroom:
    car_count = 0
    default_name = None
    default_brand = None
    default_gasoline = 0
    default_gas_tank_volume = 0

    @staticmethod
    def default_info():
        """Вывод стандартной комплектации автомобиля у диллера"""
        return f"""Стандартная комплектация автомобиля: 
        Стандартное имя: {Car_showroom.default_name}
        Стандартный бренд: {Car_showroom.default_brand}
        Стандартное наличие топлива: {Car_showroom.default_gasoline}
        Стандартный объем топливного бака: {Car_showroom.default_gas_tank_volume}
        """

    def __init__(self, name="c200", brand="mercedes", model=2008, gasoline=0, gas_tank_volume=1.5):
        """Сборка автомобиля"""
        Car_showroom.car_count += 1
        self.name = name
        self.brand = brand
        self.model = model
        self.gasoline = gasoline
        self.gas_tank_volume = gas_tank_volume
        self.engine_condition = False

    def refueling_car(self):
        """Заправка автомобиля"""
        refueling = self.gasoline / self.gas_tank_volume * 100
        return refueling

    def info(self):
        """Вывод комплектации текущего автомобиля по категориям"""
        dct_info = {
"Название": self.name,
"Бренд": self.brand,
"Модель": self.model,
"Количество бензина": self.gasoline,
"Объем бензобака": self.gas_tank_volume,
"Заправленность": str(self.refueling_car()) + "%",
"Стоп": "stop"
        }
        print(*dct_info.keys(), sep='\n')
        while (val := input(f"""Введите категорию, которая вас интересует: """)) != "Стоп":
            if val in dct_info.keys():
                print(dct_info[val])

    def refilling_the_car(self, val):
        """Заправка автомобиля"""
        if val <= self.gas_tank_volume:
            self.gasoline += val
            print(f"Бак заправлен на {val}л бензина. Автомобиль заправлен на {self.refueling_car()}%")
        else:
            print("*Заправщик качает головой*",
                  " - Напокупали машин, а не знают даже, какой у них объем бака", sep="\n")

    def engine_start(self):
        """Включение зажигания"""
        if self.engine_condition is False:
            print("""*Двигатель автомобиля мелодично заурчал*""")
            self.engine_condition = True
        else:
            print("""*Двигатель автомобиля включен и не может быть заведен еще раз*""")

    def engine_stop(self):
        """Выключенbие зажигания"""
        if self.engine_condition is True:
            self.engine_condition = False
        else:
            print("*Двигатель автомобиля выключен и не может быть еще раз выключен")



car = Car_showroom()
while (command := input(f"""
Действия с машиной
default_info - {Car_showroom.default_info.__doc__}
info - {car.info.__doc__}
refilling_the_car - {car.refilling_the_car.__doc__}
engine_start - {car.engine_start.__doc__}
engine_stop - {car.engine_stop.__doc__}
Что необходимо сделать: """)) != "stop":
    if command in dir(car):
        print(eval(f'{car}.{command}()'))

