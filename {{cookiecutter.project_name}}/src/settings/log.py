import logging.config
from os.path import join
from .base import config

LOGFILE_ROOT = config.get("apps", "logfile_root")
MAX_BYTES = 10485760

LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        "request_id": {
            "()": "request_id.logging.RequestIdFilter"
        }
    },
    'formatters': {
        'json': {
            '()': 'drf_json_logging.json_logging.JsonFormatter',
            'fmt': '%(name)s %(levelno)s %(levelname)s %(pathname)s %(filename)s %(module)s %(lineno)d %(funcName)s '
                   ' %(asctime)s %(message)s %(request_id)s',
        }
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(LOGFILE_ROOT, 'project.log'),
            'maxBytes': MAX_BYTES,  # 5 MB
            'backupCount': 7,
            'formatter': 'json',
            'filters': ['request_id'],
        }
    },
    'loggers': {
        'src': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'drf_json_logging': {
            'handlers': ['proj_log_file'],
            'level': "DEBUG",
        },
    }
}

logging.config.dictConfig(LOGGING)