import pytest

from Ataques import Fuego as AtaqueFuego, Saltar
from Enemigos import Caminante, Enemigos, Fantasma, Tortuga
from Estados import Fuego, Grande, Pequenio
from Nivel import Nivel
from Objetos import Caja_misteriosa, Hongo
from Observadores import ObservadorPuntos
from Personaje import Personaje


def puntos():
    return [ObservadorPuntos()]


def test_super_plomero_comienza_pequeno():
    assert isinstance(Personaje().estado, Pequenio)


def test_pequeno_con_hongo_pasa_a_grande():
    assert isinstance(Pequenio().potenciar(Hongo()), Grande)


def test_grande_con_hongo_conserva_estado_y_obtiene_100_puntos():
    observadores = puntos()
    estado = Grande()

    resultado = estado.potenciar(Hongo(), observadores)

    assert isinstance(resultado, Grande)
    assert observadores[0].puntos == 100


def test_grande_que_recibe_dano_pasa_a_pequeno():
    assert isinstance(Grande().nuevo_estado(), Pequenio)


def test_fuego_que_recibe_dano_pasa_a_grande():
    assert isinstance(Fuego().nuevo_estado(), Grande)


def test_caja_misterio_entrega_su_objeto_una_sola_vez():
    observadores = puntos()
    caja = Caja_misteriosa(1, Hongo())

    caja.tocar_caja(observadores, Grande())
    assert caja.objeto is None


def test_caminante_es_derrotado_al_saltar_sobre_el():
    caminante = Caminante(1)

    caminante.atacado(Saltar())

    assert caminante.vida == 0


def test_tortuga_queda_en_caparazon_al_primer_salto():
    tortuga = Tortuga(1)

    tortuga.atacado(Saltar())

    assert tortuga.vida == 1


def test_tortuga_es_derrotada_al_segundo_salto():
    tortuga = Tortuga(1)

    tortuga.atacado(Saltar())
    tortuga.atacado(Saltar())

    assert tortuga.vida == 0


def test_fantasma_no_es_derrotado_al_recibir_un_salto():
    fantasma = Fantasma(1)

    fantasma.atacado(Saltar())

    assert fantasma.vida == 1


def test_fantasma_es_derrotado_con_bola_de_fuego():
    fantasma = Fantasma(1)

    fantasma.atacado(AtaqueFuego())

    assert fantasma.vida == 0


def test_derrotar_caminante_otorga_100_puntos():
    caminante = Caminante(1)
    observadores = puntos()

    observadores[0].actualizar(caminante.atacado(Saltar()))

    assert observadores[0].puntos == 100


def test_nivel_con_todos_los_enemigos_derrotados_esta_completado():
    nivel = Nivel("1-1")
    caminante = Caminante(1)
    nivel.agregar_enemigo(caminante)
    caminante.vida = 0

    assert not nivel.quedan_enemigos()


def test_escenario_hongo_y_ataque_de_caminante():
    plomero = Personaje()
    plomero.estado = Pequenio().potenciar(Hongo())
    plomero.recibir_dano()

    assert isinstance(plomero.estado, Pequenio)


def test_caja_usada_no_entrega_nuevamente_su_contenido():
    observadores = puntos()
    caja = Caja_misteriosa(1, Hongo())

    caja.tocar_caja(observadores, Grande())
    puntos_obtenidos = observadores[0].puntos

    assert caja.objeto is None
    assert puntos_obtenidos == 100


def test_plomero_pierde_su_ultima_vida_y_se_interrumpe_el_juego():
    plomero = Personaje()

    with pytest.raises(SystemExit):
        for _ in range(3):
            plomero.recibir_dano()
