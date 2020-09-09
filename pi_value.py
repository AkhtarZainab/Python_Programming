import math

def fact(k):
    if k == 0:
        return 1
    if k == 1:
        return 1
    k = k * fact(k-1)
    print(k)
    return k


def estimate_pi():
    k=0
    sum_factor=0
    while True:
    # for i in range(5):

        a = (fact(4*k)) * (1103+(26390*k)) / ((fact(k)**4) * (396**(4*k)))
        print('Value of a = ', a)
        if a <= 1e-15:
            break
        sum_factor = sum_factor+a
        print('Current summation value is: ',sum_factor)
        k=k+1
    b = (2*math.sqrt(2))/9801
    pi_est = 1/(b*sum_factor)
    return pi_est

print(estimate_pi())
print(math.pi)