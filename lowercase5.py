def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('DAY'))
print(any_lowercase5('Day'))
print(any_lowercase5('dAY'))
print(any_lowercase5('day'))
print(any_lowercase5('DAy'))
print(any_lowercase5('dAy'))
print(any_lowercase5('daY'))