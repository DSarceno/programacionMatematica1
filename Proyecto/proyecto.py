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
import os
from PIL import Image, ImageDraw, ImageFont
import math as m
import tweepy
import subprocess

class ascii(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = 'Arte ASCII')
        self.set_default_size(700,500)
        self.set_resizable(False)
        self.box = Gtk.VBox()
        self.add(self.box)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(1)
        self.grid.set_column_spacing(1)
        self.box.pack_start(self.grid,True,True,0)

        self.boxNormal = Gtk.VBox()
        self.boxAscii = Gtk.VBox()
        self.boxGenerador = Gtk.HBox()
        self.boxSaveTXT = Gtk.HBox()
        self.boxTweet = Gtk.HBox()
        self.charAscii = Gtk.Label('Caracteres: ')
        self.lNormal = Gtk.Label('Normal')
        self.lAscii = Gtk.Label('Arte ASCII')
        self.lInvertir = Gtk.Label('¿Invertir imagen?')


        self.radioSi = Gtk.RadioButton.new_with_label_from_widget(None, 'Sí')
        self.radioSi.connect('toggled', self.radioSi_toggled)
        self.radioNo = Gtk.RadioButton.new_from_widget(self.radioSi)
        self.radioNo.set_label('No')
        self.radioNo.connect('toggled', self.radioNo_toggled)

        self.setAsciiChars = Gtk.Button('Aceptar')
        self.setAsciiChars.connect('clicked',self.setAsciiChars_clicked)

        self.otroAscii = Gtk.Button('Generar otro Arte Ascii')
        self.otroAscii.connect('clicked',self.otroAscii_clicked)
        self.grid.attach(self.otroAscii,700,2,1,4)

        self.entryAscii = Gtk.Entry()
        self.entryAscii.set_text('@#$S%?*+;:,. ')
        self.grid.attach(self.boxNormal, 0, 150, 350,100)
        self.grid.attach(self.boxAscii, 350, 150, 350, 100)
        self.grid.attach_next_to(self.boxGenerador,self.boxNormal,Gtk.PositionType.BOTTOM,1,10)
        self.grid.attach_next_to(self.boxSaveTXT,self.boxGenerador,Gtk.PositionType.RIGHT,1,10)
        self.grid.attach_next_to(self.boxTweet,self.boxSaveTXT,Gtk.PositionType.RIGHT,1,10)


        self.grid.attach(self.lNormal, 100, 140, 1, 2)
        self.grid.attach(self.lAscii, 450, 140, 1, 2)

        self.grid.attach(self.charAscii,0,2,1,3)
        self.grid.attach_next_to(self.entryAscii,self.charAscii,Gtk.PositionType.RIGHT,1,3)

        self.grid.attach_next_to(self.setAsciiChars, self.entryAscii, Gtk.PositionType.RIGHT,1,2)

        self.grid.attach_next_to(self.radioSi, self.setAsciiChars, Gtk.PositionType.RIGHT, 1,2)
        self.grid.attach_next_to(self.radioNo, self.radioSi, Gtk.PositionType.RIGHT, 1,2)
        #····································································
        self.file = ''
        self.ASCII_CHARS = ''
        self.credenciales = False
        self.now = datetime.now()
        self.background = (0,0,0)
        self.colorfont = (255,255,255)
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


        self.grid.attach(mainMenuB,0,0,5,1)

        # ACCIONES DEL MENU
        imgCI.connect('activate', self.imgCI_activate)
        helpAD.connect('activate', self.helpAD_activate)
        twSI.connect('activate', self.twSI_activate)
        twLO.connect('activate', self.twLO_activate)

        # Boton para crear la imagen ascii
        self.generadorAscii = Gtk.Button('Generar Ascii')
        self.generadorAscii.connect('clicked',self.generadorAscii_clicked)

        self.saveTxt = Gtk.Button('Guardar Archivo')
        self.saveTxt.connect('clicked',self.saveTxt_clicked)

        self.tweetImg = Gtk.Button('Twittear Imagen ASCII')
        self.tweetImg.connect('clicked',self.tweetImg_clicked)

    def otroAscii_clicked(self, widget):
        self.connect('destroy',Gtk.main_quit)
        subprocess.call(['python3','proyecto.py'])


    def setAsciiChars_clicked(self, widget):
        self.ASCII_CHARS = self.entryAscii.get_text()

    def radioSi_toggled(self, widget):
        self.background = (0,0,0)
        self.colorfont = (255,255,255)

    def radioNo_toggled(self, widget):
        self.background = (255,255,255)
        self.colorfont = (0,0,0)


    def twSI_activate(self, widget):
        selectKey = Gtk.FileChooserDialog('Seleccione un archivo de llaves',None,Gtk.FileChooserAction.OPEN,('Cancel',Gtk.ResponseType.CANCEL,'Ok',Gtk.ResponseType.OK))
        selectKey.set_default_response(Gtk.ResponseType.OK)
        filtroKey = Gtk.FileFilter()
        filtroKey.set_name('Llaves')
        filtroKey.add_pattern('*.txt')
        selectKey.add_filter(filtroKey)
        response = selectKey.run()
        if response == Gtk.ResponseType.OK:
            fileKey = selectKey.get_filename()
            keys = open(fileKey,'r')
            global data
            data = [line.split() for line in keys]
            self.credenciales ^= True
        elif response == Gtk.ResponseType.CANCEL:
            pass
        selectKey.destroy()

    def twLO_activate(self, widget):
        if self.credenciales == True:
            data = []
            self.credenciales ^= False
        else:
            pass



    def imgCI_activate(self, widget):
        selectImage = Gtk.FileChooserDialog('Seleccione una Imagen',None,Gtk.FileChooserAction.OPEN,('Cancel',Gtk.ResponseType.CANCEL,'Ok',Gtk.ResponseType.OK))
        selectImage.set_default_response(Gtk.ResponseType.OK)
        filtro = Gtk.FileFilter()
        filtro.set_name('Imágenes')
        filtro.add_pattern('*.png')
        filtro.add_pattern('*.jpg')
        filtro.add_pattern('*.jpeg')
        selectImage.add_filter(filtro)
        response = selectImage.run()
        if response == Gtk.ResponseType.OK:
            self.file = selectImage.get_filename()
            imageC = GdkPixbuf.Pixbuf.new_from_file_at_size(self.file,600,600)
            imageGtk = Gtk.Image()
            imageGtk.set_from_pixbuf(imageC)
            self.boxNormal.pack_start(imageGtk, False, False, 0)
            self.boxGenerador.pack_start(self.generadorAscii,False,False,0)
            self.show_all()
        elif response == Gtk.ResponseType.CANCEL:
            pass
        selectImage.destroy()

    def generadorAscii_clicked(self, widget):
        def rescale(image, newWidth=100):
            '''reescala la imagen con la misma razon de lados.
            '''
            (originalWidth, originalHeight) = image.size
            ratio = originalHeight/float(originalWidth)
            newHeight = int(ratio * newWidth)
            newImage = image.resize((newWidth, newHeight))
            return newImage, newHeight

        def escalaGrises(image):
            '''convierte la imagen a escala de escalaGrises
            '''
            return image.convert('L')

        def pixelsAscii(image, rangeWidth=m.ceil(255/len(self.ASCII_CHARS))):
            '''mapea cierto conjunto de pixeles a un caracter ascii.

            0-255 lo divide en un numero de rangos de m.ceil(255/len(ASCII_CHARS)) pixeles
            '''

            # escoje en la lista de caracteres dependiendo del grupo de pixeles
            pixelsImage = list(image.getdata())
            pixelsChars = [self.ASCII_CHARS[m.floor(pixel/rangeWidth)] for pixel in
                    pixelsImage]

            return "".join(pixelsChars)

        def imagetoAscii(image, newWidth=100):
            '''Crea el string con el ascii generado y hace la imagen en formato .png
            '''
            image, newHeight = rescale(image)
            image = escalaGrises(image)


            pixelsChars = pixelsAscii(image)

            # Crea la imagen y el archivo .txt con el asciiArt
            fnt = ImageFont.load_default()
            outputImage = Image.new('RGB', (10*newWidth, 12*newHeight), color = self.background)
            drawImage = ImageDraw.Draw(outputImage)


            for i in range(newHeight):
                for j in range(newWidth):
                    drawImage.text((10*j, 12*i), pixelsChars[j + i*newWidth], font = fnt, fill = self.colorfont)
            name = str(self.now.year) + str(self.now.month) + str(self.now.day) + str(self.now.hour) + str(self.now.minute) + str(self.now.second)
            outputImage.save('imagenesAscii/' + name + '.png')


            # realiza los saltos de linea para imprimirlo en la terminal
            lenPixelsChars = len(pixelsChars)

            imageAscii = [pixelsChars[index: index + newWidth] for index in
                    range(0, lenPixelsChars, newWidth)]

            return "\n".join(imageAscii), name

        image = Image.open(self.file)

        global imageAscii
        global name
        imageAscii, name = imagetoAscii(image)

        imageC = GdkPixbuf.Pixbuf.new_from_file_at_size('imagenesAscii/' + name + '.png',600,600)
        imageGtk = Gtk.Image()
        imageGtk.set_from_pixbuf(imageC)
        self.boxAscii.pack_start(imageGtk, False, False, 0)
        self.boxSaveTXT.pack_start(self.saveTxt, False, False, 0)
        if self.credenciales == True:
            self.boxTweet.pack_start(self.tweetImg, False, False, 0)
        self.show_all()


    def saveTxt_clicked(self, widget):
        with open('archivosAscii/' + name + '.txt', 'w') as f:
            f.write(imageAscii)

    def tweetImg_clicked(self, widget):
        consumerKey = data[1][0]
        consumerSecret = data[3][0]
        accessToken = data[5][0]
        accessSecret = data[7][0]

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessSecret)
        api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

        tweet = '#ASCIIArtPM1'
        api.update_with_media('imagenesAscii/' + name + '.png', status = tweet)

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
