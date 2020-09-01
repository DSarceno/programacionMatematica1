# @Author: Diego Sarceno
# Date: 21.08.2020

# ESCRITURA DEL ARCHIVO .csv

'''este programa tomara la lista de reproducción deseada y generara su
archivo .csv con los datos de Cancion   Artista     Duracion; cada uno
de ellos separados por tabulaciones'''

def archCSV(data):
    '''esta funcion toma una lista de la forma:
    [[cancion,artista,tiempo,[listas]],[cancion,artista,tiempo,[listas]]]
    y elimina la parte del nombre de la lista y convierte el flotante a
    string para que se pueda escripir en el .csv'''
    for i in data:
        i.pop(len(i) - 1)
        i[2] = str(i[2])
    import csv
    with open('canciones.csv','w',newline='') as file:
        writer = csv.writer(file, delimiter = '\t')
        writer.writerows(data)
    return
