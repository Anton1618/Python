def char_count(st: str) -> list:
    '''Сортировка подсчетом со смещением для латинского алфавита'''
    offset_char_lst = [0]*26
    for i in st.lower():
        if 'a'<i<'z':
            index_offset = ord(i) - 97
            offset_char_lst[index_offset] += 1
    result = []
    for i in range(len(offset_char_lst)):
        if offset_char_lst[i] > 0:
            result.append((chr(i+97), offset_char_lst[i]))
    return result

if __name__ == '__main__':
    assert char_count('Привет, Мир!') == []
    assert char_count('aaaaa') == []
    assert char_count('aaaaa zzzzzz') == []
    assert char_count('1343400 2  23 423 4234 ') == []
    assert char_count('aaaaa bbbbb') == [('b', 5)]
    assert char_count('aaaaa 34 sdfds ') == [('d', 2), ('f', 1), ('s', 2)]
    assert char_count('aaaaa bbbbb cccc') == [('b', 5), ('c', 4)]
    assert char_count('aaaaa bbbbb cccc 11111') == [('b', 5), ('c', 4)]
    assert char_count('qwerty qwerty qwerty') == [('e', 3), ('q', 3), ('r', 3), ('t', 3), ('w', 3), ('y', 3)]
    assert char_count('Hello, World!') == [('d', 1), ('e', 1), ('h', 1), ('l', 3), ('o', 2), ('r', 1), ('w', 1)]
    assert char_count('adgfrewgv25gbv253gvregwergvwregvwergfvwertq') == [('b', 1), ('d', 1), ('e', 6), ('f', 2), ('g', 8), ('q', 1), ('r', 6), ('t', 1), ('v', 6), ('w', 5)]
