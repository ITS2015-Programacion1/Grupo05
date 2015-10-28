import pilasengine
pilas.fondos.Noche()
pilas = pilasengine.iniciar()

class personaje(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "actor.ico"
	self.escala = 0.7
	self.x = -210
	self.y = 0
pilas.actores.vincular(personaje)
personaje = pilas.actores.personaje()




