import pytest, os
from pickle_storage import ObjectExistsError, PickleStorage, ObjectNotFoundError

##@pytest.mark.parametrize(('storage'), [[DictStorage()], [PickleStorage('coffee.pickle')]])
#@pytest.mark.parametrize(('storage_class, filename'), [(DictStorage, None), (PickleStorage, 'coffee.pickle')])
#def test_storage(storage_class, filename):
    #storage = storage_class(filename)
    #storage.create_obj('coffee_bene')
    #assert not storage.read('coffee_bene', 'tea')
    #storage.write('coffee_bene', 'tea', 'orange_dulce')
    #assert storage.read('coffee_bene', 'tea')=='orange_dulce'
    #with pytest.raises(ObjectExistsError):
        #storage.create_obj('coffee_bene')
    #if filename:
        #assert os.path.exists(filename)


def test_persistence(tmpdir):
    path = str(tmpdir.join('coffee.pickle'))
    assert not os.path.exists(path)
    storage = PickleStorage(path)
    assert os.path.exists(path)
    with pytest.raises(ObjectNotFoundError):
        storage.write('coffee_bene', 'tea', None)
    with pytest.raises(ObjectNotFoundError):
        storage.read('coffee_bene', 'tea')
    storage.create_obj('coffee_bene')

    with pytest.raises(ValueError):
        storage.write('coffee_bene', 'tea', None)

    assert storage.read('coffee_bene', 'tea') is None
    storage.write('coffee_bene', 'tea', 'orange_dulce')
    assert storage.read('coffee_bene', 'tea')=='orange_dulce'
    storage = PickleStorage(path)
    with pytest.raises(ObjectExistsError):
        storage.create_obj('coffee_bene')
    assert storage.read('coffee_bene', 'tea')=='orange_dulce'
