from swampy.TurtleWorld import *
from math import pi

# EJERCICIO 4.2

# se utilia esta funcion para facilitar el codigo del petalo
def arc(tortuga,radio,angulo):
    '''bajo aproximaciones la funcion crea un segmento de arco tomando
    un radio y el angulo sobre el cual se genera el arco

    Argumentos:
    radio: radio del arco
    angulo: angulo incluido en el arco
    '''
    print(t)
    long_arco = 2 * pi * radio * angulo / 360
    n = int(long_arco / 3) + 1
    paso_long = long_arco / n
    paso_angulo = float(angulo) / n
    for i in range(n):
        fd(tortuga, paso_long)
        lt(tortuga, paso_angulo)

def pet(tortuga, radio, angulo):
    '''tomamos la funcion de arco y se utiliza para generar el petalo
    utilizandola 2 veces'''
    for i in range(2):
        arc(tortuga, radio, angulo)
        lt(tortuga, 180 - angulo)

def flor(tortuga,n,radio,angulo):
    '''utilizando la funcion pet, simplemente se hace un ciclo para hacer
    varios petalos

    Argumentos:
    n: numero de petalos
    '''
    for i in range(n):
        pet(tortuga,radio,angulo)
        lt(tortuga,360/n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

pet(bob,100,50)

wait_for_user()
