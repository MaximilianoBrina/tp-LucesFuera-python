import unittest

from modulosOperativos.tableros import *

extensionDeTablero = 3
tableroConLuces = {'a0': '0', 'a1': '.', 'a2': '.', 'b0': '0', 'b1': '0', 'b2': '.', 'c0': '.', 'c1': '0', 'c2': '0'}
tableroResultante=[ ("tableroConLuces['a0']", "tableroConLuces['b0']", "tableroConLuces['c0']"),
                    ("tableroConLuces['a1']", "tableroConLuces['b1']", "tableroConLuces['c1']"),
                    ("tableroConLuces['a2']", "tableroConLuces['b2']", "tableroConLuces['c2']")]

class test_creacionDeTableroAleatorio(unittest.TestCase):

    def test_funcionDevuelveUnaLista(self):
        self.assertIsInstance(impresionDeTableroEnPantalla.formateaElTableroEnLineasDeTuplasParaImprimirloEnPantallaDeJuego(extensionDeTablero, tableroConLuces), list)

    def test_funcionDevuelveUnaListaDeTuplas(self):
        for i in range(extensionDeTablero):
            self.assertIsInstance(impresionDeTableroEnPantalla.formateaElTableroEnLineasDeTuplasParaImprimirloEnPantallaDeJuego(extensionDeTablero, tableroConLuces)[i], tuple)

    def test_confirmaQueLaCantidadDeElementosDeCadaListaInternaCoincideConLaExtensionDelTableroIngresada(self):
        for i in range(extensionDeTablero):
            self.assertEqual(len(impresionDeTableroEnPantalla.formateaElTableroEnLineasDeTuplasParaImprimirloEnPantallaDeJuego(extensionDeTablero, tableroConLuces)[i]), 3)

    def test_confirmaQueLaFuncionDevuelveElTableroEsperado(self):
        for i in range(extensionDeTablero):
            self.assertEqual(impresionDeTableroEnPantalla.formateaElTableroEnLineasDeTuplasParaImprimirloEnPantallaDeJuego(extensionDeTablero, tableroConLuces), tableroResultante)
