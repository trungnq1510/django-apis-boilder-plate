# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
from .base import config

# DATABASES = {
#     'default': {
#         'ENGINE'       : 'django.db.backends.mysql',
#         'NAME'         : config.get("database", "name"),
#         'USER'         : config.get("database", "user"),
#         'PASSWORD'     : config.get("database", "password"),
#         'HOST'         : config.get("database", "host"),
#         'CONN_MAX_AGE' : 600, # timeout for persistent connection
#     },
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

