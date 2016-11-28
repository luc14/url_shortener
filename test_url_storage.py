import pytest
from url_storage import URLStorage

def test_url_storage(tmpdir):
    with pytest.raises(KeyError):
        url_storage = URLStorage({'type':'pickle'}, 'http://localhost:5000')
    path = str(tmpdir.join('url_storage'))
    long_url = 'https://www.youtube.com/watch?v=E6iN6VTL7v8&ab_channel=AvoidatAllCosts'
    url_storage = URLStorage({'type':'pickle', 'path': path}, 'http://localhost:5000')
    assert url_storage.get_long(url_storage.get_short(long_url)) == long_url

