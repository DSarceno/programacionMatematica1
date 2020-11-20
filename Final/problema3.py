#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Diego Sarceno
# Date: 20.11.2020
#
#
#
#

from math import floor

def coins(n):
    '''La función recibe un numero entero y en base a las seis denominaciones
    de monedas que se tienen, da el numero minimo de monedas para ajustar
    dicha cantidad.

    '''
    numC = 0
    while n != 0:
        if n >= 100:
            numC += floor(n/100)
            n = n % 100
        elif 50 <= n < 100:
            numC += floor(n/50)
            n = n % 50
        elif 10 <= n < 50:
            numC += floor(n/10)
            n = n % 10
        elif 5 <= n < 10:
            numC += floor(n/5)
            n = n % 5
        elif 2 <= n < 5:
            numC += floor(n/2)
            n = n % 2
        elif 0 < n < 2:
            numC += n
            n = n % 1
    return numC

# Entrada (como se especifica en el documento)
rep = input()
numCoins = []

for i in range(int(rep)):
    n = input()
    numCoins.append(coins(int(n)))

print('----------------')

# Salida (como se especifica en el documento)
for i in range(int(rep)):
    print(numCoins[i])
