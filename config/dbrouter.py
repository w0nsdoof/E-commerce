import random
from django.db.utils import OperationalError
from django.db import connections

class ReadWriteRouter:
    def db_for_read(self, model, **hints):
        # Simple round-robin read strategy
        try:
            return random.choice(['default', 'replica'])
        except OperationalError:
            return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'