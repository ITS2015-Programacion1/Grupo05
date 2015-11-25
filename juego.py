#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random

Fin_del_juego = False
#Iniciar el motor de PilasEngine
pilas = pilasengine.iniciar(ancho=288, alto=511)
#Añadir un marcador
puntos = pilas.actores.Puntaje(x=100, y=240, color=pilas.colores.naranja)
puntos.magnitud = 40
#Añadir el conmutador de sonido
Sonido = pilas.actores.Sonido
#Variables y constantes
Tubos1 = []
Tubos2 = []
Pisos = []
Puntos = []
#Define todas las cualidades del Fondo
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

#Define todas las cualidades de los Tubos (Colisionadores)
class Tubo(pilasengine.actores.Actor):

    def iniciar(self):
        # Define la imagen que se usara como Tubo
        self.imagen = 'flappytubo.png'
        # Define velocidad con la que se movera el tubo  
        self.velocidad = 1  
        # Posicion en X en la que aparecera
        self.x = 288 

        # posicion en Y aleatoria entre 159 y 250
        self.y = self.pilas.azar(95, 350)
    def actualizar(self):
        # mover tubos constantemente
        self.x -= self.velocidad  
        # Si el tubo llega al al borde izquierdo de la pantalla entonces lo eliminamos
        if self.x + self.ancho <= -144:
            self.eliminar()
    def crear_tubos():
        #funcion que sera llamada como una tarea
        tubo1 = Tubo(pilas)
        #Define que el radio de colision sea rectangular
        colision_rec1 = pilas.fisica.Rectangulo(-1000,-1000,50,315, sensor=True, dinamica= False)
        tubo1.figura_de_colision = colision_rec1
        #Agrega los tubos al vector, para asi de este modo se puedan eliminar luego
        Tubos1.append(tubo1)
        #Tubo de abajo
        tubo2 = Tubo(pilas)
        #Define que el radio de colision sea rectangular
        colision_rec2 = pilas.fisica.Rectangulo(-1000,-1000,50,315, sensor=True, dinamica= False)
        tubo2.figura_de_colision = colision_rec2
        #Define que el tubo debe rotar para poder quedar con la forma deseada de tubo
        tubo2.rotacion = 180
        #Define la distancia 
        tubo2.y = tubo1.y - (tubo1.alto / 2) * 2 - 100
        #Agrega los tubos al vector, para asi de este modo se puedan eliminar luego
        Tubos2.append(tubo2)
        #Llamar a la funcion crear_tubos cada 2.5 segundos
    pilas.tareas.siempre(4, crear_tubos)
#Define todas las cualidades del Piso (Colisionadores)
class Piso(pilasengine.actores.Actor):
    def iniciar(self):
        #Define la imagen que se usara como Piso
        self.imagen = 'flappypiso.png'
        #Define la velocidad con la que se movera el Piso
        self.velocidad = 1
        #Posicion X en la que aparecera
        self.x = 288
        #Posicion Y en la que aparecera
        self.y = -270
    def actualizar(self):
        # mover tubos constantemente
        self.x -= self.velocidad  
        # Si el Piso llega al al borde izquierdo de la pantalla entonces lo eliminamos
        if self.x + self.ancho <= -144:
            self.eliminar()
    def crear_piso():
        #Funcion que será llamada como Tarea
        piso1 = Piso(pilas)
        #Define que la colision sea rectangular
        colision_rec9 = pilas.fisica.Rectangulo(-1000,-1000,185,100, sensor=True, dinamica= False)
        piso1.figura_de_colision = colision_rec9
        #Agrega el piso a un vector, para que de este modo se pueda eliminar luego
        Pisos.append(piso1)
        #Llamar a la funcion crear_piso cada 2.5 segundos
    pilas.tareas.siempre(3, crear_piso)  

class ganar_puntos(pilasengine.actores.Actor):
    def iniciar(self):
        # Define la imagen que se usara como Actor para generar puntos
        self.imagen = 'invisible.png'
        # Define velocidad con la que se movera el tubo  
        self.velocidad = 1  
        # Posicion en X en la que aparecera
        self.x = 288 
        # posicion en Y aleatoria entre -160 y -30
        self.y = self.pilas.azar(-160, -30)
    def actualizar(self):
        # mover puntos constantemente
        self.x -= self.velocidad  
        # Si el tubo llega al al borde izquierdo de la pantalla entonces lo eliminamos
        if self.x + self.ancho <= -144:
            self.eliminar()
