def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(capitalize_all(['one', 'two', 'three', 'four', 'five']))