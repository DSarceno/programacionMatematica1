#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Diego Sarceno
# Date: 20.11.2020
#
#
#
# -----------------------

# Modulos Requeridos
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from datetime import datetime

class ascii(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = 'Arte ASCII')
        self.set_default_size(300,400)
        self.set_resizable(False)
        self.box = Gtk.VBox()
        self.add(self.box)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(1)
        self.grid.set_column_spacing(1)
        #self.add(self.grid)
        self.box.pack_start(self.grid,True,True,0)

        # Create HeaderBar.
        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)

        #····································································
        
        self.now = datetime.now()
        # ···································································
        # BARRA DE MENU
        mainMenuB = Gtk.MenuBar()
        # Archivo
        imgMenu = Gtk.Menu()
        imgMenuName = Gtk.MenuItem('Imagen')
            # Items
        imgCI = Gtk.MenuItem('Cargar Imagen')

        imgMenuName.set_submenu(imgMenu)
        imgMenu.append(imgCI)


        # Config
        twMenu = Gtk.Menu()
        twMenuName = Gtk.MenuItem('Twitter')
            # Items
        twSI = Gtk.MenuItem('Iniciar Sesión')
        twLO = Gtk.MenuItem('Cerrar Sesión')


        twMenuName.set_submenu(twMenu)
        twMenu.append(twSI)
        twMenu.append(Gtk.SeparatorMenuItem())
        twMenu.append(twLO)


        # Ayuda
        helpMenu = Gtk.Menu()
        helpMenuName = Gtk.MenuItem('Ayuda')
            # Items
        helpAD = Gtk.MenuItem('Acerca de...')

        helpMenuName.set_submenu(helpMenu)
        helpMenu.append(helpAD)


        # se añade al menu principal
        mainMenuB.append(imgMenuName)
        mainMenuB.append(twMenuName)
        mainMenuB.append(helpMenuName)

        # self.layout.pack_start(mainMenuB,True, True, 0)
        self.box1 = Gtk.HBox()
        self.hb.pack_start(mainMenuB)
        #self.grid.attach(self.hb,0,0,10,1)
        self.box1.pack_start(self.hb,True,True,0)
        self.grid.attach(self.box1,0,0,5,1)

        # ACCIONES DEL MENU
        imgCI.connect('activate', self.imgCI_activate)
        helpAD.connect('activate', self.helpAD_activate)


    def imgCI_activate(self, widget):
        dialog = Gtk.FileChooserDialog('Select a File',None,Gtk.FileChooserAction.OPEN,('Cancel',Gtk.ResponseType.CANCEL,'Ok',Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            '''
            bx = Gtk.VBox()
            imagen = GdkPixbuf.Pixbuf.new_from_file_at_scale(dialog.get_filename(), 100, 100,False)
            imagenC = Gtk.Image()
            imagenC.set_from_pixbuf(imagen)
            bx.pack_start(imagenC,True,True,0)
            self.grid.attach_next_to(imagenC,self.box1,Gtk.PositionType.BOTTOM,10,10)
            '''
        elif response == Gtk.ResponseType.CANCEL:
            pass
        dialog.destroy()

    def helpAD_activate(self, widget):
        #acerca de dialogo
        vbox = Gtk.VBox()
        adD = Gtk.AboutDialog()
        adD.set_program_name('Arte ASCII')
        adD.set_version('Programación Matemática 1')
        #adD.set_authors('DSR')
        adD.set_copyright('Copyright © 2020 Diego Sarceño')
        adD.set_comments('Conversor de imágenes a Artes ASCII, programado con e lenguaje de Python 3.')
        adD.set_website('https://github.com/DSarceno/programacionMatematica1/blob/master/Proyecto/proyecto.py')
        adD.set_website_label('Codigo Fuente')

        vbox.pack_start(adD, False, False, 0)
        self.add(vbox)
        adD.run()
        adD.destroy()


ventana = ascii()
ventana.connect('delete-event', Gtk.main_quit)
ventana.show_all()
Gtk.main()
