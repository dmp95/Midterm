import os
import logging.config

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
LOG_FILE = os.getenv('LOG_FILE', 'app.log')

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'standard',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': LOG_LEVEL,
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
