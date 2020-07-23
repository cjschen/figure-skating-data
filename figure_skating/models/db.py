
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from figure_skating.models import base

import os
import sys

class Singleton:
    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

@Singleton
class DB:
    session = None
    
    def __init__(self):
        engine = create_engine(os.environ['DATABASE_URL'])

        if 'drop' in sys.argv:
            base.Base.metadata.drop_all(engine)

        base.Base.metadata.create_all(engine)

        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

