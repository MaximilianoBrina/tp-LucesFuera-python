from tableros import *
import unittest

tamanoDeTablero=6
letrasCoordenadasDelTablero=["a","b","c","d","e","f"]

class test_generarListaDeCoordenadas(unittest.TestCase):

    def test_funcionDevuelveUnaLista(self):
        self.assertIsInstance(generacionDeTableros.generarListaDeCoordenadas(tamanoDeTablero, letrasCoordenadasDelTablero), list)

    def test_funcionDevuelve_listaDe36Elementos(self):
        self.assertEqual(len(generacionDeTableros.generarListaDeCoordenadas(tamanoDeTablero, letrasCoordenadasDelTablero)), 36)

    def test_funcionDevuelve_a_primerValorDeLaLista(self):
        self.assertEqual(generacionDeTableros.generarListaDeCoordenadas(tamanoDeTablero, letrasCoordenadasDelTablero)[0], ('a', 0))

    def test_funcionDevuelve_e_ultimoValorDeLaLista(self):
        self.assertEqual(generacionDeTableros.generarListaDeCoordenadas(tamanoDeTablero, letrasCoordenadasDelTablero)[35], ('f', 5))
