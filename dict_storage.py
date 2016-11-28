class ObjectExistsError(Exception):
    pass

class ObjectNotFoundError(Exception):
    pass

class DictStorage:
    def __init__(self, *args):
        self._storage = {}

    def create_obj(self, obj):
        if obj in self._storage:
            raise ObjectExistsError
        self._storage[obj] = {}

    def write(self, obj, key, value):
        self._storage[obj][key] = value

    def read(self, obj, key):
        return self._storage[obj].get(key)