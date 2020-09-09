def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
    return False



print(any_lowercase1('DAY'))
print(any_lowercase1('Day'))
print(any_lowercase1('dAY'))
print(any_lowercase1('day'))
print(any_lowercase1('DAy'))
print(any_lowercase1('dAy'))
print(any_lowercase1('daY'))