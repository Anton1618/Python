bomb = '💣'
clean_zone = ['🌳', '🌿', '🌲', '🌱']


def collectionGenerator():
    from random import choice
    """Генератор игровой карты"""
    N = int(input('Введите количество строк: '))
    M = int(input('Введите количество столбцов: '))
    matrix = []
    for i in range(N):
        row = []
        for j in range(M):
            val = choice([*bomb, *clean_zone])
            row.append(val)
        matrix.append(row)
    return matrix

# Генерация игрового поля
collection = collectionGenerator()

# Игворое поле для отображения игроку. Изначально засекречено. При открытии элементов, они отображаются на карте
player_collection = [['*' for j in range(len(collection[i]))] for i in range(len(collection))]


def checkGameVal():
    player_score = sum([1 for i in player_collection for j in i if j in clean_zone])
    all_score = sum([1 for i in collection for j in i if j in clean_zone])
    win_score = all_score - player_score
    return win_score


def check(game_collection):
    """Вывод значений игрового поля"""
    st = '{:5}' * len(game_collection)
    for i in game_collection:
            print(st.format(*i))

def findVal(index_row, index_col):
    cir = correct_index_row = index_row - 1
    cic = correct_index_col = index_col -1
    result = player_collection[cir][cic] = collection[cir][cic]
    return result


status = 'Значение найденного элемента'
while status != bomb:
    check(player_collection)
    print('Ваш ход!')
    iir = incorrect_index_row = int(input('Введите номер строки: '))
    iic = incorrect_index_col = int(input('Введите номер столбца: '))
    status = findVal(iir, iic)
    if status == bomb:
        check(collection)
        print('Wasted')
    elif status != bomb:
        score = checkGameVal()
        if score < 1:
            status = bomb
            print('Winner!!!')
            check(collection)
else:
    print("Конец игры")