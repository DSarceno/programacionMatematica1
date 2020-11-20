#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Diego Sarceno
# Date: 20.11.2020
#
#
#
#

'''El programa toma dos numeros como entrada, el primero es el monto a
retirar y el segundo el saldo total en la cuenta. El banco cobra 0.5 por cada
retiro'''

monto = input('Entrada: ')
saldo = input()

def salResult(m,s):
    '''La funcion recibe dos numeros el monto a retirar y el saldo de la cuenta
    con el cobro del banco de 0.50

    '''

    m = int(m)
    s = round(float(s),2)

    if s <= m:
        return 'No tiene suficiente dinero'
    else:
        return str(s - m - 0.5) + str(0)

print('-------------')
print(salResult(monto,saldo))
