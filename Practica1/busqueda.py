# Author: Diego Sarceno
# Date: 23.08.2020

'''en este programa se recopilan todos los archivos .xml que esten
en los directorios en donde esta carpeta se encuentra'''

import glob
import os

print('Ingrese el directorio con un backslash extra en cada cambio de carpeta \
sin incluir el nombre del archivo.')
dir = input('Directorio: ')
if os.path.isdir(dir) == False:
    print('El directorio ingresado no existe, no sera tomado en cuenta.')
else:
    dir += '\\*xml'
    xml = glob.glob(dir)
    xmls += xml
