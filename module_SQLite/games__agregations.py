'''
# Создание, наполнение и агрегация БД `games.db`

## Состав
- Обновление состояния БД
- Простая сортировка записей о призовых фондах для каждой игры
- Группировка, подсчет числа дисциплин, получение суммы призового фонда и сортировка
- Группировка, сортировка, сумма и среднее
'''

import sqlite3 as sq
from practice_other.formatting import db_table_print

DB_PATH = 'module_SQLite/games.db'




print('Очистка БД предыдущей сессии...')
print('Сборка новой БД...')
with sq.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.executescript('''
                        DROP TABLE IF EXISTS games;
                        
                        CREATE TABLE games (
                            id INTEGER PRIMARY KEY,
                            date TEXT,
                            tournament TEXT,
                            game TEXT,
                            prize_fund INTEGER,
                            players TEXT,
                            status INTEGER
                        );
                        
                        INSERT INTO games (date, tournament, game, prize_fund, players, status)
                        VALUES ('20.03.2024', 'Elite League', 'Dota 2', 120000, '9Pandas', 1),
                            ('15.03.2024', 'ESL Challenger Jonköping 2024', 'CS2', 115000, 'NAVI', 0),
                            ('28.02.2024', 'WINLINE EPIC Standoff 2 Season 8', 'Standoff', 135000, 'Sentinels', 0),
                            ('18.02.2024', 'VALORANT Champions Tour 2024: Masters Madrid', 'Valorant', 80000, 'NAVI', 1),
                            ('18.02.2024', 'PGL Wallachia 2024: Season 1', 'Dota 2', 100000, 'Sentinels', 1),
                            ('18.02.2024', 'DreamLeague Season 23', 'Dota 2', 100000, '9Pandas', 1),
                            ('10.02.2024', 'DreamLeague Season 22', 'Dota 2', 75000, 'NAVI', 1);
                        ''')
print('\n' * 4)




print('===========================================================================')
print('Получение записей о призовых фондах для каждой игры, отсортированных по возрастанию размера фонда')
with sq.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.execute('''
                    SELECT game, prize_fund
                    FROM games
                    ORDER BY prize_fund
                    ''')
    columns = cursor.description
    data = cursor.fetchall()

# for d in data:
#     print(*d, sep=': ')
# print('\n' * 4)

db_table_print(columns, data, 50)



print('===========================================================================')
print('Получение числа дисциплин и суммы призового фонда по каждой из них, с группировкой по размеру суммы призового фонда в убывающем порядке')
with sq.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.execute('''
                    SELECT game, count(game) AS count, SUM(prize_fund) AS sum
                    FROM games
                    GROUP BY game
                    ORDER BY sum DESC
                    ''')
    columns = cursor.description
    data = cursor.fetchall()

# for d in data:
#     print(f'{d[0]} ({d[1]}): {d[2]}')
# print('\n' * 4)

db_table_print(columns, data, 50)



print('===========================================================================')
print('Группировка игроков, где каждая группа включает общую сумму призового фонда и среднее значение по нему, а также сортировку по его значению в убывающем порядке')
with sq.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.execute('''
                    SELECT players, ROUND(AVG(prize_fund)) AS avg, SUM(prize_fund) AS result
                    FROM games
                    GROUP BY players
                    ORDER BY result DESC
                    ''')

data = cursor.fetchall()
columns = [descr[0] for descr in cursor.description]
print("%10s   %10s   %10s ▼"%(*columns,))
print(40 * '-')
for num, d in enumerate(data):
    print("%10s | %10d | %10d"%(d[0], d[1], d[2]))
print('\n' * 4)
