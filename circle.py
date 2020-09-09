import math
import turtle
bob = turtle.Turtle()

def polygon(t, angle, length, n):

    narc = int(n*angle/360)
    for i in range(narc):
        t.fd(length)
        t.lt(360/n)

def circle(t, r, angle):
    n = 200
    length = 2*math.pi*r/(n)
    polygon(t, angle, length,n)

circle(bob, 100, 360)
turtle.mainloop()