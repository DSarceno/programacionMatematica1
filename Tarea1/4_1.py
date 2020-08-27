from swampy.TurtleWorld import *
from math import pi

# EJERCICIO 4.1

#funcion que hace un cuadrado

def cuadrado(tortuga, lado):
    '''funcion que genera un cuadrado con lado dado por el usuario

    Argumentos:
    lado: longitud del lato del cuadrado
    '''
    print(tortuga)
    for i in range(4):
        fd(tortuga,lado)
        lt(tortuga)

# funcion que hace un poligono regular de n lados

def poligono(tortuga, nLados, tLado):
    '''genera un poligono regular de cierto numero de lados y su
    tamaño

    Argumentos:
    nLado: cantidad de lados
    tLado: tamaño de lado
    '''
    print(tortuga)
    for i in range(nLados):
        fd(tortuga, tLado)
        lt(tortuga, (360/nLados)) # angulo exterior


# funcion que aproxima un poligono regular a un circulo de cierto radio
def circ(tortuga, radio):
    '''funcion que aproxima la funcion poligono a un circulo
    tomandoun tamaño pequeño de lado y una gran cantidad de lados

    Argumentos:
    radio: radio del circulo
    '''
    print(tortuga)
    tLado = 2*pi*radio / 1000
    print(tLado)    # INCISO b EJERCICIO 4.1 (agregar 'prints')
    for i in range(1000):
        fd(tortuga, tLado)
        lt(tortuga, (360/1000))

# funcion que crea un segmento de arco
def arc(tortuga,radio,angulo):
    '''bajo aproximaciones la funcion crea un segmento de arco tomando
    un radio y el angulo sobre el cual se genera el arco
    
    Argumentos:
    radio: radio del arco
    angulo: angulo incluido en el arco
    '''
    print(tortuga)
    long_arco = 2 * pi * radio * angulo / 360
    n = int(long_arco / 3) + 1
    paso_long = long_arco / n
    paso_angulo = float(angulo) / n
    for i in range(n):
        fd(tortuga, paso_long)
        lt(tortuga, paso_angulo)

#   INCISO c DEL EJERCICIO 4.1 NO SE PUEDE REALIZAR PORQUE LA PAGINA DONDE
#       ESTA EL CODIGO YA NO EXISTE

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

arc(tortuga = bob, radio = 30, angulo = 50)

wait_for_user()
