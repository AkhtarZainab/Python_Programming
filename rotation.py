def rotate_word(s, num):
    d = ''
    for i in s:
        a = ord(i)
        b = a + num
        c = chr(b)
        d = d+c
    return d

print(rotate_word('cheer', 7))