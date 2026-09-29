from abc import ABC, abstractmethod
class Objeto(ABC):
    nombre: str
    @abstractmethod
    def accion(self, observadores):
        """actualizar a esstado nuevo del personaje"""

class Moneda(Objeto):
    nombre = "Moneda"

    def accion(self, observadores):
        for observador in observadores:
            observador.actualizar(50)

class Potenciadores(Objeto):
    nombre = "Potenciador"
    def accion(self, observadores, estado):
        estado.potenciar(self,observadores)

class Hongo(Potenciadores):
    nombre = "Hongo"
    def accion(self, observadores,estado):
        estado.potenciar(self, observadores)

class Flor(Potenciadores):
    nombre = "Flor"
    def accion(self, observadores, estado):
        estado.potenciar(self, observadores)

class Caja_misteriosa:
    def __init__(self, numero, objeto):
        self.numero = numero
        self.objeto = objeto

    def tocar_caja(self, observadores, estado=None):
        if self.objeto is not None:
            if hasattr(observadores, "obtener_objeto"):
                observadores.obtener_objeto(self.objeto)
            else:
                self.objeto.accion(observadores, estado)
            self.objeto = None
        