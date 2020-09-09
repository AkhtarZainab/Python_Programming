def any_lowercase4(s):
    flag = True
    for c in s:
        flag = c.islower()
        return flag

print(any_lowercase4('DAY'))
print(any_lowercase4('Day'))
print(any_lowercase4('dAY'))
print(any_lowercase4('day'))
print(any_lowercase4('DAy'))
print(any_lowercase4('dAy'))
print(any_lowercase4('daY'))