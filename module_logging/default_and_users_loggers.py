'''Логирование встроенным и пользовательским регистраторами

Встроенный регистратор:


Пользовательский регистратор:
Применяемые обработчики (Handlers)
- Обработчик FileHandler сохраняет выходные данные logger в файл my_log.log
- Обработчик StreamHandler направляет выходные данные logger в консоль
'''
import logging
import sys

print('Создание пользовательского регистратора - логгер для приложения42'.center(80, '-'))
logger = logging.getLogger('app42')
print()

print('Установка уровня логирования на DEBUG для этого конкретного логгера')
logger.setLevel(logging.DEBUG)
print()

print('Создание обработчиков')
print('Обработчик, который будет выводить сообщения в консоль')
console_handler = logging.StreamHandler(stream=sys.stdout)
print('Обработчик, который будет записывать сообщения в файл')
file_handler = logging.FileHandler('app42.log')
print()

print('Добавление обработчика к регистратору')
logger.addHandler(console_handler)
logger.addHandler(file_handler)
print()

print('Создание объекта форматера, который отформатирует выходные данные обработчика')
formatter = logging.Formatter('%(name)s %(levelname)s %(asctime)s | %(message)s',
                              datefmt='[%d.%m.%Y %H:%M:%S]')
print()

print('Установка форматора для обработчиков')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
print()

print(' Логирование сообщений '.center(80, '-'))
print('Логирование сообщений регистратором по умолчанию')
print('При создании пользовательского регистратора, он наследует настройки и обработчики от регистратора по умолчанию. '
      'Поэтому, если в регистраторе по умолчанию были настроены обработчики или уровень логирования, то они будут '
      'применяться и к пользовательскому регистратору.')
logging.debug('This is a debug message')  # DEBUG:app42:This is a debug message
logging.info('This is an info message')  # INFO:app42:This is an info message
logging.warning('This is a warning message')  # WARNING:app42:This is a warning message
logging.error('This is an error message')  # ERROR:app42:This is an error message
logging.critical('This is a critical message')  # CRITICAL:app42:This is a critical message
logging.exception('This is an exception message')  # ERROR:app42:This is an exception message
logging.log(logging.DEBUG, logging.debug, 'This is a debug message')
print()

print('Логирование сообщений пользовательским регистратором')
logger.debug('This is a debug message')  # app42 DEBUG [07.05.2023 15:12:01] | This is a debug message
logger.info('This is an info message')  # app42 INFO [07.05.2023 15:12:01] | This is an info message
logger.warning('This is a warning message')  # app42 WARNING [07.05.2023 15:12:01] | This is a warning message
logger.error('This is an error message')  # app42 ERROR [07.05.2023 15:12:01] | This is an error message
logger.critical('This is a critical message')  # app42 CRITICAL [07.05.2023 15:12:01] | This is a critical message
logger.exception('This is an exception message')  # app42 ERROR [07.05.2023 15:12:01] | This is an exception message
logger.log(logging.DEBUG, logging.debug, 'This is a debug message')  # ?
print('Также, благодаря хендлеру (обработчику) FileHandler, все эти сообщения будут сохранены в файл app42.log')
print()
