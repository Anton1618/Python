'''
Применение значений из сторонней таблицы


'''

import sqlite3

DB_PATH = 'module_SQLite/use_data_from_other_db.db'

DATA = {
    'employees name': ['Прохор Овчинников',
                'Назар Русаков',
                'Эмилия Куликова',
                'Кондрат Комаров',
                'Трифон Прохоров',
                'Фаина Белозерова'],
    
    'employees salary': [72000, 12000, 80000, 150000, 65000, 110000],

    'employees department': ['hr', 'sales', 'sales', 'develop', 'marketing', 'sales'],

    'customer name': ['Мария Бобылева',
                'Устин Носов',
                'Светлана Назарова',
                'Анастасия Капустина',
                'Николай Зуев',
                'Лавр Хохлов',
                'Николай Плесецкий',
                'Петр Мамонов',
                'Лариса Звонарева'],

    'customer mail': ['Dallin86@gmail.com',
                'Kale87@gmail.com',
                'Madge_Toy@yahoo.com',
                'Suzanne_Lynch@hotmail.com',
                'Rhoda_Lockman60@gmail.com',
                'Clare45@gmail.com'],
    
    'product title': ['Смарт-часы Xiaomi Redmi Watch 4 Silver Gray BHR7848GL (X51488)',
                'Смарт-часы Huawei Watch Fit 2 Active Edition Midnight Black (YDA-B09S)',
                'Смарт-часы Apple Watch Series 9 41mm Starlight Aluminium Case with Starlight Sport Band, размер M/L (MR8U3)',
                'Смартфон Google Pixel 7 8/256GB Black',
                'Смартфон Honor Magic 6 Pro 12/512GB Green',
                'Смартфон Xiaomi 14 Ultra 16/512GB Black',
                'Планшет Huawei MatePad 11 2023 DBR-W19 8/128GB Wi-Fi + Pencil Graphite Black (53013VCN)',
                'Планшет Xiaomi Redmi Pad SE 4/128GB Gray (49283)',
                'Планшет Huawei MatePad SE 4+64GB LTE Black (AGS5-L09)',
                'Планшет Honor Pad X8 4+64GB LTE Blue (AGM3-AL09DHN)',
                'Планшет Oppo Pad Air 128GB Grey (OPD2102A)'],

    'product price': [10000, 8000, 46000, 61000, 110000, 15000, 36000, 16000, 15000, 12700, 25000],

    'product characteristics': ['Смарт-часы Xiaomi Redmi Watch 4 Silver Gray BHR7848GL (X51488) оборудованы сенсорным экраном диагональю 1,97 дюйма. AMOLED-матрица обеспечивает высокую детализацию и реалистичность цвета. Устройство воспроизводит изображение с разрешением 390х450 пикселей. Яркость дисплея составляет 600 кд/м2. Это позволяет комфортно пользоваться часами даже в солнечный день. Модель оборудована специальными датчиками, которые фиксируют количество шагов, уровень кислорода в крови, ЧСС и фазы сна.',
                        'Смарт-часы HUAWEI Watch Fit 2 Active Edition Midnight Black (YDA-B09S) оптимальны для использования взрослыми и подростками. В конструкции модели есть модуль Bluetooth. За счет этого удобно осуществлять беспроводную синхронизацию устройства с мобильным телефоном. Смарт-часы оснащены динамиком и микрофоном, что позволяет использовать модель для ответа на входящие вызовы. Встроенный шагомер, пульсометр, счетчик калорий и пульсоксиметр помогают контролировать показатели организма во время спортивных тренировок. Для спутниковой навигации есть системы ГЛОНАСС и GPS.',
                        'Смарт-часы Apple Watch Series 9 GPS 41mm Starlight Aluminium Case with Starlight Sport Band M/L оборудованы чипом S9 SiP, который обеспечивает высокую производительность, общесистемные улучшения и новые функциональные возможности. Четырехъядерный нейронный процессор способен мгновенно обрабатывать задачи машинного обучения. Благодаря высокой энергоэффективности и емкому аккумулятору модель до 18 ч работает автономно в активном режиме.',
                        '!$@',
                        'Камера HONOR Falcon второго поколения с технологиями AI. Не упустите ни одной волнующей секунды. Технология «Захват движения» поможет автоматически сфотографировать решающий момент и сохранить на память лучшие кадры.',
                        '$-!',
                        'Планшет HUAWEI MatePad 11 2023 DBR-W19 8/128GB Wi-Fi + Pencil Graphite Black (53013VCN) имеет сенсорный широкоформатный экран с IPS-матрицей, которая исключает искажение цветов и очертаний объектов при воспроизведении. Процессор с графическим ускорителем обеспечивает быстродействие системы при обработке запросов. Для хранения файлов используется встроенная память значительного объема. Для воспроизведения мелодий и голосов предусмотрены встроенные динамики.',
                        'Планшет Xiaomi Redmi Pad SE 4/128GB Gray (49283) на платформе Android оборудован процессором Qualcomm Snapdragon 680 с максимальной тактовой частотой 2,4 ГГц, оперативной памятью размером 4 Гб, встроенным накопителем емкостью 128 Гб и опцией расширения объема данных за счет использования карт памяти microSD до 1 Тб. Металлический корпус серого цвета обладает высоким качеством и прочностью, надежно защищая устройство от повреждений и продлевая срок службы. Экран типа TFT IPS диагональю 11" и разрешением 1920х1200 пикс выдает четкое, насыщенное изображение и обеспечивает точное взаимодействие с сенсорной поверхностью.',
                        '&$!',
                        'Планшет OPPO Pad Air 128GB Grey (OPD2102A) оснащен восьмиядерным процессором, который обеспечивает высокий уровень производительности. Благодаря оптимальному объему оперативной памяти устройство способно молниеносно запускать ресурсоемкие приложения и переключаться между задачами. Вывод изображения осуществляется на экран TFT IPS. К преимуществам технологии относятся реалистичная передача цвета, широкий угол обзора, яркость и контрастность.'],
    
    'product category': ['Смарт часы', 'Смарт часы', 'Смарт часы', 'Смартфоны', 'Смартфоны', 'Смартфоны', 'Планшеты', 'Планшеты', 'Планшеты'],
}




