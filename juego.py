#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

class FondoConMovimiento(pilasengine.fondos.Fondo):

    def iniciar(self):
        self.imagen = 'flappyfondo.png'  # definir imagen
        self.velocidad = 1  # velocidad a la que se movera el fondo

    def actualizar(self):
        self.x -= self.velocidad  # mover hacia la izquierda

        # Si el fondo llega al borde izquierdo de la pantall
        # entonces cambiar su posicion en X
                # Si el fondo llega al borde izquierdo de la pantall
        # entonces cambiar su posicion en X
        if self.x + self.ancho <= 0:
            self.x = self.ancho