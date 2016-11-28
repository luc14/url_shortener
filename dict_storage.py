from base_storage import ObjectExistsError, ObjectNotFoundError
class DictStorage:
    def __init__(self):
        self._storage = {}

    def create_obj(self, obj):
        '''create a new dictionary with name obj in storage if it doesn't exist;
        Otherwise raise ObjectExistsError
        '''
        if obj in self._storage:
            raise ObjectExistsError
        self._storage[obj] = {}

    def write(self, obj, key, value):
        '''Write key and value into obj in the storage if obj exists and value is not None;
        Raise ObjectNotFoundError if obj doesn't exist;
        Raise ValueError if value is None
        '''
        if obj not in self._storage:
            raise ObjectNotFoundError
        if value is None:
            raise ValueError
        self._storage[obj][key] = value

    def read(self, obj, key):
        '''Return obj[key] from storage if obj exists; otherwise raise ObjectNotFoundError
        '''
        if obj not in self._storage:
            raise ObjectNotFoundError
        return self._storage[obj].get(key)