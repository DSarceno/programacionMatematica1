from swampy.TurtleWorld import *
from math import pi

# EJERCICIO 4.1


# funcion que aproxima un poligono regular a un circulo de cierto radio
def circ(tortuga,a,b):
    '''crea el espiral de arquimides  utilizando la ecuacion
    r=a+b*theta

    Argumentos:
    Como esta es una ecuacion lineal en coordenadas polares

    r: distancia entre el centro y el punto donde se encuentra el objeto
    a,b: parámetros
    theta: variable independiente, se utiliza para moderar dtheta
    dtheta: angulo que cambia para generar el espiral
    '''
    print(tortuga)
    tLado = 3
    theta = 0
    for i in range(1000):
        fd(tortuga, tLado)
        dtheta = 1 / (a + b*theta)
        lt(tortuga, dtheta)
        theta += dtheta

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

circ(bob,0.01,0.0002)

wait_for_user()