print('Очистка БД предыдущей сессии...')
print('Сборка новой БД...')
with sqlite3.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.executescript(
        '''
        DROP TABLE IF EXISTS employees;
        DROP TABLE IF EXISTS customers;
        DROP TABLE IF EXISTS product;
        DROP TABLE IF EXISTS sales;

        CREATE TABLE employees (
            name TEXT,
            salary INTEGET,
            department TEXT
        );
        CREATE TABLE customers (
            name TEXT,
            mail TEXT
        );
        CREATE TABLE product (
            title TEXT,
            characteristics TEXT,
            price INTEGER,
            category TEXT
        );
        CREATE TABLE sales (
            title TEXT,
            price INTEGER,
            customer TEXT,
            manager TEXT
        );
        ''')

    cursor.executemany('''
        INSERT INTO employees (name, salary, department)
        VALUES (?, ?, ?)
    ''', list(zip(DATA['employees name'], DATA['employees salary'], DATA['employees department'])))

    cursor.executemany('''
        INSERT INTO customers (name, mail)
        VALUES (?, ?)
    ''', list(zip(DATA['customer name'], DATA['customer mail'])))

    cursor.executemany('''
        INSERT INTO product (title, characteristics, price, category)
        VALUES (?, ?, ?, ?)
    ''', list(zip(DATA['product title'], DATA['product characteristics'], DATA['product price'], DATA['product category'])))
print('\n')



# ===========================================================================
# Объединение данных из трех разных таблиц, для создания записи о продаже в текущей таблице sales
with sqlite3.connect(DB_PATH) as con:
    cursor = con.cursor()


    # Каждая продажа включает в себя наименование товара, покупателя и менеджера
    QUERY_INSERT_INTO = '''INSERT INTO sales (title, price, customer, manager)'''

    # ============ Проверка наличия данных в таблицах. Если хотя бы одно из указанных условий не выполнится, то запрос SELECT не вернёт результатов, а вставка в таблицу sales не произойдет
    # SELECT * FROM product WHERE p.ROWID = 7").fetchall()  # Будет производиться взятие значение товара по столбцу title, но уточняющим критерием WHERE станет являться значение столбца ROWID
    # SELECT * FROM customers WHERE name = 'Анастасия Капустина'").fetchall()  # Будет производиться взятие значения имени покупателя по столбцу name. Уточняющий критерий совпадает со значением по столбцу name
    # SELECT * FROM employees WHERE name = 'Эмилия Куликова'").fetchall()  # Будет производиться взятие значения имени продавца по столбцу name. Уточняющий критерий совпадает со значением по столбцу name

    SALE1 = '''
        SELECT
            p.title,
            p.price,
            c.name,
            e.name
        FROM
            product p,
            customers c,
            employees e
        WHERE
            p.rowid = 7 AND
            c.name = 'Анастасия Капустина' AND
            e.name = 'Эмилия Куликова'
        '''
    cursor.execute(QUERY_INSERT_INTO + SALE1)

    # ============ Продажа №2
    SALE2 = '''
        SELECT
            p.title,
            p.price,
            c.name,
            e.name
        FROM
            product p,
            customers c,
            employees e
        WHERE
            p.rowid = 3 AND
            c.name = 'Светлана Назарова' AND
            e.name = 'Назар Русаков'
        '''
    cursor.execute(QUERY_INSERT_INTO + SALE2)

    # ============ Продажа №3
    SALE2 = '''
        SELECT
            p.title,
            p.price,
            c.name,
            e.name
        FROM
            product p,
            customers c,
            employees e
        WHERE
            p.rowid = 8 AND
            c.name = 'Анастасия Капустина' AND
            e.name = 'Назар Русаков'
        '''
    cursor.execute(QUERY_INSERT_INTO + SALE2)




print('===========================================================================')
print('Получение сводной таблицы по результатам продаж')
with sqlite3.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.execute('''
        SELECT * FROM sales

    ''')
    print('\n')









    print('===========================================================================')
    print('Получение всех записей таблицы sales')
    cursor.execute('''SELECT * FROM sales''')
    data = cursor.fetchall()
    columns = cursor.description

    for line in data:
        print(f'Элемент:')
        for val in line:
            print(val)
        print()
    print('\n')
