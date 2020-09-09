def any_lowercase2(s):
    for c in s:
        if c.islower():
            return True

    return False

print(any_lowercase2('DAY'))
print(any_lowercase2('Day'))
print(any_lowercase2('dAY'))
print(any_lowercase2('day'))
print(any_lowercase2('DAy'))
print(any_lowercase2('dAy'))
print(any_lowercase2('daY'))