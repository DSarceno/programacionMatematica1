# Author: Diego Sarceno
# Date: 22.08.2020

# REPORTE E HISTOGRAMA

'''Este programa tiene las funciones que generan historgramas segun se pasen
listas con los datos y genera un documento de latex'''

def graph(datos):
    '''esta funcion recibe una lista de listas de la forma:
    [[cancion,artista,tiempo,[listas]],[cancion,artista,tiempo,[listas]]]
    y devuelve el histograma en pdf, esta funcion es necesario qeu vaya
    antes de la funcion pdf, para que el histograma se pueda agregar al
    archivo'''
    import numpy as np
    import matplotlib.pyplot as plt
    tiempos = []
    for x in datos:
        tiempos.append(x[2])
    m = int(max(tiempos)) + 1
    bins = [i for i in range(m + 1)]
    # graficacion del histograma
    plt.hist(tiempos, bins, histtype = 'bar', rwidth = 0.9, color = 'blue')
    plt.title('Duracion de Canciones')
    plt.xlabel('Tiempo')
    plt.ylabel('Cantidad de Canciones')
    plt.savefig('histograma.pdf')




def pdf(datos):
    '''esta funcion recibe una lista de listas de la forma:
    [[cancion,artista,tiempo,[listas]],[cancion,artista,tiempo,[listas]]]
    y esta funcion devuelve el .pdf con los datos en tabla y el histograma'''
    doc = open('graficaYDatos.tex','w')
    doc.write('\\input{preambulo.tex} \n')
    doc.write('\\begin{document} \n')
    doc.write('\\begin{titlepage} \n')
    doc.write('\\input{header.tex}\n')
    doc.write('\\section*{Datos}\n')
    doc.write('\\begin{longtable}{||c|c|c|p{4cm}||}\n')
    doc.write('\\hline \n')
    doc.write('\\hline \n')
    doc.write('Cancion & Artista & Tiempo & Listas de reproduccion en las\
    que aparece \\\\ \n')
    doc.write('\\hline \n')
    for x in datos:
        LRep = ''
        for i in x[3]:
            if i != x[3][len(x[3]) - 1]:
                LRep += i + ','
            elif i == x[3][len(x[3]) - 1]:
                LRep += i
        row = '{} & {} & {} & {} \\\\ \n'
        doc.write(row.format(x[0],x[1],x[2],LRep))
        doc.write('\\hline \n')
    doc.write('\\hline \n')
    doc.write('\\hline \n')
    doc.write('\\end{longtable}\n')
    # se añade la grafica
    doc.write('\\section*{Grafica} \n')
    doc.write('\\begin{figure}[H] \n')
    doc.write('\\centering \n')
    doc.write('\\includegraphics[scale=0.7]{histograma.pdf} \n')
    doc.write('\\caption{Estadisticas} \n')
    doc.write('\\end{figure} \n')
    doc.write('\\end{titlepage}\n')
    doc.write('\\end{document}')
    doc.close()
    import subprocess
    subprocess.run('pdfLatex "graficaYDatos.tex"', shell=True)
    subprocess.run('del "graficaYDatos.aux"', shell=True)
    subprocess.run('del "graficaYDatos.log"', shell=True)
    subprocess.run('del "graficaYDatos.out"', shell=True)
    subprocess.run('cls', shell=True)
    return
