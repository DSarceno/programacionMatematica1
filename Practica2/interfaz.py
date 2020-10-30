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
from datetime import datetime


# Clase General
class ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Juego de la Vida')
        self.set_default_size(350,100)
        self.set_resizable(False)
        self.box = Gtk.VBox()
        self.add(self.box)


        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(4)
        self.grid.set_column_spacing(5)
        #self.add(self.grid)
        self.box.pack_start(self.grid,True,True,0)

        # Create HeaderBar.
        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)


        #····································································
        self.pause = False
        self.now = datetime.now()
        # ···································································
        # BARRA DE MENU
        mainMenuB = Gtk.MenuBar()
        # Archivo
        archMenu = Gtk.Menu()
        archMenuName = Gtk.MenuItem('Archivo')
            # Items
        archCI = Gtk.MenuItem('Cargar Configuración Inicial')
        #archGS = Gtk.MenuItem('Guardar Estado de Simulación')
        archCA = Gtk.MenuItem('Generar Configuración Inicial Aleatoria')

        archMenuName.set_submenu(archMenu)
        archMenu.append(archCI)
        archMenu.append(Gtk.SeparatorMenuItem())
        #archMenu.append(archGS)
        #archMenu.append(Gtk.SeparatorMenuItem())
        archMenu.append(archCA)


        # Config
        conMenu = Gtk.Menu()
        conMenuName = Gtk.MenuItem('Configuración')
            # Items
        conFN = Gtk.MenuItem('Fronteras Normales')
        conFT = Gtk.MenuItem('Fronteras Toroidales')
        #conST = Gtk.MenuItem('Segundos de Espera entre Turnos')

        conMenuName.set_submenu(conMenu)
        conMenu.append(conFN)
        conMenu.append(Gtk.SeparatorMenuItem())
        conMenu.append(conFT)
        #conMenu.append(Gtk.SeparatorMenuItem())
        #conMenu.append(conST)


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
        self.hb.pack_start(mainMenuB)
        self.grid.attach(self.hb,0,0,5,1)
        #self.box.pack_start(self.hb,True,True,0)
        # ····································································
        self.pp = Gtk.Button('Play/Pausa')
        self.grid.attach(self.pp,1,2,1,1)


        self.savePos = Gtk.Button('Guardar')
        self.grid.attach_next_to(self.savePos,self.pp,Gtk.PositionType.RIGHT,1,1)


        self.scale = Gtk.ScaleButton().new(2,0.00001,5,0.00001,None)
        self.grid.attach_next_to(self.scale,self.savePos,Gtk.PositionType.RIGHT,1,1)
        self.timeFrame = 1


        self.buffer = Gtk.TextBuffer()
        self.display = Gtk.TextView(buffer = self.buffer)
        self.display.set_size_request(30,30)
        self.grid.attach_next_to(self.display,self.scale,Gtk.PositionType.RIGHT,1,1)
        # ····································································

        # Hace que los botones hagan lo que tienen que hacer
        self.pp.connect('clicked', self.pp_clicked)
        self.savePos.connect('clicked', self.savePos_clicked)
        self.scale.connect('value-changed', self.scale_clicked)

        # Hace que el menu haga lo que tiene que hacer
        archCI.connect("activate", self.archCI_activate)
        archCA.connect("activate", self.archCA_activate)
        conFN.connect("activate", self.conFN_activate)
        conFT.connect("activate", self.conFT_activate)
        helpAD.connect("activate", self.helpAD_activate)
        helpCF.connect("activate", self.helpCF_activate)


        #·····································································
    # Funcionamiento de los botones
    # Escala tiempo
    def scale_clicked(self,scalebutton,value):
        self.timeFrame = self.scale.get_value()

    # Boton de pausa
    def pp_clicked(self, widget):
        self.pause ^= True

    # Boton de guardado de estado
    def savePos_clicked(self, widget):
        # FORMATO DE NOMBRES 'AñoMesDiaHoraMinutoSegundo.jvpm2'
        name = 'estadosGuardados/' + str(self.now.year) + str(self.now.month) + str(self.now.day) + str(self.now.hour) + str(self.now.minute) + str(self.now.second) + '.jvpm2'
        file = open(name,'w')
        file.write(str(N) + '\n')
        for j in range(N):
            line = ''
            for i in range(N):
                line += str(gState[j,i]) + ' '
            file.write(line + '\n')
        file.close()

    # Funcionamiento del menu
    # Cargar Configuracion inicial
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
                    gState[j,i] = eval(data[j][i])
            file.close()
        elif response == Gtk.ResponseType.CANCEL:
            pass
        dialog.destroy()

    # Cargar configuracion aleatoria
    def archCA_activate(self, widget):
        global N
        N = random.randint(3,250)
        global gState
        gState = np.zeros((N,N))

        for y in range(N):
            for x in range(N):
                gState[y,x] = random.randint(0,1)

    def conFN_activate(self, widget):
        # SIMULACION
        def vecindadNormal(gState):
            '''Esto crea una matriz en la que cada entrada muestra el numero de celulas
            vivas alrededor de dicha celula con fronteras normales'''
            # CUADRO INTERIOR
            neigh = np.zeros((len(gState),len(gState)))
            for j in range(1,len(gState) - 1):
                for i in range(1,len(gState) - 1):
                    neigh[j,i] = (
                        gState[j + 1,i - 1] +  # Abajo - Izquierda
                        gState[j + 1,i] +  # Abajo
                        gState[j + 1,i + 1] +  # Abajo - Derecha
                        gState[j,i + 1] +  # Derecha
                        gState[j - 1,i + 1] +  # Arriba - Derecha
                        gState[j - 1,i] +  # Arriba
                        gState[j - 1,i - 1] +  # Arriba - Izquierda
                        gState[j,i - 1]  # Izquierda
                    )
            # HORIZONTAL SUPERIOR SIN ESQUINAS
            for i in range(1,len(gState) - 1):
                neigh[0,i] = (
                    gState[0,i - 1] + # Izquierda
                    gState[1,i - 1] + # Abajo - Izquierda
                    gState[1,i] + # Abajo
                    gState[1,i + 1] + # Abajo - Derecha
                    gState[0,i + 1] # Derecha
                )

            # HORIZONTAL INFERIOR SIN ESQUINAS
            for i in range(1,len(gState) - 1):
                neigh[len(gState) - 1,i] = (
                    gState[len(gState) - 1,i - 1] + # Izquierda
                    gState[len(gState) - 2,i - 1] + # Arriba - Izquierda
                    gState[len(gState) - 2,i] + # Arriba
                    gState[len(gState) - 2,i + 1] + # Arriba - Derecha
                    gState[len(gState) - 1,i + 1] # Derecha
                )
            # VERTICAL IZQUIERDA SIN ESQUINAS
            for j in range(1,len(gState) - 1):
                neigh[j,0] = (
                    gState[j - 1,0] + # Arriba
                    gState[j - 1,1] + # Arriba - Derecha
                    gState[j,1] + # Derecha
                    gState[j + 1,1] + # Abajo - Derecha
                    gState[j + 1,0] # Abajo
                )
            # VERTICAL DERECHA SIN ESQUINAS
            for j in range(1,len(gState) - 1):
                neigh[j,0] = (
                    gState[j - 1,len(gState) - 1] + # Arriba
                    gState[j - 1,len(gState) - 2] + # Arriba - Izquierda
                    gState[j,len(gState) - 2] + # Izquierda
                    gState[j + 1,len(gState) - 2] + # Abajo - Izquierda
                    gState[j + 1,len(gState) - 1] # Abajo
                )
            #ESQUINA SUPERIOR IZQUIERDA
            neigh[0,0] = (
                gState[0,1] + # Derecha
                gState[1,1] + # Abajo - Derecha
                gState[1,0] # Abajo
            )
            # ESQUINA SUPERIOR DERECHA
            neigh[0,len(gState) - 1] = (
                gState[0,len(gState) - 2] + # Izquierda
                gState[1,len(gState) - 2] + # Abajo - Izquierda
                gState[1,len(gState) - 1] # Abajo
            )
            # ESQUINA INFERIOR IZQUIERDA
            neigh[len(gState) - 1,0] = (
                gState[len(gState) - 2,0] + # Arriba
                gState[len(gState) - 2,1] + # Arriba - Derecha
                gState[len(gState) - 1,1] # Derecha
            )
            # ESQUINA INFERIOR DERECHA
            neigh[len(gState) - 1,len(gState) - 1] = (
                gState[len(gState) - 2,len(gState) - 1] + # Arriba
                gState[len(gState) - 2,len(gState) - 2] + # Arriba - Izquierda
                gState[len(gState) - 1,len(gState) - 2] # Izquierda
            )
            return neigh

        def paso(gState):
            '''Reglas del juego de la vida'''
            v = vecindadNormal(gState)
            ngState = gState.copy()  # Copia de la matriz para no sobreescribir
            for i in range(ngState.shape[0]):
                for j in range(ngState.shape[1]):
                    if v[i, j] == 3 or (v[i, j] == 2 and ngState[i, j]):
                        ngState[i, j] = 1
                    else:
                        ngState[i, j] = 0
            return ngState

        # Creamos la figura, formateo diverso
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        imagen = ax.imshow(gState, interpolation="none", aspect = "equal", cmap=cm.bwr)

        plt.tick_params(
            axis='x',
            which='both',
            bottom=False,
            top=False,
            labelbottom=True)

        def animate(i):
            global gState
            if self.pause == False:
                self.buffer.set_text(str(i))
                gState = paso(gState)
                imagen.set_data(gState)

            return imagen,

        anim = animation.FuncAnimation(fig, animate, frames=100, blit=True, interval = (self.timeFrame * 1000), repeat = True)
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

        # Creamos la figura, formateo diverso
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        imagen = ax.imshow(gState, interpolation="none", aspect = "equal", cmap=cm.bwr)

        plt.tick_params(
            axis='x',
            which='both',
            bottom=False,
            top=False,
            labelbottom=True)

        def animate(i):
            global gState
            if self.pause == False:
                self.buffer.set_text(str(i))
                gState = paso(gState)
                imagen.set_data(gState)

            return imagen,

        anim = animation.FuncAnimation(fig, animate, frames=100, blit=True, interval = (self.timeFrame * 1000), repeat = True)
        plt.show()

    def helpAD_activate(self, widget):
        webbrowser.open_new_tab('https://github.com/DSarceno/programacionMatematica1/blob/master/Practica2/README.md')

    def helpCF_activate(self, widget):
        webbrowser.open_new_tab('https://github.com/DSarceno/programacionMatematica1/blob/master/Practica2/interfaz.py')



window = ventana()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
