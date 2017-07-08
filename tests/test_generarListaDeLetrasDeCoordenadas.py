import unittest

from modulosOperativos.tableros import *

tamanoDeTablero = 8

class test_generarListaDeLetrasDeCoordenadas(unittest.TestCase):

    def test_funcionDevuelveUnaLista(self):
        self.assertIsInstance(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio(tamanoDeTablero), list)

    def test_funcionDevuelve_listaCuyaCantidadDeElementosEsIgualAlTamanoDelTableroIngresado(self):
        self.assertEqual(len(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio(tamanoDeTablero)), 8)

    def test_funcionDevuelve_a_primerValorDeLaLista(self):
        self.assertEqual(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio(tamanoDeTablero)[0], "a")

    def test_funcionDevuelve_e_ultimoValorDeLaLista(self):
        self.assertEqual(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio(tamanoDeTablero)[4], "e")
