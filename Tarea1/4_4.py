from swampy.TurtleWorld import *
from math import pi

# EJERCICIO 4.4

# A
def draw_a(t):
    '''dibuja la letra A'''
    print(t)
    lt(t,60)
    fd(t,100)
    rt(t,120)
    fd(t,100)
    lt(t,180)
    fd(t,50)
    lt(t,60)
    fd(t,50)

# B
def draw_a(t):
    '''dibuja la letra B'''
    print(t)



world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

draw_a(bob)

wait_for_user()
