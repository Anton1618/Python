'''
# Создание и наполнение `sales.db`

## Состав
- DATA: словарь объектов, включающий все изначальные объекты для составления таблиц и генерации продаж
- Создание таблиц: сотрудники, клиенты, товары. Наполнение их данными из словаря объектов
- Создание таблицы продаж и её наполнение объединением данных из нескольких таблиц
    - Автоматическая генерация и добавление 80 продаж
    - Составление и добавление продаж вручную
- Получение и просмотр части записей таблицы sales
'''

import sqlite3
import random
from practice_other import formatting

DB_PATH = 'module_SQLite/sales.db'

DATA = {
    'employee_names': [
        'Прохор Овчинников',
        'Назар Русаков',
        'Эмилия Куликова',
        'Кондрат Комаров',
        'Трифон Прохоров',
        'Фаина Белозерова'
    ],

    'employee_salaries': [72000, 12000, 80000, 150000, 65000, 110000],

    'employees_departments': ['hr', 'sales', 'sales', 'develop', 'marketing', 'sales'],

    'customer_names': [
        'Мария Бобылева',
        'Устин Носов',
        'Светлана Назарова',
        'Анастасия Капустина',
        'Николай Зуев',
        'Лавр Хохлов',
        'Николай Плесецкий',
        'Петр Мамонов',
        'Лариса Звонарева',
        'Максим Лещенко',
        'Савелий Муров',
        'Екатерина Привольнова',
        'Зинаида Дерибатьковна',
        'Елизавета Сургина',
        'Григорий Паводин'
    ],

    'customer_mails': [
        'marya_lapochka@hotmail.com',
        'Ustinos86@gmail.com',
        'svet87nazarova@yandex.ru',
        'nasteanastea@yahoo.com',
        'kilyanchik@gmail.com',
        'LavredHohlov@mail.ru',
        'nickolay_koya9812@yahoo.com',
        'petrec_best@gmail.com',
        'zvonareva_larisa@mail.ru',
        'maksvaks02@yandex.ru',
        'fighterbomba@gmail.com',
        'cvetochekpusya@yahoo.com',
        'zindza1985@gmail.com',
        'kotenokmarusya@gmail.com',
        'povodin@hotmail.com',
    ],

    'product_titles': [
        'Смарт-часы Xiaomi Redmi Watch 4 Silver Gray BHR7848GL (X51488)',
        'Смарт-часы Huawei Watch Fit 2 Active Edition Midnight Black (YDA-B09S)',
        'Смарт-часы Apple Watch Series 9 41mm Starlight Aluminium Case with Starlight Sport Band, размер M/L (MR8U3)',

        'Смартфон Google Pixel 7 8/256GB Black',
        'Смартфон Honor Magic 6 Pro 12/512GB Green',
        'Смартфон Xiaomi 14 Ultra 16/512GB Black',

        'Планшет Huawei MatePad 11 2023 DBR-W19 8/128GB Wi-Fi + Pencil Graphite Black (53013VCN)',
        'Планшет Xiaomi Redmi Pad SE 4/128GB Gray (49283)',
        'Планшет Huawei MatePad SE 4+64GB LTE Black (AGS5-L09)',
        'Планшет Honor Pad X8 4+64GB LTE Blue (AGM3-AL09DHN)',
        'Планшет Oppo Pad Air 128GB Grey (OPD2102A)',

        'Наушники True Wireless HUAWEI FreeBuds SE 2 T0016 White',
        'Наушники Apple AirPods Pro 2nd generation MagSafe Case USB-C (MTJV3)',
        'Наушники Apple AirPods 2nd generation with Charging Case (MV7N2)',
        'Наушники True Wireless HUAWEI Freebuds 5i Nebula Black (T0014)',
    ],

    'product_prices': [
        10000, 8000, 46000, 
        61000, 110000, 15000, 
        36000, 16000, 15000, 12700, 25000, 
        2499, 28999, 14499, 5499
    ],

    'product_characteristics': [
        'Смарт-часы Xiaomi Redmi Watch 4 Silver Gray BHR7848GL (X51488) оборудованы сенсорным экраном диагональю 1,97 дюйма. AMOLED-матрица обеспечивает высокую детализацию и реалистичность цвета. Устройство воспроизводит изображение с разрешением 390х450 пикселей. Яркость дисплея составляет 600 кд/м2. Это позволяет комфортно пользоваться часами даже в солнечный день. Модель оборудована специальными датчиками, которые фиксируют количество шагов, уровень кислорода в крови, ЧСС и фазы сна.',
        'Смарт-часы HUAWEI Watch Fit 2 Active Edition Midnight Black (YDA-B09S) оптимальны для использования взрослыми и подростками. В конструкции модели есть модуль Bluetooth. За счет этого удобно осуществлять беспроводную синхронизацию устройства с мобильным телефоном. Смарт-часы оснащены динамиком и микрофоном, что позволяет использовать модель для ответа на входящие вызовы. Встроенный шагомер, пульсометр, счетчик калорий и пульсоксиметр помогают контролировать показатели организма во время спортивных тренировок. Для спутниковой навигации есть системы ГЛОНАСС и GPS.',
        'Смарт-часы Apple Watch Series 9 GPS 41mm Starlight Aluminium Case with Starlight Sport Band M/L оборудованы чипом S9 SiP, который обеспечивает высокую производительность, общесистемные улучшения и новые функциональные возможности. Четырехъядерный нейронный процессор способен мгновенно обрабатывать задачи машинного обучения. Благодаря высокой энергоэффективности и емкому аккумулятору модель до 18 ч работает автономно в активном режиме.',

        None,
        None,
        'Камера HONOR Falcon второго поколения с технологиями AI. Не упустите ни одной волнующей секунды. Технология «Захват движения» поможет автоматически сфотографировать решающий момент и сохранить на память лучшие кадры.',

        None,
        'Планшет HUAWEI MatePad 11 2023 DBR-W19 8/128GB Wi-Fi + Pencil Graphite Black (53013VCN) имеет сенсорный широкоформатный экран с IPS-матрицей, которая исключает искажение цветов и очертаний объектов при воспроизведении. Процессор с графическим ускорителем обеспечивает быстродействие системы при обработке запросов. Для хранения файлов используется встроенная память значительного объема. Для воспроизведения мелодий и голосов предусмотрены встроенные динамики.',
        'Планшет Xiaomi Redmi Pad SE 4/128GB Gray (49283) на платформе Android оборудован процессором Qualcomm Snapdragon 680 с максимальной тактовой частотой 2,4 ГГц, оперативной памятью размером 4 Гб, встроенным накопителем емкостью 128 Гб и опцией расширения объема данных за счет использования карт памяти microSD до 1 Тб. Металлический корпус серого цвета обладает высоким качеством и прочностью, надежно защищая устройство от повреждений и продлевая срок службы. Экран типа TFT IPS диагональю 11" и разрешением 1920х1200 пикс выдает четкое, насыщенное изображение и обеспечивает точное взаимодействие с сенсорной поверхностью.',
        None,
        'Планшет OPPO Pad Air 128GB Grey (OPD2102A) оснащен восьмиядерным процессором, который обеспечивает высокий уровень производительности. Благодаря оптимальному объему оперативной памяти устройство способно молниеносно запускать ресурсоемкие приложения и переключаться между задачами. Вывод изображения осуществляется на экран TFT IPS. К преимуществам технологии относятся реалистичная передача цвета, широкий угол обзора, яркость и контрастность.',

        'Наушники True Wireless Huawei FreeBuds SE 2 T0016 выполнены в пластиковом белом корпусе. Отличаются легкостью и компактностью, вес — 97 г. Встроена функция быстрой зарядки, система активного подавления шума. Воспроизведение аудио от аккумулятора емкостью 41 мА*ч происходит в течение 40 ч.',
        'Наушники Apple AirPods Pro (MTJV3) — модель типа вкладыши в корпус из пластика, амбушюры сделаны из силикона. Благодаря стандарту IPX4 модель не боится попадания воды. Девайс поддерживает опцию беспроводного соединения с источником звука за счет наличия встроенного Bluetooth-адаптера версии 5.3. Радиус действия работы достигает 10 м, что дает возможность свободно перемещаться по квартире без смартфона в руке. Управление параметрами производится посредством сенсорной панели.',
        'Наушники Apple AirPods with Charging Case (MV7N2) синхронизируются с источником звука с помощью модуля Bluetooth версии 5 с дальностью действия до 45 м. Гарнитура обеспечивает быстрый доступ к голосовому помощнику Siri, поддерживает Live-прослушивание и быструю зарядку в футляре.\nЭта модель оборудована сдвоенными направленными микрофонами, передающими речь без помех и искажений. На корпусе расположены кнопки управления воспроизведением. На одном заряде аккумулятора наушники работают до 5 часов. В комплекте — кабель с коннекторами Apple Lightning — USB Type-A.',
        'Наушники True Wireless Huawei Freebuds 5i Nebula Black (T0014) поставляются с тремя парами силиконовых насадок разного размера. Амбушюры позволяют выбрать наиболее комфортный вариант и обеспечивают максимальное прилегание к ушной раковине. Динамики диаметром 10 мм отвечают за воспроизведение объемного звука.'
    ],

    'product_categories': [
        'Смарт часы', 'Смарт часы', 'Смарт часы',
        'Смартфоны', 'Смартфоны', 'Смартфоны',
        'Планшеты', 'Планшеты', 'Планшеты', 'Планшеты', 'Планшеты',
        'Наушники', 'Наушники', 'Наушники', 'Наушники'
    ],

    'product_brands': [
        'Xiaomi', 'HUAWEI', 'Apple',
        'Google', 'Honor', 'Xiaomi',
        'HUAWEI', 'Xiaomi', 'HUAWEI', 'Honor', 'Oppo',
        'HUAWEI', 'Apple', 'Apple', 'HUAWEI'
    ],
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
            category TEXT,
            brand TEXT
        );
        CREATE TABLE sales (
            title TEXT,
            price INTEGER,
            customer TEXT,
            manager TEXT,
            category TEXT,
            brand TEXT
        );
        ''')

    cursor.executemany('''
        INSERT INTO employees (name, salary, department)
        VALUES (?, ?, ?)
    ''', list(zip(DATA['employee_names'], DATA['employee_salaries'], DATA['employees_departments'])))

    cursor.executemany('''
        INSERT INTO customers (name, mail)
        VALUES (?, ?)
    ''', list(zip(DATA['customer_names'], DATA['customer_mails'])))

    cursor.executemany('''
        INSERT INTO product (title, characteristics, price, category, brand)
        VALUES (?, ?, ?, ?, ?)
    ''', list(zip(DATA['product_titles'], DATA['product_characteristics'], DATA['product_prices'], DATA['product_categories'], DATA['product_brands'])))




# ===========================================================================
# Автоматическое генерирование продаж из объектов словаря данных
with sqlite3.connect(DB_PATH) as con:
    cursor = con.cursor()

    for _ in range(80):
        r_manager = random.choice([1, 2, 5])  # Случайный сотрудник отдела продаж
        r_customer = random.choice(range(len(DATA['customer_names'])))
        r_prod = random.randint(0, len(DATA['product_titles'])-1)  # Случайный товар из набора товаров

        # Каждая продажа включает в себя наименование, стоимость, категорию товара и бренд, а также покупателя и менеджера
        gen_sales = [DATA['product_titles'][r_prod], DATA['product_prices'][r_prod], DATA['customer_names'][r_customer], DATA['employee_names'][r_manager], DATA['product_categories'][r_prod], DATA['product_brands'][r_prod]]
        cursor.execute('''
            INSERT INTO sales (title, price, customer, manager, category, brand)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', gen_sales)




