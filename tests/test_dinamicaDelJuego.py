from modulosOperativos import dinamicaDelJuego
from modulosOperativos.dinamicaDelJuego import *
import unittest

tableronivel1 = {   "a1": "0", "b1": "0", "c1": ".", "d1": "0", "e1": "0",
                    "a2": "0", "b2": ".", "c2": "0", "d2": ".", "e2": "0",
                    "a3": ".", "b3": "0", "c3": "0", "d3": "0", "e3": ".",
                    "a4": "0", "b4": ".", "c4": "0", "d4": ".", "e4": "0",
                    "a5": "0", "b5": "0", "c5": ".", "d5": "0", "e5": "0"}


tableroCambioEnCoordeanadaC3 = {    "a1": "0", "b1": "0", "c1": ".", "d1": "0", "e1": "0",
                                    "a2": "0", "b2": ".", "c2": ".", "d2": ".", "e2": "0",
                                    "a3": ".", "b3": ".", "c3": ".", "d3": ".", "e3": ".",
                                    "a4": "0", "b4": ".", "c4": ".", "d4": ".", "e4": "0",
                                    "a5": "0", "b5": "0", "c5": ".", "d5": "0", "e5": "0"}

tableroCambioEnCoordeanadaA5 = {    "a1": "0", "b1": "0", "c1": ".", "d1": "0", "e1": "0",
                                    "a2": "0", "b2": ".", "c2": ".", "d2": ".", "e2": "0",
                                    "a3": ".", "b3": ".", "c3": ".", "d3": ".", "e3": ".",
                                    "a4": ".", "b4": ".", "c4": ".", "d4": ".", "e4": "0",
                                    "a5": ".", "b5": ".", "c5": ".", "d5": "0", "e5": "0"}

class test_Tablero_predeterminado(unittest.TestCase):

    def test_comprueba_que_la_funcion_devuelve_una_lista(self):
        self.assertIs(type(dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("a1", tableronivel1)), dict)

    def test_contrasta_coordenada_LETRA_NRO_Devuelve_True(self):
        self.assertTrue(dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("c3", tableronivel1))

    def test_contrasta_tableros_antes_y_despues_de_la_jugada_y_confirma_efecto_de_la_misma_en_coordenada_angular(self):
        self.assertNotEqual(dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("a5", tableronivel1), tableroCambioEnCoordeanadaA5)

    def test_contrasta_tableros_antes_y_despues_de_la_jugada_y_confirma_efecto_de_la_misma_en_coordenada_central(self):
        self.assertNotEqual(dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("c3", tableronivel1), tableroCambioEnCoordeanadaC3)

    def test_confirma_el_apagado_de_luces_encendidas_y_viceversa_en_las_coordenadas_afectadas(self):
        self.assertNotEqual((dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("c3", tableronivel1)["c2"],
                             dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("c3", tableronivel1)["b3"],
                             dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("c3", tableronivel1)["c3"],
                             dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("c3", tableronivel1)["d3"],
                             dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario("c3", tableronivel1)["c4"]),
                            (tableroCambioEnCoordeanadaC3["c2"],
                            tableroCambioEnCoordeanadaC3["b3"],
                            tableroCambioEnCoordeanadaC3["c3"],
                            tableroCambioEnCoordeanadaC3["d3"],
                            tableroCambioEnCoordeanadaC3["c4"]))