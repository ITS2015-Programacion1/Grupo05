#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

class FondoConMovimiento(pilasengine.fondos.Fondo):

    def iniciar(self):
    	 # define que imagen se usara como fondo
        self.imagen = 'flappyfondo.png' 
        # velocidad a la que se movera el fondo
        self.velocidad = 1  

    def actualizar(self):
    	# define que se movera hacia la izquierda
        self.x -= self.velocidad  

        # Si el fondo llega al borde izquierdo de la pantalla entonces cambiar su posicion en X
        if self.x + self.ancho <= 0:
            self.x = self.ancho

class Tubo(pilasengine.actores.Actor):

    def iniciar(self):
    	# Define la imagen que se usara como Tubo
        self.imagen = 'flappytubo.png'
        # Define velocidad con la que se movera el tubo  
        self.velocidad = 1  
        # Posicion en X en la que aparecera
        self.x = 288 

        # posicion en Y aleatoria entre 159 y 250
        self.y = self.pilas.azar(159, 250)

    def actualizar(self):
    	# mover tubos constantemente
        self.x -= self.velocidad  

        # Si el tubo llega al al borde izquierdo de la pantalla entonces lo eliminamos
        if self.x + self.ancho <= -144:
             self.eliminar()
    def crear_tubos():
		#funcion que sera llamada como una tarea
	    tubo1 = Tubo(pilas)
	    #Tubo de abajo
	    tubo2 = Tubo(pilas)
	    tubo2.rotacion = 180
	    tubo2.y = tubo1.y - (tubo1.alto / 2) * 2 - 100

