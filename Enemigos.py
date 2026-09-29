from abc import ABC, abstractmethod
from Ataques import Fuego

class Enemigos(ABC):
    def __init__(self, numero):
        self.numero = numero
        self.vida = 1
        self.puntos = 100

    @abstractmethod
    def atacado(self, ataque):
        """actualizar a esstado nuevo del personaje"""

class Caminante(Enemigos):
    def __init__(self, numero=0):
        super().__init__(numero)

    def atacado(self, ataque):
        if self.vida > 0:
            self.vida -= 1
            return self.puntos
        return 0

class Tortuga(Enemigos):
    def __init__(self, numero):
        super().__init__(numero)
        self.vida = 2
        self.puntos = 200
        self.en_caparazon = False

    def atacado(self, ataque):
        if not isinstance(ataque, Fuego):
            if self.vida > 0:
                self.vida -= 1
                self.en_caparazon = True
                if self.vida == 0:
                    return self.puntos
            return 0
        else:
            derrotado = self.vida > 0
            self.vida = 0
            return self.puntos if derrotado else 0

class Fantasma(Enemigos):
    def __init__(self, numero):
        super().__init__(numero)
        self.vida = 1
        self.puntos = 300

    def atacado(self, ataque):
        if not isinstance(ataque, Fuego):
            return 0
        else:
            derrotado = self.vida > 0
            self.vida = 0
            return self.puntos if derrotado else 0