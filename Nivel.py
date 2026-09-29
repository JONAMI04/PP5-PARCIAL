from Enemigos import Enemigos
from Objetos import Objeto

class Nivel:
    def __init__(self, nombre):
        self.nombre = nombre
        self._enemigos = []
        self._objetos = []

    @property
    def enemigos(self):
        return tuple(self._enemigos)

    @property
    def objetos(self):
        return tuple(self._objetos)

    def agregar_objeto(self, objeto):
        if not isinstance(objeto, Objeto):
            assert TypeError("El objeto debe ser una instancia de la clase Objeto")
        self._objetos.append(objeto)

    def agregar_enemigo(self, enemigo):
        if not isinstance(enemigo, Enemigos):
            assert TypeError("El enemigo debe ser una instancia de la clase Enemigos")
        self._enemigos.append(enemigo)

    def quedan_enemigos(self):
        for enemigo in self._enemigos:
            if enemigo.vida > 0:
                return True
        return False

    def esta_completado(self):
        return not self.quedan_enemigos()

    @property
    def completado(self):
        return self.esta_completado()

    def comprobar_nivel(self):
        if self.quedan_enemigos():
            print("Aún quedan enemigos en el nivel.")
        print("nivel terminado, no quedan enemigos.")
        exit()
