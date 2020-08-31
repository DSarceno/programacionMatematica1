# Author: Diego Sarceno
# Date: 22.08.2020

# ARCHIVO PRINCIPAL DEL programa

'''menu inicial del programa'''
import subprocess
import glob
import os

# menu
print('En cuantos directorios desea buscar?')
cant = input('Escriba el numero de listas deseado: ' )
xmls = []
try:
    cant = int(cant)
    for i in range(cant):
        print('Ingrese el directorio con un backslash extra en cada cambio de \
carpeta sin incluir el nombre del archivo.')
        dir = input('Directorio: ')
        if os.path.isdir(dir) == False:
            print('El directorio ingresado no existe, no sera tomado en \
            cuenta.')
        else:
            dir += '\\*xml'
            xml = glob.glob(dir)
            xmls += xml
except ValueError:
    subprocess.run('cls',shell=True)
    print('No ha ingresado un numero entero, ingrese su eleccion de nuevo.')
    subprocess.run('python menu.py', shell=True)

print('Listas de reproduccion a analizar. Son estas las listas que \
escogio?')
for playlist, i in zip(xmls,range(1,len(xmls) + 1)):
    print(i,'. ' + playlist)
con = input('S: para confirmar, N para negar y volver a empezar. ')
if con == 'S':
    import lecturaXML as lxml
    for arch in xmls:
        print(lxml.lectura(arch))
elif con == 'N':
    subprocess.run('cls',shell=True)
    subprocess.run('python menu.py',shell=True)
else:
    print('Caracter no valido')
