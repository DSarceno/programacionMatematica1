#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Diego Sarceno
# Date: 22.10.2020


# Modulos Requeridos
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import webbrowser
import numpy as np
import random
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
from matplotlib.widgets import Button
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

# Clase General
class ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Juego de la Vida')
        self.set_default_size(300,300)
        self.set_resizable(False)
        # self.layout = Gtk.Box()
        # self.add(self.layout)

        grid = Gtk.Grid()
        self.add(grid)


        # Create HeaderBar.
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)


        #····································································
        # BARRA DE MENU
        mainMenuB = Gtk.MenuBar()
        # Archivo
        archMenu = Gtk.Menu()
        archMenuName = Gtk.MenuItem('Archivo')
            # Items
        archCI = Gtk.MenuItem('Cargar Configuración Inicial')
        archGS = Gtk.MenuItem('Guardar Estado de Simulación')
        archCA = Gtk.MenuItem('Generar Configuración Inicial Aleatoria')

        archMenuName.set_submenu(archMenu)
        archMenu.append(archCI)
        archMenu.append(Gtk.SeparatorMenuItem())
        archMenu.append(archGS)
        archMenu.append(Gtk.SeparatorMenuItem())
        archMenu.append(archCA)


        # Config
        conMenu = Gtk.Menu()
        conMenuName = Gtk.MenuItem('Configuración')
            # Items
        conFN = Gtk.MenuItem('Fronteras Normales')
        conFT = Gtk.MenuItem('Fronteras Toroidales')
        conST = Gtk.MenuItem('Segundos de Espera entre Turnos')

        conMenuName.set_submenu(conMenu)
        conMenu.append(conFN)
        conMenu.append(Gtk.SeparatorMenuItem())
        conMenu.append(conFT)
        conMenu.append(Gtk.SeparatorMenuItem())
        conMenu.append(conST)


        # Ayuda
        helpMenu = Gtk.Menu()
        helpMenuName = Gtk.MenuItem('Ayuda')
            # Items
        helpAD = Gtk.MenuItem('Acerca de...')
        helpCF = Gtk.MenuItem('Código Fuente')

        helpMenuName.set_submenu(helpMenu)
        helpMenu.append(helpAD)
        helpMenu.append(Gtk.SeparatorMenuItem())
        helpMenu.append(helpCF)


        # se añade al menu principal
        mainMenuB.append(archMenuName)
        mainMenuB.append(conMenuName)
        mainMenuB.append(helpMenuName)

        # self.layout.pack_start(mainMenuB,True, True, 0)
        hb.pack_start(mainMenuB)
        grid.attach(hb,0,0,4,1)
        # ····································································

        # Hace que el menu haga lo que tiene que hacer
        archCI.connect("activate", self.archCI_activate)
        archCA.connect("activate", self.archCA_activate)
        conFN.connect("activate", self.conFN_activate)
        conFT.connect("activate", self.conFT_activate)
        helpAD.connect("activate", self.helpAD_activate)
        helpCF.connect("activate", self.helpCF_activate)

        #·····································································
    # Funcionamiento del menu
    def archCI_activate(self, widget):
        dialog = Gtk.FileChooserDialog('Select a File',None,Gtk.FileChooserAction.OPEN,('Cancel',Gtk.ResponseType.CANCEL,'Ok',Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            # Lectura del archivo .pm2
            file = open(dialog.get_filename(),'r')
            global N
            N = int(file.readline())
            data = [line.split() for line in file]
            global gState
            gState = np.zeros((N,N))
            for j in range(len(data)):
                for i in range(len(data)):
                    gState[j,i] = int(data[j][i])
        elif response == Gtk.ResponseType.CANCEL:
            pass
        dialog.destroy()

    def archCA_activate(self, widget):
        global N
        N = random.randint(3,250)
        global gState
        gState = np.zeros((N,N))

        for y in range(n):
            for x in range(n):
                gState[y,x] = random.randint(0,1)

    def conFN_activate(self, widget):
        # SIMULACION
        def vecindad(gState):
            '''Esto crea una matriz en la que cada entrada muestra el numero de celulas
            vivas alrededor de dicha celula'''
            neigh = (
                np.roll(np.roll(gState, 1, 1), 1, 0) +  # Abajo-derecha
                np.roll(gState, 1, 0) +  # Abajo
                np.roll(np.roll(gState, -1, 1), 1, 0) +  # Abajo-izquierda
                np.roll(gState, -1, 1) +  # Izquierda
                np.roll(np.roll(gState, -1, 1), -1, 0) +  # Arriba-izquierda
                np.roll(gState, -1, 0) +  # Arriba
                np.roll(np.roll(gState, 1, 1), -1, 0) +  # Arriba-derecha
                np.roll(gState, 1, 1)  # Derecha
            )
            return neigh

        def paso(gState):
            '''Reglas del juego de la vida'''
            v = vecindad(gState)
            ngState = gState.copy()  # Copia de la matriz para no sobreescribir
            for i in range(ngState.shape[0]):
                for j in range(ngState.shape[1]):
                    if v[i, j] == 3 or (v[i, j] == 2 and ngState[i, j]):
                        ngState[i, j] = 1
                    else:
                        ngState[i, j] = 0
            return ngState

        pause = False # Pausa
        '''
        def onClick(event):
            global pause
            pause ^= True
        '''
        # Creamos la figura, formateo diverso
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        imagen = ax.imshow(gState, interpolation="none", aspect = "equal", cmap=cm.bwr)

        plt.tick_params(
            axis='x',
            which='both',
            bottom=False,
            top=False,
            labelbottom=False)

        def animate(i):
            global gState
            if not pause:
                print(i)
                gState = paso(gState)
                imagen.set_data(gState)

            return imagen,
        '''
        # Play/Pausa
        pause_ax = fig.add_axes((0.3, 0.025, 0.23, 0.04), anchor = 'SE')
        pause_button = Button(pause_ax, 'Play/pause', hovercolor='0.975')
        pause_button.on_clicked(onClick)
        '''

        anim = animation.FuncAnimation(fig, animate, frames=100, blit=True, interval = 200, repeat = True)
        grafico = Gtk.ScrolledWindow()
        canvas = FigureCanvas(fig)
        plt.show()


    def conFT_activate(self,widget):
        def vecindad(gState):
            '''Esto crea una matriz en la que cada entrada muestra el numero de celulas
            vivas alrededor de dicha celula con fronteras toroidales'''
            neigh = (
                np.roll(np.roll(gState, 1, 1), 1, 0) +  # Abajo-derecha
                np.roll(gState, 1, 0) +  # Abajo
                np.roll(np.roll(gState, -1, 1), 1, 0) +  # Abajo-izquierda
                np.roll(gState, -1, 1) +  # Izquierda
                np.roll(np.roll(gState, -1, 1), -1, 0) +  # Arriba-izquierda
                np.roll(gState, -1, 0) +  # Arriba
                np.roll(np.roll(gState, 1, 1), -1, 0) +  # Arriba-derecha
                np.roll(gState, 1, 1)  # Derecha
            )
            return neigh


        def paso(gState):
            '''Reglas del juego de la vida'''
            v = vecindad(gState)
            ngState = gState.copy()  # Copia de la matriz para no sobreescribir
            for i in range(ngState.shape[0]):
                for j in range(ngState.shape[1]):
                    if v[i, j] == 3 or (v[i, j] == 2 and ngState[i, j]):
                        ngState[i, j] = 1
                    else:
                        ngState[i, j] = 0
            return ngState

        pause = False # Pausa
        '''
        def onClick(event):
            global pause
            pause ^= True
        '''
        # Creamos la figura, formateo diverso
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        imagen = ax.imshow(gState, interpolation="none", aspect = "equal", cmap=cm.bwr)

        plt.tick_params(
            axis='x',
            which='both',
            bottom=False,
            top=False,
            labelbottom=False)

        def animate(i):
            global gState
            if not pause:
                print(i)
                gState = paso(gState)
                imagen.set_data(gState)

            return imagen,
        '''
        # Play/Pausa
        pause_ax = fig.add_axes((0.3, 0.025, 0.23, 0.04), anchor = 'SE')
        pause_button = Button(pause_ax, 'Play/pause', hovercolor='0.975')
        pause_button.on_clicked(onClick)
        '''
        anim = animation.FuncAnimation(fig, animate, frames=100, blit=True, interval = 200, repeat = True)
        plt.show()

    def helpAD_activate(self, widget):
        webbrowser.open_new_tab('https://github.com/DSarceno/programacionMatematica1/blob/master/Practica2/README.md')

    def helpCF_activate(self, widget):
        webbrowser.open_new_tab('https://github.com/DSarceno/programacionMatematica1/tree/master/Practica2')



window = ventana()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