def crear_ganar_puntos():
    gana = ganar_puntos(pilas)
    #Define que la colision sea rectangular
    colision_rec7 = pilas.fisica.Rectangulo(-1000,-1000,50,95, sensor=True, dinamica= False)
    gana.figura_de_colision = colision_rec7
    #Agrega crear_ganar_puntos a un vector para ser eliminados luego
    Puntos.append(gana)
    #Aumenta el contador en 1
    puntos.aumentar(1)
    #Llama a la funcion crear_ganar_piso en 2.5 segundos 
pilas.tareas.siempre(4, crear_ganar_puntos)


# Crear fondo 1 con posicion en X de 288 (no visible)
fondo55 = FondoConMovimiento(pilas)
fondo55.x = 288
# Crear fondo 2
fondo22 = FondoConMovimiento(pilas)
#Define los controles que usara el juego
teclas = {
            pilas.simbolos.w: 'arriba',
            pilas.simbolos.s: 'abajo',
        }
mi_control = pilas.control.Control(teclas)
#Define al personaje principal FlappyBird
class FlappyConControles(pilasengine.actores.Actor):
    #Clase que define todos los aspectos del Actor
    def iniciar(self):
        #Define la imagen que se utilizara para el actor"
        self.imagen = pilas.imagenes.cargar_grilla("flappybird.png", 3)
        #Define la escala de tamaño del actor
        self.escala = 1.2
        #Define la posicion X en la cual se posicionara el actor
        self.x = -80
        #Define la posicion Y en la cual se posicionara el actor
        self.y = -200
        
    def actualizar(self):
        #Define cuanto avanzara en 0
        self.x += 0
        #Define cuanto avanzara el actor
        self.imagen.avanzar()
        #Define los controles
        #Define que pasara cuando se toque la letra "S"
        if mi_control.abajo:
            #Define cuanto se movera en el eje Y, mediante la interpolacion
            self.v=self.y-20
            #Define cuanto se movera el personaje gracias a esta interpolacion
            pilas.utils.interpolar(FlappyBird,'y',self.v,0.1)
        #Define que pasara cuando se toque la letra "W"
        if mi_control.arriba:
            #Define cuanto se movera en el eje Y, mediante la interpolacion
            self.z=self.y+90
            #Define cuanto se movera el personaje gracias a esta interpolacion
            pilas.utils.interpolar(FlappyBird,'y',self.z,0.4)
            #Define que sonido se escuchara cuando se toque la tecla "W"
            self.sonido_saltar = self.pilas.sonidos.cargar("audio/saltar.wav")
            #Le indica que se comiense a reproducir el sonido del salto
            self.sonido_saltar.reproducir()
        
#Funcion utilizada para cuando el usuario Pierde
def Perder(FlappyBird, tubos):  
    global Fin_del_juego
    FlappyBird.y = 0
    tubos.eliminar()
    #Emerger mensaje cuando el FlappyBird colisiona con un tubo
    texto1=pilas.actores.Texto("GAME OVER")
    texto1.y= 100
    #Informarle al usuario sobre su puntuacion obtenida
    texto2=pilas.actores.Texto("Perdiste conseguiste %d puntos" % (puntos.obtener()))
    texto2.y= -100
    #Define que el juego a finalizado.
    Fin_del_juego=True

    if Fin_del_juego:
        return False
    else:
        return True
#Vincula a FlappyConControles como un Actor
pilas.actores.vincular(FlappyConControles)
#Vincula a Tubo como un Actor
pilas.actores.vincular(Tubo)
#Vincula a Piso como un Actor
pilas.actores.vincular(Piso)
#Define como se llamara FlappyConControles
FlappyBird = FlappyConControles(pilas)
#Colision del actor FlappyBird con los Tubos1 y de esta manera ejecuta Perder
pilas.colisiones.agregar(FlappyBird, Tubos1, Perder)
#Colision del actor FlappyBird con los Tubos2 y de esta manera ejecuta Perder
pilas.colisiones.agregar(FlappyBird, Tubos2, Perder)
#Colision del actor FlappyBird con Piso y de esta manera ejecuta Perder
pilas.colisiones.agregar(FlappyBird, Pisos, Perder)

pilas.ejecutar()