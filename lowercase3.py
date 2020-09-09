def any_lowercase3(s):
    flag = True
    for c in s:
        if c.islower():
            return flag
    return False

print(any_lowercase3('DAY'))
print(any_lowercase3('Day'))
print(any_lowercase3('dAY'))
print(any_lowercase3('day'))
print(any_lowercase3('DAy'))
print(any_lowercase3('dAy'))
print(any_lowercase3('daY'))