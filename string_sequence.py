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


