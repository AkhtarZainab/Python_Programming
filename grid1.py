

def do_loop():
    do_plus()
    do_stand()
    do_plus()

def do_plus():
    for i in range(4):
        print('+', '-' * 4, end='+')
        print('-' * 4, end='+')
    print("\n")

def do_stand():
    for i in range(4):
        print('|', ' ' * 4, end='|')
        print(' ' * 4, end='|')
    print("\n")

do_loop()
