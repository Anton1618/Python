pets = {
    1:
        {
            "Мухтар":
                {
                    "Вид питомца": "собака",
                    "Возраст питомца": 9,
                    "Имя владельца": "Павел"
                },
        },
    2:
        {
            "Каа":
                {
                    "Вид питомца": "желторотый питон",
                    "Возраст питомца": 19,
                    "Имя владельца": "Саша"
                },
        },
}


def create_id():
    """Определение нового идентификатора ID"""
    last_key = list(enumerate(pets))[-1][1]  # Последнее значение ключа
    all_array = range(last_key + 1)  # Формирование диапазона по последний ключ включительно
    actual_keys = pets.keys()  # Получение значений текущих ключей
    symmetric_difference = list(
        set(all_array) ^ set(actual_keys))  # Перевод в множества и получение симетрической разности
    if symmetric_difference:
        created = symmetric_difference[0]
    else:
        created = last_key + 1
    return created


def get_pet() -> (str, int, dict):
    """Запрашивает кличку животного и на его основе возвращает:
    Кличка животного - Переданное значение;
    ID питомца - Актуальный id по переданной кличке;
    Словарь питомца - {Вид питомца: '', Возраст питомца: int, Хозяин питомца: ''}
    """
    name = input("Введите кличку животного: ")
    actual_id = 0
    for i in pets.keys():
        if name in pets.setdefault(i):
            actual_id = i
    dct_animal = pets[actual_id][name] if actual_id in pets.keys() else False
    return name, actual_id, dct_animal


def read():
    """Вывести информацию о питомце"""
    name, actual_id, dct_animal = get_pet()
    kind_of_animal = dct_animal['Вид питомца']
    age = dct_animal['Возраст питомца']
    owner_name = dct_animal['Имя владельца']
    print(
        f"Это {kind_of_animal} по кличке {name}. Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner_name}")


def write_info():
    """Формирует и возвращает словарь {Кличка питомца: {Вид питомца: '', Возраст питомца: int, Хозяин питомца: ''}}"""
    # {1: {"name1": {"1": "a","11": "aa"},}, 2:{"name2": {"2": "b", "22": "bb"},},}                # Структура
    # {ID: {"---": {"Вид питомца": "---", "Возраст питомца": "---", "Имя владельца": "---"},},}    # Оформление
    welcome = ["Кличка животного", "Вид питомца", "Возраст питомца", "Имя владельца"]
    print("Пожалуйста внесите следующие сведения о вашем питомце")
    information = {
        input(f"{welcome[0]}: "):
            {
                welcome[1]: input(f"{welcome[1]}: "),
                welcome[2]: int(input(f"{welcome[2]}: ")),
                welcome[3]: input(f"{welcome[3]}: ")
            },
    }
    return information


def create():
    """Создавать новую запись о питомце"""
    pets.update({
        create_id():
            write_info()
    })


def update():
    """Обновить информацию о питомце"""
    name, actual_id, dct_animal = get_pet()
    update_info = {
        actual_id:
            write_info()
    }
    return pets.update(update_info)


def delete():
    """Удалить запись о питомце"""
    name, actual_id, dct_animal = get_pet()
    pets.pop(actual_id)
    print(f"Запись о {name} удалена")


def get_suffix(age):
    """Формирование суфикса для возраста"""
    age = int(age)
    simple_n = age % 10
    if age in (11, 12, 13, 14):
        return 'лет'
    elif simple_n == 0 or simple_n > 4:
        return 'лет'
    elif simple_n == 1:
        return 'год'
    else:
        return 'года'


def pets_list():
    """Отображение всей базы построчно"""
    for i in pets.keys():
        name = list(enumerate(pets[i], 1))[0][1]
        for key, val in pets[i][name].items():
            print({key}, {val}, end=" ")
        print()


def menu():
    while (commands := input(
            f"""
            Доступные программы
            create - {create.__doc__}
            read - {read.__doc__}
            update - {update.__doc__}
            delete - {delete.__doc__}
            stop - Для выхода из меню
            Введите название программы: """
    )) != "stop":
        if commands in globals():
            globals()[commands]()



menu()
