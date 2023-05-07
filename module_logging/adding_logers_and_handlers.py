'''Создание новых обработчиков и логгеров для дополнения файла конфигураций.py

В данной реализации изменяются только значения переменной импортированного файла

Описание:
- Существует некое приложение app42. Для него определен логгер, с уровнем DEBUG и обработчик, который логирует данные
    в консоль. Требуется внести новый обработчик, который станет сохранять данные в одноименный с приложением файл.
- Также, существует некое приложение app69. Для него не определено логирование. Требуется создать логгер и определить
    для него два обработчика, которые станут выполнять работу, эквивалентную для первого приложения, т.е. логировать
    данные в одноименный с приложением файл и в консоль.
'''

import logging.config
from module_logging.two_logger import LOGGING_CONFIG

print(' Импортированный файл конфигураций расширяется, для внесения нового функционала '.center(120, '-'))
print('Для логирования приложения app42, в файле конфигураций уже существует логгер, выводящий данные в консоль\n'
      'Для логирования приложения в файл, создается обработчик file_handler_app42, сохраняющий логи в одноименный с '
      'приложением файл.\n'
      'В файле конфигураций, обработчик будет добавлен в словарь обработчиков и в логгер приложения')
print('В результате, для логгера app42 станут задействованы два обработчика. При регистрировании события:\n'
      'console_handler станет логировать данные в консоль, а file_handler_app42 логировать данные в файл app42.log\n')

print('Создание обработчика file_handler_app42 и его добавление в словарь всех обработчиков файла конфигураций')
LOGGING_CONFIG['handlers'].update({
    "file_handler_app42": {
        "class": "logging.FileHandler",
        "level": "DEBUG",
        "filename": "C:/GoogleDrive/Python/module_logging/app42.log",
        "formatter": "formatter_1",
    },
})
print('Добавление строкового идентификатора обработчика в список обработчиков словаря логгер app42 файла конфигураций')
LOGGING_CONFIG['loggers']['app42']['handlers'].append('file_handler_app42')
print()

print('Применение файла конфигураций')
logging.config.dictConfig(LOGGING_CONFIG)
print()

print('Определение логгера app42 в текущем модуле и применение для него соответствующих настроек из файла конфигураций')
app42 = logging.getLogger('app42')
app42.info('Info message from application app42')
print()

print(' Импортированный файл конфигураций расширяется, для внесения нового функционала '.center(120, '-'))
print('Для логирования приложения app69 создается соответствующий логгер.\n'
      'Для логирования приложения в файл, создается обработчик file_handler_app69, сохраняющий логи в одноименный с '
      'приложением файл.\n'
      'Для логирования приложения в консоль, применяется уже определенный в файле конфигураций обработчик '
      'console_handler')
print('В результате, для логгера app69 станут задействованы два обработчика, аналогично предыдущему приложению\n')

print('Создание логгера app69 и его добавление в словарь всех логгеров файла конфигураций')
LOGGING_CONFIG["loggers"].update({
    "app69": {
        "level": "DEBUG",
        "handlers": ["file_handler_app69", "console_handler"],
        "propagate": False
        }
    })
print('Создание обработчика file_handler_app69 и его добавление в словарь всех обработчиков файла конфигураций')
LOGGING_CONFIG["handlers"].update({
    "file_handler_app69": {
        "class": "logging.FileHandler",
        "level": "DEBUG",
        "filename": "C:/GoogleDrive/Python/module_logging/app69.log",
        "formatter": "formatter_1",
        }
    })
print('Применение файла конфигураций')
logging.config.dictConfig(LOGGING_CONFIG)
print()

print('Определение логгера app69 в текущем модуле и применение для него соответствующих настроек из файла конфигураций')
app69 = logging.getLogger('app69')
app69.info('Info message from application app69')
print()