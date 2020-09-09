def grid():
    do_loop()


def do_loop():
    for i in range(4):
        do_plus()
        for i in range(4):
            do_stand()

    do_plus()


def do_plus():
    print('+', '-' * 4, end='+')
    print('-' * 4, end='+')
    print("\n")


def do_stand():
    print('|', ' ' * 4, end='|')
    print(' ' * 4, end='|')
    print("\n")


grid()
