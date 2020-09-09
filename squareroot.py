def mysqrt(a):
    x = 9
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    print("The square root of ", a, "is ", y)

mysqrt(10)