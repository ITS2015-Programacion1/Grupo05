#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random
import pilasengine
fin_de_juego = False

#Iniciar el motor de Pilas Engine
pilas = pilasengine.iniciar()
#Dotar de un Fondo 
fondo = pilas.fondos.Galaxia()
# Añadir un marcador
puntos = pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.rojo)
puntos.magnitud = 40
# Añadir el conmutador de Sonido
pilas.actores.Sonido()

# Crear personaje
class android(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "actor.ico"
		self.escala = 0.7
		self.x = -210
		self.y = 0
pilas.actores.vincular(android)
android = pilas.actores.android()


#agregar efecto al personaje
android.escala = 1
android.rotacion = 0

def girar():
	android.rotacion = android.rotacion + 1
	return True




pilas.escena.tareas.siempre(0.01, girar)

