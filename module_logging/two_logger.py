LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "formatter_1": {
            "format": "%(name)s %(levelname)s %(asctime)s | %(message)s",
            "datefmt": "[%d.%m.%Y %H:%M:%S]"
        },
    },
    "handlers": {
        "console_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
            "formatter": "formatter_1",
        },
        # "file_handler_app69": {
        #     "class": "logging.FileHandler",
        #     "level": "DEBUG",
        #     "filename": "C:/GoogleDrive/Python/module_logging/app69.log",
        #     "formatter": "formatter_1",
        # },
    },
    "loggers": {
        "app42": {
            "level": "DEBUG",
            "handlers": ["console_handler"],
            "propagate": False
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console_handler"]
    }
}
