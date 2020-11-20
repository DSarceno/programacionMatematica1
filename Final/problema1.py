#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Diego Sarceno
# Date: 20.11.2020
#
#
#
#

from math import sqrt, floor

# Número palindrome
def pal(n):
    return (str(n) == str(n)[::-1])

def sumP(n):
    '''Esta funcion toma las sumas de cuadrados y verifica si es un
    numero palindrome. Toma valores desde sqrt(n = 100000000) puesto que
    si el numero palindrome mas grande cumple, el numero mayor que lo
    puede generar en la suma es sqrt(10^8)

    '''
    numDone = []
    result = 0
    # se usa floor para que aproxime y devuelva un entero
    for i in range(floor(sqrt(n))):
        whileSum = i**2 # se define el primer elemento de la suma del numero
        for j in range(i + 1,floor(sqrt(n))):
            whileSum += j**2 # se empiezan a agregar terminos

            # si es menor al limite verifica que sea palindrome
            if whileSum >= n:
                break
            # Si el numero es palindrome y ya esta en la lista lo obvia, sino
            # se agrega a la suma
            elif whileSum not in numDone and (pal(whileSum) ==True):
                result += whileSum
                numDone.append(whileSum)
    # Se devuelve el resultado menos 1 por la condicion del problema
    return result - 1


print(sumP(100000000))
