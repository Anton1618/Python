'''
Знакомство с SQLite

- Установка соединения с БД и пустой запрос
- Вариант с использованием контекстного менеджера
- Удаление таблицы
- Создание таблицы с несколькими столбцами
- Внесение данных в таблицу
- Применение различных методов для выполнения SQL-команд
- Изменение и удаление данных в записях
- Получение и сохранение данных из БД
'''

import sqlite3 as sq

DB_PATH = 'module_SQLite/scientists.db'



# ===========================================================================
# Установка соединения с БД и пустой запрос
# ============ Простой вариант, уязвимый к ошибке закрытия соединения
con = sq.connect('module_SQLite/scientists.db')  # Создание объекта соединения, для обеспечения доступа к БД и управления транзакциями
cur = con.cursor()  # Создание объекта курсора - интерфейса взаимодействия, для непосредственного выполнения SQL-запросов
cur.execute('')  # Выполнение команды
cur.close()  # Закрытие объекта курсора
con.close()  # Закрытие файлового дескриптора


# ============ Вариант с использованием контекстного менеджера, автоматически закрывающего соединение и курсор
with sq.connect('module_SQLite/scientists.db') as con:
    cur = con.cursor()
    cur.execute('')




# ===========================================================================
# Удаление таблицы (Оператор DROP + query)
# Удаление таблицы предыдущей сессии)
with sq.connect(DB_PATH) as con:
    cur = con.cursor()

    cur.execute('''DROP TABLE IF EXISTS scientists''')  # Дополнительная проверка IF EXISTS позволяет исключить ошибку, при которой таблица не существует




# ===========================================================================
#  Создание таблицы с несколькими столбцами (Оператор CREATE + query)
with sq.connect(DB_PATH) as con:
    cur = con.cursor()

    # Скрипты, при повторном выполнении, станут возвращать ошибку, потому как таблица уже будет существовать. Поэтому, конструкции в скрипте, создающем таблицу, обычно добавляется отрицательная проверка IF NOT EXISTS, для того, чтобы совершить указанное действие, только если таблица не существует
    cur.execute('''CREATE TABLE IF NOT EXISTS scientists (
                name TEXT DEFAULT anonim,
                sex INTEGER,
                date_of_born INTEGER,
                date_of_death INTEGER NOT NULL
                )''')
    # Применение констрейнтов позволяет создавать гибкие условия и форматы для хранения данных




# ===========================================================================
#  Внесение данных в таблицу (Оператор INSERT INTO + VALUES)
with sq.connect(DB_PATH) as con:
    cur = con.cursor()

    # Добавление одной записи, заполняя данные по определенным столбацам
    cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death)
                VALUES ('Джеймс Максвелл', 1, 1831, 1879)
                ''')
    
    # Добавление множества записей, заполняя данные по определенным столбацам, перечисляя значения оператора values через запятую
    cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death)
                VALUES ('Конрад Рентген', 1, 1845, 1923), ('Томас Эдисон', 1, 1847, 1931), ('Error', 'Error', 'Error', 'Error')
                ''')
    
    # Добавление одной или множества записей, без указания наименований столбцов, производя упорядоченное добавление данных во все соответствующие столбцы
    cur.execute('''INSERT INTO scientists
                VALUES ('Никола Тесла', 1, 1856, 1943)
                ''')




# ===========================================================================
#  Применение различных методов для выполнения SQL-команд
with sq.connect(DB_PATH) as con:
    cur = con.cursor()

    # ============ execute - метод для выполнения SQL-запроса с одним набором параметров
    # Применяется для разовой операции, например, создание таблицы, добавление или редактирование записей, но с применением только одного набора параметров
    # Запросы без параметров
    cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death)
                VALUES ('Макс Планк', 1, 1858, 1947)
                ''')
    
    cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death)
                VALUES ('Альберт Эйнштейн', 1, 1879, 1955), ('Энрико Ферми', 1, 1901, 1954)
                ''')


    # С применением набора параметров
    cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death)
                VALUES ('Лебедев Петр Николаевич', 1, 1866, ?)
                ''', (1912,))
    
    cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death)
                VALUES ('Эрнест Резерфорд', 1, ?, ?)
                ''', (1871, 1937))

    cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death)
                VALUES ('Игорь Васильевич Курчатов', 1, ?, ?), ('Нильс Бор', 1, ?, ?)
                ''', (1903, 1960, 1885, 1962))


    # ====== executemany - метод для выполнения SQL-запроса DML с каждым параметром из множества наборов параметров
    # Применяется для множественной вставки или обновления данных, с возможным применением множества наборов параметров
    # executemany - выполняет SQL-запрос для каждого переданного набора параметров
    new_scientists = [('Мария Кюри', 2, 1867, 1934), ('Александр Михайлович Прохоров', 1, 1916, 2002)]
    cur.executemany('''INSERT INTO scientists (name, sex, date_of_born, date_of_death) VALUES (?, ?, ?, ?)''', new_scientists)

    # Метод execute в таком случае менее эффективен, потому как для него потребуется задействие цикла, в котором на каждой итерации станет выполняться очередной SQL-запрос
    # for elm in new_scientists:
    #     cur.execute('''INSERT INTO scientists (name, sex, date_of_born, date_of_death) VALUES (?, ?, ?, ?)''', elm)




# ============================== Изменение и удаление данных в записях (Оператор UPDATE и DELETE)
with sq.connect(DB_PATH) as con:
    cur = con.cursor()

    # Установка нового значения в столбце name, для определенной записи с ROWID = 1 (первая запись в таблице)
    cur.execute('''UPDATE scientists
                SET name = 'Джеймс Клерк Максвелл'
                WHERE ROWID = 1
                ''')

    # Удаление записи по фильтрующему свойству WHERE, со значением 'Error' в столбце name
    cur.execute('''DELETE FROM scientists
                WHERE name = 'Error'
                ''')




# =============================== Получение и сохранение данных из БД (Оператор SELECT + методы чтения данных)
# Данные, собранные через запрос, можно получить, построчно проитерировав объект курсора, либо используя методы курсора: fetchone(), fetchall() или fetchmany(), но лишь один раз для каждого результата запроса в объекте курсора
with sq.connect(DB_PATH) as con:
    cur = con.cursor()

    # Итерирование полученных данных напрямую из объекта курсора
    data = cur.execute('''SELECT * FROM scientists''')  # Сохраняя результат запроса сразу в переменную
    all_rows1 = []  # Сохраняя рузультат построчно во время итерации данных
    for row in cur:
        all_rows1.append(row)
    

    # Получение всех данных из метода fetchall
    cur.execute('''SELECT * FROM scientists''')
    all_rows2 = cur.fetchall()


    # Для получения всех строк данных с помощью fetchone и fetchmany, необходимо продолжать вызывaть эти методы до тех пор, пока они не вернут None
    cur.execute('''SELECT * FROM scientists''')
    all_rows3 = []
    while (row:=cur.fetchone()):
        all_rows3.append(row)
    
    # При этом, методу fetchmany потребуется передать размер пакетов строк для обработки и сгладить полученный массив
    cur.execute('''SELECT * FROM scientists''')
    all_rows4 = []
    while (row:=cur.fetchmany(2)):
        for elm in row:
            all_rows4.append(elm)




if __name__ == '__main__':
    for num, query in enumerate((all_rows1, all_rows2, all_rows3, all_rows4), 1):
        print(f'query {num}:', query)
        print()
