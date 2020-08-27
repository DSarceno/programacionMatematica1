# @Author: Diego Sarceno
# Date: 18.08.2020

# Problema 6.5 del libro 'Think Python'

'''Se programa la funcion de Ackermann'''

def ack(m,n):
    if m == 0:
        return n + 1
    elif (m > 0) and (n == 0):
        return ack(m - 1, 1)
    elif (m > 0) and (n > 0):
        return ack(m - 1, ack(m,n - 1))

print(ack(1,2))
