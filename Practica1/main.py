# Author: Diego Sarceno
# Date: 22.08.2020

# ARCHIVO PRINCIPAL DEL programa

'''menu inicial del programa'''
import subprocess
import glob
import os

# menu
cant = input('En cuantos directorios desea buscar? ' )
dirs = [] # guarda  el directorio para eliminarlo y dejar el nombre de la lista
xmls = [] # guarda la ruta completa para leer el archivo

# Esto se realiza para evitar que el programa se detenga por error de valor
try:
    cant = int(cant)
    for i in range(cant):
        print('Ingrese el directorio con un backslash extra \
en cada cambio de carpeta sin incluir el nombre del archivo.')
        print('Si no se encuentra ningun archivo en el directorio, simplemete \
sera obviado \n')
        dir = input('Directorio: ')
        if os.path.isdir(dir) == False:
            print('El directorio ingresado no existe, no sera tomado en \
            cuenta.')
        else:
            dirs.append(dir + '\\')
            dir += '\\*xml'
            xml = glob.glob(dir)
            xmls += xml
            for i in range(len(xmls) - len(dirs)):
                dirs.append(dirs[len(dirs) - 1])
except ValueError:
    subprocess.run('cls',shell=True)
    print('No ha ingresado un numero entero, ingrese su eleccion de nuevo.')
    subprocess.run('python main.py', shell=True)

# Teniendo las listas se crea el arreglo para procesarlas
print('Listas de reproduccion a analizar. Desea continuar?')
for playlist, i in zip(xmls,range(1,len(xmls) + 1)):
    print(i,'. ' + playlist)
con = input('S: para confirmar, N para negar y volver a empezar. ')
if con == 'S':
    import lecturaXML as lxml
    import archivoCSV as CSV
    DATA = []
    for arch,dir in zip(xmls,dirs):
        DATA.extend(lxml.lectura(arch,dir))
    print(DATA)
    CSV.archCSV(DATA)
elif con == 'N':
    subprocess.run('cls',shell=True)
    subprocess.run('python menu.py',shell=True)
else:
    print('Caracter no valido')

# se genera el histograma y el reporte
import texYGrafica as TG
TG.graph(DATA)
TG.pdf(DATA)
