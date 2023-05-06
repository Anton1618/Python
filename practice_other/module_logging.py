'''Логирование обработчиками (Handlers)

- Обработчик FileHandler сохраняет выходные данные logger в файл my_log.log
- Обработчик StreamHandler направляет выходные данные logger в консоль
'''
import logging

logger = logging.getLogger(__name__)

# Установка уровня логирования на DEBUG для этого конкретного логгера
logger.setLevel(logging.DEBUG)

# Создание обработчиков
# Обработчик, который будет выводить сообщения в консоль
console_handler = logging.StreamHandler()
# Обработчик, который будет записывать сообщения в файл
file_handler = logging.FileHandler('app42.log')

# Создание объекта форматера, который отформатирует выходные данные обработчика
formatter = logging.Formatter('%(name)s %(levelname)s %(asctime)s - %(message)s',
                              datefmt='[%d.%m.%Y %H:%M:%S]')

# Добавление обработчика к регистратору
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Установка форматора для обработчиков
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Логирование сообщений
logger.debug('This is a debug message')  # __main__ DEBUG [06.05.2023 01:13:31] - This is a debug message
logger.info('This is an info message')  # __main__ INFO [06.05.2023 01:13:31] - This is an info message
logger.warning('This is a warning message')  # __main__ WARNING [06.05.2023 01:13:31] - This is a warning message
logger.error('This is an error message')  # __main__ ERROR [06.05.2023 01:13:31] - This is an error message
logger.critical('This is a critical message')  # __main__ CRITICAL [06.05.2023 01:13:31] - This is a critical message
logger.exception('This is a exception message')  # __main__ CRITICAL [06.05.2023 01:13:31] - This is a critical message
# Также, благодаря хендлеру (обработчику) FileHandler, все эти сообщения будут сохранены в файл my_log.log
