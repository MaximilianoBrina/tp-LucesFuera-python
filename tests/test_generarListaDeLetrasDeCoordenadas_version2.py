from tableros import *
import unittest

tamanoDeTablero = 8

class test_generarListaDeLetrasDeCoordenadas(unittest.TestCase):

    def test_funcionDevuelveUnaLista(self):
        self.assertIsInstance(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio_version2(tamanoDeTablero), list)

    def test_funcionDevuelve_listaCuyaCantidadDeElementosEsIgualAlTamanoDelTableroIngresado(self):
        self.assertEqual(len(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio_version2(tamanoDeTablero)), 8)

    def test_funcionDevuelve_a_primerValorDeLaLista(self):
        self.assertEqual(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio_version2(tamanoDeTablero)[0], "a")

    def test_funcionDevuelve_e_ultimoValorDeLaLista(self):
        self.assertEqual(generacionDeTableros.generarListaDeLetrasDeCoordenadasDeTableroAleatorio_version2(tamanoDeTablero)[4], "e")
