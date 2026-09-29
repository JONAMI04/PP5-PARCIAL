from Observadores import ObservadorPuntos, ObservadorVidas
from Ataques import Fuego as AtaqueFuego
from Estados import Fuego as EstadoFuego
from Estados import Pequenio

class Personaje:
    def __init__(self):
        self.estado = Pequenio()
        self._observadores = [ObservadorPuntos(), ObservadorVidas()]

    @property
    def observadores(self):
        return tuple(self._observadores)

    def recibir_dano(self):
        dano = self.estado.recibir_dano()
        for observador in self.observadores:
            observador.actualizar(dano)
        self.estado = self.estado.nuevo_estado()

    def atacar(self, enemigo):
        self.estado.atacar(enemigo)

    @property
    def juego_interrumpido(self):
        return self._juego_interrumpido

    def interrumpir_juego(self):
        self._juego_interrumpido = True

    def obtener_objeto(self, objeto):
        objeto.accion(self.observadores, self.estado)

    obterner_objeto = obtener_objeto

    def sumar_puntos(self, puntos):
        for observador in self._observadores:
            observador.actualizar(puntos)

    def sumar_vidas(self, vidas):
        for observador in self._observadores:
            observador.actualizar(vidas)

    def toca_enemigo(self):
        self.recibir_dano()
