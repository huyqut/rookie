# LOGGING
# There are 5 levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
# Choose 1 level, it will only serve logging from that level to the right (above order)

import logging
import logging.config
from python_101.chap15_logging_other import *

# By default, the logging use append mode: 'a'
# To overwrite, add filemode = 'w'


def tradition():
    logging.basicConfig(filename = './data/chap15_log', filemode = 'w', level = logging.DEBUG)
    # Default is root logger
    logging.debug('This is a debug log')
    logging.info('This is an info log')
    logging.warning('This is a warning')
    logging.error('This is an error')
    logging.critical('This is a critical log')

    logex = logging.getLogger('ex')  # Create a logger named 'ex'

    try:
        raise Exception()
    except Exception as e:
        logex.exception(str(e))  # Print exception with trace back

    logger = logging.getLogger('roses')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('./data/chap15_multi')

    formatter = logging.Formatter('[%(asctime)s] %(name)s::%(levelname)s > %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.info('Mofo just started!!!')
    do_something()
    logger.info('Mofo just stopped')


def file_config():  # Error prone
    logging.config.fileConfig('./data/chap15_log_config')
    logger = logging.getLogger('roses')
    logger.info('Mofo just started!!!')
    do_something()
    logger.info('Mofo just stopped')

#file_config()

def dict_config():
    dictLogConfig = {
        "version": 1,
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": "./data/chap15_log_dictconf"
            }
        },
        "loggers": {
            "roses": {
                "handlers": ["fileHandler"],
                "level": "INFO",
            }
        },
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }
    logging.config.dictConfig(dictLogConfig)

    logger = logging.getLogger('roses')

    logger.info('Mofo just started!!!')
    do_something()
    logger.info('Mofo just stopped')

dict_config()
