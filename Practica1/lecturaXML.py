# -*- UTF-8 -*-
# @Author: Diego Sarceno
# Date: 21.08.2020

# LECTURA DE ARCHIVO .xml
'''
# Para el nombre
print(x[17][8:12])
print(x[17][26:len(x[17]) - 10])

# Para el artista
print(x[18][8:14])
print(x[18][28:len(x[18]) - 10])

# para el tiempo
print(x[25][8:18])
print(x[25][33:len(x[26]) - 10])
'''

def lectura(arxiv,dir):
    archivo = open(arxiv,'r')

    x = archivo.readlines()

    canciones = []
    for thing in x:
        if thing[8:12] == 'Name':
            canciones.append(thing[26:len(thing) - 10])
        elif thing[8:14] == 'Artist':
            canciones.append(thing[28:len(thing) - 10])
        elif thing[8:18] == 'Total Time':
            tmin = round(float(thing[33:len(thing) - 11]) / 60000, 2)
            canciones.append(tmin)
    '''esto devolvera una lista en la que cada 3 entradas es una cancion y en
    la ultima entrada se tiene el nmbre de la lista de reproduccion a la
    cual pertenece'''
    songs = []
    for i in range(int(len(canciones) / 3)):
        song = []
        song.append(canciones[3*i])
        song.append(canciones[3*i + 1])
        song.append(canciones[3*i + 2])
        song.append([arxiv[len(dir):len(arxiv) - 4]])
        songs.append(song)
    '''esto es para que devuelva el formato necesario para las funciones
    que generan la gráfica y el reporte'''
    return songs
