'''
Различные SQL-функций

- Создание БД для демонстрации
- Простая сортировка записей о призовых фондах для каждой игры
- Группировка, подсчет числа дисциплин, получение суммы призового фонда и сортировка
- Группировка, сортировка, сумма и среднее
'''

import sqlite3 as sq
from practice_functions.staff_functions import pretty_header, text_ellipsis

db_path = 'module_SQLite/game_matches.db'




descr1 = 'Очистка БД предыдущей сессии'

with sq.connect(db_path) as con:
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
print(text_ellipsis(descr1))




title1 = 'Получение записей о призовых фондах для каждой игры, отсортированных по возрастанию размера фонда'
with sq.connect(db_path) as con:
    cursor = con.cursor()

    cursor.execute('''
                    SELECT game, prize_fund
                    FROM games
                    ORDER BY prize_fund
                    ''')
    data = cursor.fetchall()

pretty_header(title1)
for d in data:
    print(*d, sep=': ')
print()




title2 = 'Получение числа дисциплин и суммы призового фонда по каждой из них, с группировкой по размеру суммы фонда по убыванию'
with sq.connect(db_path) as con:
    cursor = con.cursor()

    cursor.execute('''
                    SELECT game, count(game) AS count, SUM(prize_fund) AS sum
                    FROM games
                    GROUP BY game
                    ORDER BY sum DESC
                    ''')
    data = cursor.fetchall()

pretty_header(title2)
for d in data:
    print(f'{d[0]} ({d[1]}): {d[2]}')
print()




title3 = 'Группировка игроков, где каждая группа включает общую сумму призового фонда и среднее значение по нему, а также сортировку по его значению по убыванию'
with sq.connect(db_path) as con:
    cursor = con.cursor()

    cursor.execute('''
                    SELECT players, ROUND(AVG(prize_fund)) AS avg, SUM(prize_fund) AS result
                    FROM games
                    GROUP BY players
                    ORDER BY result DESC
                    ''')
    data = cursor.fetchall()
    columns = [descr[0] for descr in cursor.description]

    pretty_header(title3)
    print("%10s   %10s   %10s ▼"%(*columns,))
    print(40 * '-')
    for num, d in enumerate(data):
        print("%10s | %10d | %10d"%(d[0], d[1], d[2]))
