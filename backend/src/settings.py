import os
_basedir = os.path.abspath(os.path.dirname(__file__))

FLASK_ENV = 'development'
DEBUG = True

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

DATABASES = {
    'sqlalchemy': {
        'drivername': 'postgres',
        'host': 'map_db',
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
