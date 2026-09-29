class ObservadorPuntos:
    def __init__(self):
        self.puntos = 0

    def actualizar(self, puntosTotales):
        if puntosTotales > 10:
            self.puntos += puntosTotales
        return


class ObservadorVidas:
    def __init__(self):
        self.vidas = 3

    def actualizar(self, vidasTotales):
        if vidasTotales <= 1:
            self.vidas = vidasTotales+self.vidas
            if self.vidas <= 0:
                self.alPerderUltimaVida()
        return

    def alPerderUltimaVida(self):
        print("¡Has perdido todas tus vidas! Fin del juego.")
        exit()