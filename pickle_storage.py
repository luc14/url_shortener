import pickle, os
from base_storage import ObjectExistsError, ObjectNotFoundError

class PickleStorage:
    def __init__(self, path):
        '''create a storage if path doesn't exist
        '''
        self.path = path
        if not os.path.exists(path):
            storage = {}
            with open(self.path, 'wb') as f:
                pickle.dump(storage, f, 0)

    def _load(self):
        return pickle.load(open(self.path, 'rb'))

    def _dump(self, storage):
        with open(self.path, 'wb') as f:
            pickle.dump(storage, f, 0)

    def create_obj(self, obj):
        '''create a new dictionary with name obj in storage if it doesn't exist;
        Otherwise raise ObjectExistsError
        '''
        storage = self._load()
        if obj in storage:
            raise ObjectExistsError
        storage[obj] = {}
        self._dump(storage)

    def write(self, obj, key, value):
        '''Write key and value into obj in the storage if obj exists and value is not None;
        Raise ObjectNotFoundError if obj doesn't exist;
        Raise ValueError if value is None
        '''
        storage = self._load()
        if obj not in storage:
            raise ObjectNotFoundError
        if value is None:
            raise ValueError
        storage[obj][key] = value
        self._dump(storage)

    def read(self, obj, key):
        '''Return obj[key] from storage if obj exists; otherwise raise ObjectNotFoundError
        '''
        storage = self._load()
        if obj not in storage:
            raise ObjectNotFoundError
        return storage[obj].get(key)