# ===========================================================================
# Ручное составление продаж, через объединение данных из трех разных таблиц
with sqlite3.connect(DB_PATH) as con:
    cursor = con.cursor()

    # Каждая продажа включает в себя наименование, стоимость, категорию товара и бренд, а также покупателя и менеджера
    QUERY_INSERT_INTO = '''INSERT INTO sales (title, price, customer, manager, category, brand)'''

    # ============ Проверка наличия данных в таблицах.
    # Если хотя бы одно из указанных условий не выполнится, то запрос SELECT не вернёт результатов, а вставка в таблицу sales не произойдет
    # Например
    # SELECT * FROM product WHERE p.ROWID = 7").fetchall()  # Будет производиться взятие значение товара по столбцу title, но уточняющим критерием WHERE станет являться значение столбца ROWID
    # SELECT * FROM customers WHERE name = 'Анастасия Капустина'").fetchall()  # Будет производиться взятие значения имени покупателя по столбцу name. Уточняющий критерий совпадает со значением по столбцу name
    # SELECT * FROM employees WHERE name = 'Эмилия Куликова'").fetchall()  # Будет производиться взятие значения имени продавца по столбцу name. Уточняющий критерий совпадает со значением по столбцу name

    # ============ Продажа №1
    SALE1 = '''
        SELECT
            p.title,
            p.price,
            c.name,
            e.name,
            p.category,
            p.brand
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
            e.name,
            p.category,
            p.brand
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
    SALE3 = '''
        SELECT
            p.title,
            p.price,
            c.name,
            e.name,
            p.category,
            p.brand
        FROM
            product p,
            customers c,
            employees e
        WHERE
            p.rowid = 8 AND
            c.name = 'Анастасия Капустина' AND
            e.name = 'Назар Русаков'
        '''
    cursor.execute(QUERY_INSERT_INTO + SALE3)




print('\n\n===========================================================================')
print('Получение и просмотр 10 записей таблицы sales\n')
with sqlite3.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.execute('''SELECT * FROM sales''')

    data = cursor.fetchall()[:10]
    columns = cursor.description

    formatting.db_table_print(columns, data, 120)
    print('\n')
