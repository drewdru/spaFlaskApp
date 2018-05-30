# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative

from src import settings

def db_connect():
    """ Performs database connection using database settings from settings.py.
        :return: sqlalchemy engine instance
    """
    # return create_engine('sqlite:///images.db', echo=True)
    return create_engine('{drivername}://{username}:{password}@{host}:{port}/{database}'\
        .format(**settings.DATABASES['sqlalchemy'])
    )

ENGINE = db_connect()
SESSION_MAKER = sessionmaker()

@as_declarative()
class Base(object):
    """ Base class for sqlalchemy models
    """
    def __init__(self):
        self.conn = ENGINE.connect()
        self.session = SESSION_MAKER(bind=self.conn)
        self.close()

    def open(self):
        self.conn = ENGINE.connect()
        self.session = SESSION_MAKER(bind=self.conn)

    def close(self):
        self.session.close()
        self.conn.close()
        ENGINE.dispose()
