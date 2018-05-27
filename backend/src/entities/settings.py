DATABASES = {
    'sqlalchemy': {
        'drivername': 'postgres',
        'host': 'HOST',
        'port': 'PORT',
        'username': 'USERNAME',
        'password': 'PASSWORD',
        'database': 'DATABASENAME',
    },
}


try:
    from .local_settings import *
except Exception:
    try:
        from local_settings import *
    except ImportError:
        pass
