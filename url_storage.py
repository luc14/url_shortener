import string, os
import string_sequence
from pickle_storage import PickleStorage

# another option is to ask user to create a storage instance and pass it to URLStorage
class URLStorage:
    chars = string.ascii_lowercase + string.digits

    def __init__(self, storage_info, domain):
        '''
        Args: storage_info: a dict like {'type': 'pickle', 'path': path}
        domain: a string

        If path is missing when storage_type is 'pickle', raise a PathNotFoundError
        '''
        self.domain = domain
        #if storage_type == 'dict':
            #self.storage = DictStorage()
        if storage_info['type'] == 'pickle':
            #add a method to create a new pickle file
            self.storage = PickleStorage(storage_info['path'])
        else:
            raise TypeError('unknown storage type')
        self.storage.create_obj('long_to_short')
        self.storage.create_obj('short_to_long')
        self.storage.create_obj('misc')

    def get_long(self, short_url):
        '''return a long url
        '''
        return self.storage.read(obj='short_to_long', key=short_url)

    def _create_new_short(self):
        last_short = self.storage.read(obj='misc', key='last_short')
        if not last_short:
            last_short = ''
        last_short = string_sequence.plus_str(last_short, self.chars)
        self.storage.write(obj='misc', key='last_short', value=last_short)
        return last_short

    def get_short(self, long_url):
        '''create a new short_url if the long_url doesn't exist in the storage;
        return short url

        '''
        short_url = self.storage.read(obj='long_to_short', key=long_url)
        if not short_url:
            short_url = self.domain + '/' +self._create_new_short()
            self.storage.write(obj='short_to_long', key=short_url, value=long_url)
            self.storage.write(obj='long_to_short', key=long_url, value=short_url)
        return self.storage.read(obj='long_to_short', key=long_url)
