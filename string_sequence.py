import string

def plus_list_inplace(lst, chars):
    '''
    Args: lst is the currence string list in sequence;
    chars is iterable

    Modify lst to be the next list in sequence
    '''
    start = chars[0]
    end = chars[-1]
    plus_dict = {chars[i]: chars[i+1] for i in range(-1, len(chars)-1)}
    #chars_n = len(chars)
    #plus_dict = {chars[i]: chars[(i+1)%chars_n] for i in range(chars_n)}
    n = len(lst)

    def inner_plus(i):
        '''changes lst[:i] to be in sequence
        '''
        if i == 0:
            lst[0:0] = [start]
        elif lst[i-1] != end:
            lst[i-1] = plus_dict[lst[i-1]]
        else:
            lst[i-1] = start
            inner_plus(i-1)

    inner_plus(n)

def plus_list_inplace(lst, chars):
    start = chars[0]
    end = chars[-1]
    plus_dict = {chars[i]: chars[i+1] for i in range(-1, len(chars)-1)}
    i = len(lst)-1
    carry_over = True
    while carry_over and i >= 0:
        carry_over = lst[i]==end
        lst[i] = plus_dict[lst[i]]
        i -= 1
    if carry_over:
        lst[0:0] = [start]


def plus_str(s, chars):
    s_lst = list(s)
    plus_list_inplace(s_lst, chars)
    return ''.join(s_lst)

def plus_list(lst, chars):
    result = list(lst)
    plus_list_inplace(result, chars)
    return result

assert plus_str('zz', chars = string.ascii_lowercase) == 'aaa'
assert plus_str('aaa', chars = string.ascii_lowercase) == 'aab'
assert plus_str('$$', chars = '!@$') == '!!!'
print('tests passed')

