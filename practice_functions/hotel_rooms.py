'''
# Задача
Распределяйте клиентов по гостиничным номерам в зависимости от дней их прибытия и отъезда.
Каждому клиенту нужна отдельная комната, поэтому два клиента могут остановиться в одной комнате только в том случае, если день отъезда первого клиента наступает раньше дня прибытия второго клиента.
Количество используемых комнат должно быть сведено к минимуму.


## Поступающие данные
Список или массив из n клиентов, 1 <= n <= 1000.
Каждый клиент представлен числами (`день_прибытия`, `день_отправления`), которые являются положительными целыми числами, удовлетворяющими условию `день_прибытия` <= n <= `день_отправления`.
Список клиентов не обязательно упорядочен по времени прибытия.


## Выход
Список или массив n-размера, где элемент i указывает номер, который был выделен клиенту i.
Комнаты пронумерованы 1,2,...,k для некоторого 1 <= k <= n.
Любое распределение, которое минимизирует количество комнат k, является допустимым решением.


## Пример
Предположим, что клиенты — это [(1,5), (2,4), (6,8), (7,7)].
Очевидно, что клиенты 1 и 2 не могут получить один и тот же номер.
Клиент 3 может использовать комнату в качестве любого из них, поскольку они оба уходят до прибытия клиента 3. 
Тогда клиенту 4 можно будет предоставить другую комнату.
Таким образом, любое из [1,2,1,2], [1,2,2,1], [2,1,2,1], [2,1,1,2] является допустимым решением.
'''

def allocate_clients_to_rooms(randays):
    '''Функция распределения клиентов по номерам'''
    rooms = {1: set()}
    res = []
    randays = [set(range(array[0], array[1]+1)) for array in randays]

    for client_days in randays:  # Размещение клиента
        available_room = None
        for room, booked_days in rooms.items():
            if not booked_days & client_days:
                available_room = room
                break

        if available_room is None:
            available_room = max(rooms.keys()) + 1
            rooms[available_room] = set()  # Подготовка нового номера (Аллокация)
        
        rooms[available_room] |= client_days  # Бронирование номера через приращение новых значений
        res.append(available_room)
    
    for n, date in enumerate(randays):
        print(f'Номер: {res[n]}. Бронь: {date}')
    print(f'Список задействованных номеров: {res}')
    print('\n\n')
    return res




# # Оптимизация кода для больших нагрузок ЭФФЕКТИВНОСТЬ НЕ ДОКАЗАНА НА CODEWARS
# В основной части алгоритма используется heapq.heappop для получения наиболее подходящей комнаты и heapq.heappush для ее обновления после размещения клиента

# - OrderedDict для хранения комнат
# Для быстрого поиска и сохранения порядка комнат.
# Для хранения комнат в порядке их добавления и обеспечения быстрой вставки и поиска
# - Приоритетная очередь (heapq)
# Для поддержания комнат в порядке, что позволяет быстро находить минимально занятые комнаты.
# Используется heapq для поддержания комнат в порядке, где комнаты с минимально занятыми днями имеют приоритет при новой проверке.
# Это помогает быстро находить и обновлять соответствующие комнаты.


# from collections import OrderedDict
# import heapq

# def allocate_rooms(randays):
#     # Преобразуем диапазоны дней клиентов в множества дней
#     randays = [set(range(array[0], array[1]+1)) for array in randays]
    
#     # Структура данных для хранения комнат и займ в порядке их добавления
#     rooms = OrderedDict({1: set()})
#     res = []
    
#     # Приоритетная очередь для хранения свободных комнат
#     available_rooms = [(0, 1)]  # (количество занятых дней, номер комнаты)
#     room_count = 1  # Счетчик для новых комнат

#     for client_days in randays:
#         placed = False
        
#         while available_rooms:
#             # Получить комнату с минимально занятым количеством дней
#             _, room = heapq.heappop(available_rooms)
            
#             # Проверить, можно ли разместить клиента в этой комнате
#             if not rooms[room] & client_days:
#                 rooms[room] |= client_days
#                 res.append(room)
                
#                 # Снова поместить комнату в очередь с обновлённой занятостью
#                 heapq.heappush(available_rooms, (len(rooms[room]), room))
#                 placed = True
#                 break
        
#         if not placed:
#             # Если ни одна существующая комната не подходит, создаем новую комнату
#             room_count += 1
#             rooms[room_count] = client_days
#             res.append(room_count)
#             heapq.heappush(available_rooms, (len(client_days), room_count))

#     return res



if __name__ == '__main__':
    assert allocate_clients_to_rooms([(1,2),(2,4),(4,4)]) == [1,2,1]  # or [2,1,2]
    assert allocate_clients_to_rooms([(1,5),(2,4),(6,8),(7,7)]) == [1,2,1,2]  # or any from [1,2,2,1], [2,1,2,1], [2,1,1,2]]
    assert allocate_clients_to_rooms([(15,22),(2,4),(6,9),(3,33),(12,21)]) == [1, 1, 1, 2, 3]  # or any from [1,2,2,3,2], [2,1,1,3,1], [3,1,3,2,1]
    assert allocate_clients_to_rooms([(1,10),(2,5),(6,6),(3,7),(6,6),(11,13),(9,15),(8,14)]) == [1, 2, 2, 3, 4, 1, 2, 3]  # or any from [1,2,2,3,4,1,3,2] [1,2,2,3,4,1,2,3], [1,2,4,3,2,1,3,2], [2,3,3,1,4,2,1,3]
    assert allocate_clients_to_rooms([(8,8),(5,8),(8,9),(1,4),(1,3),(5,7),(4,8),(2,2),(4,5),(6,8)]) == [1, 2, 3, 1, 2, 1, 4, 3, 3, 5]  # or [4, 1, 5, 1, 2, 4, 2, 3, 3, 3], [5, 4, 2, 2, 1, 2, 3, 3, 1, 1]


    print('\n\n✅ Все тесты пройдены')
