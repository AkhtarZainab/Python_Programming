import turtle
bob = turtle.Turtle()


def koch(t, x):
    if x < 3:
        t.fd(x)
        return
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)
    t.rt(120)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)

koch(bob, 100)
turtle.mainloop()