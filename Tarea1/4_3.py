from swampy.TurtleWorld import *
from math import pi, sqrt, cos

# EJERCICIO 4.3

# se toma la funcion del poligono y se realiza el poligono y se modifica
def poligono_diag(tortuga, nLados, tLado):
    '''genera un poligono regular de cierto numero de lados (nLados) y su
    tamaño (tLado)

    Argumentos:
    Con estos datos se crean los rayos en el polinomio
    
    alpha: angulo generado por radios contiguos del polinomio
    beta: angulo entre lado y radio
    r: radio, distancia entre el centro y los vertices del poligono
    '''
    print(tortuga)
    for i in range(nLados):
        fd(tortuga, tLado)
        lt(tortuga, (360/nLados)) # angulo exterior
    # ahora, desde la posición en la que esta se generan los radios
    alpha = 360 / nLados
    beta = (180 - alpha) / 2
    r = sqrt((tLado**2) / (2*(1-cos(alpha * pi / 180))))
    # se mueve el primer angulo, el cual es el unico distinto
    lt(tortuga, beta)
    fd(tortuga,r)
    for i in range(nLados -1 ):
        rt(tortuga,180 - alpha)
        fd(tortuga,r)
        lt(tortuga,alpha + beta)
        fd(tortuga,tLado)
        lt(tortuga,alpha + beta)
        fd(tortuga,r)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

poligono_diag(tortuga = bob, nLados = 10, tLado = 30)

wait_for_user()
