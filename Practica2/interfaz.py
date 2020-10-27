#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Diego Sarceno
# Date: 22.10.2020

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import webbrowser
import numpy as np
import random


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

        '''
        # Create Notebook
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Create Boxes
        self.page1 = Gtk.Box()
        self.page1.set_border_width(50)
        self.page1.add(Gtk.Label("Saliooooooo xd"))
        self.notebook.append_page(self.page1, Gtk.Label("Pag1"))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(50)
        self.page2.add(Gtk.Label("Buenardo"))
        self.notebook.append_page(self.page2, Gtk.Label("Pag2"))

        grid.attach(self.notebook,0,2,4,6)
        '''


        # Hace que el menu haga loque tiene que hacer
        archCI.connect("activate", self.archCI_activate)
        archCA.connect("activate", self.archCA_activate)
        helpCF.connect("activate", self.helpCF_activate)



    def archCI_activate(self, widget):
        dialog = Gtk.FileChooserDialog('Select a File',self,Gtk.FileChooserAction.OPEN,('Cancel',Gtk.ResponseType.CANCEL,'Ok',Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print('Buenardo, archivo seleccionado: ',dialog.get_filename())
            ruta = dialog.get_filename()
            file = open(ruta,'r')
            data = file.readline()
            print(data)
        elif response == Gtk.ResponseType.CANCEL:
            print('Ningún archivo seleccionado')
        dialog.destroy()

    def archCA_activate(self, widget):
        n = random.randint(3,250)
        gstate = np.zeros((n,n))

        for y in range(n):
            for x in range(n):
                gstate[x,y] = random.randint(0,1)

        print(gstate)

    def helpCF_activate(self, widget):
        webbrowser.open_new_tab('https://github.com/DSarceno/programacionMatematica1/tree/master/Practica2')



window = ventana()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
