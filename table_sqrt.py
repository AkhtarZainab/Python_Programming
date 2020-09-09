import math


def mysqrt(a):
        x = a - 1
        while True:
                y = (x + a / x) / 2
                if y == x:
                        break
                x = y
        return y


def test_square_root():
        for i in range(10):
                a = i + 1

                if a == 1:
                        # print("The square root of ", a, "is ", 1)
                        print(a, 1.0, 1.0, 0.0)
                        continue

                b = mysqrt(a)
                c = math.sqrt(a)
                diff = mysqrt(a) - math.sqrt(a)

                print(a, b, c, diff)

test_square_root()