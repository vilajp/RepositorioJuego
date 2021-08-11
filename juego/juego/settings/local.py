from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'BDJUEGO',
        'Trusted_Connection': 'yes',
        'HOST': 'localhost\\SQLEXPRESS',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0',
        }
    }
}
