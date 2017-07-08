import tableros.generacionDeTableros
import unittest

dimensionFilaDeTablero = 26

class test_rangoDeLetrasAZminuscula(unittest.TestCase):

    def test_funcionDevuelveUnaLista(self):
        self.assertIsInstance(tableros.generacionDeTableros.rangoDeLetrasAZminuscula(dimensionFilaDeTablero), list)

    def test_funcionDevuelve_listaDe26Elementos(self):
        self.assertEqual(len(tableros.generacionDeTableros.rangoDeLetrasAZminuscula(dimensionFilaDeTablero)), 26)

    def test_funcionDevuelve_a_primerValorDeLaLista(self):
        self.assertEqual(tableros.generacionDeTableros.rangoDeLetrasAZminuscula(dimensionFilaDeTablero)[0], "a")

    def test_funcionDevuelve_LetraCorrespondienteAlValorIngresado(self):
        self.assertEqual(tableros.generacionDeTableros.rangoDeLetrasAZminuscula(dimensionFilaDeTablero)[4], "e")

    def test_funcionDevuelve_UltimoValorEs_Z_(self):
        self.assertEqual(tableros.generacionDeTableros.rangoDeLetrasAZminuscula(dimensionFilaDeTablero)[25], "z")
