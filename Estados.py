from abc import ABC, abstractmethod
from Ataques import Saltar, Fuego
from Objetos import Hongo, Potenciadores, Flor


class Estado(ABC):
    nombre: str

    @abstractmethod
    def recibir_dano(self):
        """actualizar a esstado nuevo del personaje"""

    @abstractmethod
    def nuevo_estado(self):
        """retorna el nuevo estado del personaje"""
    @abstractmethod
    def atacar(self, enemigo):
        """ataque del personaje"""
        return

class Pequenio(Estado):
    nombre = "Pequeño"

    def recibir_dano(self):
        return -1

    def nuevo_estado(self):
        return Pequenio()

    def potenciar(self, objeto):
        if isinstance(objeto, Potenciadores):
            return Grande()

    def atacar(self, enemigo):
        enemigo.atacado(self, Saltar())

class Grande(Estado):
    nombre = "Grande"

    def recibir_dano(self):
        return 0

    def nuevo_estado(self):
        return Pequenio()

    def atacar(self, enemigo):
        enemigo.atacado(self, Saltar())

    def potenciar(self, objeto, observadores):
        if isinstance(objeto, Hongo):
            for observador in observadores:
                observador.actualizar(100)
            return Grande()
        if isinstance(objeto, Flor):
            return Fuego()

class Fuego(Estado):
    nombre = "Fuego"

    def recibir_dano(self):
        return 0

    def nuevo_estado(self):
        return Grande()

    def potenciar(self, objeto, observadores):
        for observador in observadores:
            observador.actualizar(100)
        return Fuego()

    def atacar(self, enemigo):
        enemigo.atacado(self, Fuego())