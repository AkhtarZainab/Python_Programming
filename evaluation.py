def eval_loop():

    #a='begin'
    while True:
        a = input("Please input the expression to be evaluated: ")
        if a == 'done':
            break
        b = eval(a)
        print(b)
    return b


print('Return value of evaluation is: ',eval_loop())

