import string
from string_sequence import plus_str, plus_list
def test_string_sequence():
    assert plus_str('', chars= string.ascii_lowercase) == 'a'
    assert plus_str('zz', chars = string.ascii_lowercase) == 'aaa'
    assert plus_str('aaa', chars = string.ascii_lowercase) == 'aab'
    assert plus_str('$$', chars = '!@$') == '!!!'
    assert plus_list([], chars=string.ascii_lowercase) == ['a']
    assert plus_list(['$', '$'], chars='!@$') == ['!', '!', '!']