'''Логирование встроенным и пользовательским регистраторами

Логирование сообщений встроенным и пользовательским регистраторами.
Регистратор по умолчанию:
- Без изменений
Пользовательский регистратор:
Применяемые обработчики (Handlers)
- Обработчик FileHandler сохраняет выходные данные logger в файл my_log.log
- Обработчик StreamHandler направляет выходные данные logger в консоль

Демонстрация наследования настроек пользовательским логгером от встроенного
'''
import logging
import sys

print(' Логирование сообщений встроенным и пользовательским регистраторами '.center(120, '-'))
print('Создание пользовательского регистратора')
app42 = logging.getLogger('app42')
print()

print('Установка уровня логирования на DEBUG для этого конкретного логгера')
app42.setLevel(logging.DEBUG)
print()

print('Создание обработчиков')
print('Обработчик, который будет выводить сообщения в консоль')
console_handler = logging.StreamHandler(stream=sys.stdout)
print('Обработчик, который будет записывать сообщения в файл')
file_handler = logging.FileHandler('app42.log')
print()

print('Создание объекта форматера, который отформатирует выходные данные обработчика')
formatter = logging.Formatter('%(name)s %(levelname)s %(asctime)s | %(message)s',
                              datefmt='[%d.%m.%Y %H:%M:%S]')
print('Установка форматора в обработчики')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
print()

print('Добавление обработчиков в регистратор')
app42.addHandler(console_handler)
app42.addHandler(file_handler)
print()

print(' Логирование сообщений '.center(80, '-'))
print('Логирование сообщений регистратором по умолчанию')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')  # WARNING:root:This is a warning message
logging.error('This is an error message')  # ERROR:root:This is an error message
logging.critical('This is a critical message')  # CRITICAL:root:This is a critical message
logging.exception('This is an exception message')  # ERROR:root:This is an exception message
print()

print('Логирование сообщений пользовательским регистратором')
app42.debug('This is a debug message')  # app42 DEBUG [07.05.2023 15:12:01] | This is a debug message
app42.info('This is an info message')  # app42 INFO [07.05.2023 15:12:01] | This is an info message
app42.warning('This is a warning message')  # app42 WARNING [07.05.2023 15:12:01] | This is a warning message
app42.error('This is an error message')  # app42 ERROR [07.05.2023 15:12:01] | This is an error message
app42.critical('This is a critical message')  # app42 CRITICAL [07.05.2023 15:12:01] | This is a critical message
app42.exception('This is an exception message')  # app42 ERROR [07.05.2023 15:12:01] | This is an exception message
print('Также, благодаря хендлеру (обработчику) FileHandler, все эти сообщения будут сохранены в файл app42.log')
print()

print(' Демонстрация наследования настроек пользовательским логгером от встроенного '.center(120, '-'))
print('При создании пользовательского регистратора, он наследует настройки и обработчики от регистратора по умолчанию. '
      'Поэтому, если в регистраторе по умолчанию были настроены обработчики или уровень логирования, то они будут '
      'применяться и к пользовательскому регистратору.')
print()

print('Установка в корневом логгере уровня логирования INFO и задание форматора')
logging.basicConfig(level=logging.INFO, format='%(name)s %(levelname)s')
print()
print('Создание пользовательского логгера, наследующего настройки от базового')
app69 = logging.getLogger('app69')
print()

print('Применение встроенного логгера')
logging.debug('This is a debug message')  # (Проигнорирован)
logging.info('This is an info message')  # root INFO
logging.warning('This is a warning message')  # root WARNING

print('Применение пользовательского логгера')
app69.debug('This is a debug message')  # (Проигнорирован)
app69.info('This is an info message')  # app69 INFO
app69.warning('This is a warning message')  # app69 WARNING
