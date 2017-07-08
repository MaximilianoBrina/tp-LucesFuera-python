from tableros import *
import unittest

opcionDelUsuario = "7"

class test_tamanoTablero(unittest.TestCase):

    def test_funcionDevuelveNroEntre5Y10(self):
        self.assertNotIn(generacionDeTableros.tamanoTablero(opcionDelUsuario),["5","6","7","8","9","10"])

    def test_funcionDevuelveUnoDeLosNumerosPosibles(self):
        if generacionDeTableros.tamanoTablero(opcionDelUsuario) in ["5","6","7","8","9","10"]:
            self.assertTrue()

