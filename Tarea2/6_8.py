# @Author: Diego Sarceno
# Date: 18.08.2020

# Problema 6.8 del libro 'Think Python'

'''Este programa calcula el maximo comun divisor de entre dos numeros
utilizando el algoritmo de euclides'''

def mcd(a,b):
    '''funcion que calcula el mcd con el algoritmo de euclides'''
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

print(mcd(5,10))
