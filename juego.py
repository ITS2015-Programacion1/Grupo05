#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random

fin_de_juego = False

#Iniciar el motor de Pilas Engine
pilas = pilasengine.iniciar()
#Dotar de un Fondo 
Fondo = pilas.fondos.flappyfondo.png 
# Añadir un marcador
puntos = pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.rojo)
puntos.magnitud = 40
# Añadir el conmutador de Sonido
pilas.actores.Sonido()
