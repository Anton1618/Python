'''
# Агрегирование данных `sales.db`

## Состав
- Cтоимость товаров
    - 10 наиболее дорогих товаров из всех категорий
    - Общая выручка по каждой группе товаров, начиная с наибольшей
    - 3 наиболее дорогих марки товаров из категории "Смартфоны"
    - 3 наиболее дорогих товара из каждой категории (из таблицы товаров)

- Результаты по продавцам
    - Сумма продаж, их число и среднее значение по выручке для каждого продавца
    - Сумма продаж и их число по каждому продавцу в категории "Смартфоны"

- Число продаж товаров
    - 10 наиболее популярных товаров из всех
    - 2 наименее популярных марки товаров в категории "Планшеты"
    - 3 наиболее популярные марки товаров
'''

import sqlite3 as sq
import pandas as pd
from practice_other.formatting import pretty_header

DB_PATH = 'module_SQLite/sales.db'
SEP = '======'
SEP_GAP2N = '\n\n' + SEP
GAP4N = '\n\n\n\n'




pretty_header('Cтоимость товаров')
with sq.connect(DB_PATH) as con:
    print(SEP)
    print('10 наиболее дорогих товаров из всех категорий')
    query = '''
        SELECT DISTINCT title, price, category
        FROM sales
        ORDER BY price DESC
        LIMIT 10
    '''
    print(pd.read_sql_query(query, con))


    print(SEP_GAP2N)
    print('Общая выручка по каждой группе товаров, начиная с наибольшей')
    query = '''
        SELECT category, SUM(price) AS amount
        FROM sales
        GROUP BY category
        ORDER BY amount DESC
    '''
    print(pd.read_sql_query(query, con))


    print(SEP_GAP2N)
    print('3 наиболее дорогих марки товаров из категории "Смартфоны"')
    query = '''
        SELECT DISTINCT brand, title, price
        FROM sales
        WHERE category == 'Смартфоны'
        ORDER BY price DESC
        LIMIT 3
    '''
    print(pd.read_sql_query(query, con))


    print(SEP_GAP2N)
    print('3 наиболее дорогих товара из каждой категории (из таблицы товаров)')
    query = '''
        WITH RankedSales AS (
        SELECT DISTINCT
            title,
            price,
            category,
            brand,
            ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS rank
        FROM product
        )
        SELECT
            title,
            price,
            category,
            brand
        FROM RankedSales
        WHERE rank <= 3
        ORDER BY category, price DESC;
    '''
    print(pd.read_sql_query(query, con))




print(GAP4N)
pretty_header('Результаты по продавцам')
with sq.connect(DB_PATH) as con:
    print(SEP)
    print('Сумма продаж, их число и среднее значение по выручке для каждого продавца')
    query = '''
        SELECT
            manager,
            SUM(price) AS sales_amount,
            COUNT(title) AS sales_count,
            ROUND(AVG(price)) AS sales_average
        FROM sales
        GROUP BY manager
        ORDER BY sales_amount DESC
    '''
    print(pd.read_sql_query(query, con))


    print(SEP_GAP2N)
    print('Сумма продаж и их число по каждому продавцу в категории "Смартфоны"')
    query = '''
        SELECT manager, COUNT(title) AS sales_count, SUM(price) AS sales_amount
        FROM sales
        WHERE category == 'Смартфоны'
        GROUP BY manager
        ORDER BY sales_amount DESC
    '''
    print(pd.read_sql_query(query, con))




print(GAP4N)
pretty_header('Число продаж товаров')
with sq.connect(DB_PATH) as con:
    print(SEP)
    print('10 наиболее популярных товаров')
    query = '''
        SELECT title, COUNT(title) AS product_count
        FROM sales
        GROUP BY title
        ORDER BY product_count DESC
        LIMIT 10
    '''
    print(pd.read_sql_query(query, con))


    print(SEP_GAP2N)
    print('2 наименее популярных марки товаров в категории "Планшеты"')
    query = '''
        SELECT brand, COUNT(title) AS product_count
        FROM sales
        WHERE category = 'Планшеты'
        GROUP BY brand
        ORDER BY product_count
        LIMIT 2
    '''
    print(pd.read_sql_query(query, con))


    print(SEP_GAP2N)
    print('3 наиболее популярные марки товаров')
    query = '''
        SELECT brand, COUNT(title) AS product_count
        FROM sales
        GROUP BY brand
        ORDER BY product_count DESC
        LIMIT 3
    '''
    print(pd.read_sql_query(query, con))
