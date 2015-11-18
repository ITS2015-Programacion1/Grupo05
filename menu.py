# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()
def iniciar_juego():
	pilas.escenas.Juego()

def como_jugar():
    pilas.escenas.Instrucciones()
	
def salir_del_juego():
    pilas.terminar()

class Juego(pilasengine.escenas.Escena):
    def iniciar(self):
        pilas.fondo.Noche()    

class Instrucciones(pilasengine.escenas.Escena):
    def iniciar(self):
        pilas.escenas.Normal()
        pilas.fondo.Noche()

pilas.escenas.vincular(Juego)
pilas.escenas.vincular(Instrucciones)
MenuPrincipal = pilas.fondos.Fondo()
MenuPrincipal.imagen = pilas.imagenes.cargar("fondomenu.png")
pilas.actores.Menu([('Iniciar juego', iniciar_juego),('Como jugar', como_jugar),('salir', salir_del_juego),])
pilas.ejecutar()