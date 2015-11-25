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
        pilas.fondos.Tarde()   

class Instrucciones(pilasengine.escenas.Escena):
    def iniciar(self):       
	pilas.escenas.Normal()
        mi_texto = """FlappyBird consiste en un pajaro que ha salido de su casa hacia lo desconocido y se ha perdido en la inmensidad del mundo exterior y de todo lo 		conocido para el, para retornar a la seguridad de su casa, debera sortear los diversos obstaculos que se le presentan a su paso como lo son los Tubos.
	El pajaro salta con W"""

	texto = pilas.actores.Texto(mi_texto, y=100, ancho=600)

	texto_codigo = pilas.actores.Texto("", magnitud=16, ancho =200)
	texto_codigo.x = -150
	texto_codigo.y = -150

pilas.escenas.vincular(Juego)
pilas.escenas.vincular(Instrucciones)

MenuPrincipal = pilas.fondos.Fondo()
MenuPrincipal.imagen = pilas.imagenes.cargar("fondomenu.png")
pilas.actores.Menu([('Iniciar juego', iniciar_juego),('Como jugar', como_jugar),('salir', salir_del_juego),])
pilas.ejecutar()
