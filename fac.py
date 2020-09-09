def fac(k):
    if k == 0:
        return 1
    if k == 1:
        return 1
    k = k * fac(k-1)
    return k
################




print(fac(5))

