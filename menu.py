# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
pilas.fondos.Tarde()

def ayuda():
	pilas.fondos.Tarde()
	menu.eliminar()
	mi_texto = """    Flappy Barbie es un juego que consiste en un
				android que tiene que ir volando entre filas 
				de tuberias verdes sin tocarse, la escena 
				se va desplazando lateralmente."""
	texto = pilas.actores.Texto(mi_texto, y=150)

def salir_del_juego():
	pilas.terminar()
	menu.eliminar()

def iniciar_juego():
	pilas.fondos.Noche()
	menu.eliminar()

menu = pilas.actores.Menu(
        [
            ('Iniciar juego', iniciar_juego),		
            ('Ayuda', ayuda),			
            ('Salir', 	salir_del_juego),
        ])
pilas.ejecutar()
