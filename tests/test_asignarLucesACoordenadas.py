from tableros import *
import unittest

coordenadasDeTableroAleatorio=[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('d', 0), ('d', 1), ('d', 2), ('d', 3), ('d', 4), ('d', 5), ('e', 0), ('e', 1), ('e', 2), ('e', 3), ('e', 4), ('e', 5), ('f', 0), ('f', 1), ('f', 2), ('f', 3), ('f', 4), ('f', 5)]

class test_asignarLucesACoordenadas(unittest.TestCase):

    def test_funcionDevuelveUnDiccionario(self):
        self.assertIsInstance(generacionDeTableros.asignarLucesACoordenadas(coordenadasDeTableroAleatorio), dict)

    def test_funcionDevuelve_diccionarioDe36Elementos(self):
        self.assertEqual(len(generacionDeTableros.asignarLucesACoordenadas(coordenadasDeTableroAleatorio)), 36)

    def test_confirmaQueTodasLasKeysDelDiccionarioSonLetras(self):
        listaDeKeys=list((generacionDeTableros.asignarLucesACoordenadas(coordenadasDeTableroAleatorio)).keys())
        for key in listaDeKeys:
            self.assertTrue(type(key) != int)

    def test_confirmaQueTodosLosValoresDelDiccionarioSonEncendidoOApagado(self): #encendido = "0", apagado = "."
        listaDeValores = list((generacionDeTableros.asignarLucesACoordenadas(coordenadasDeTableroAleatorio)).values())
        listaDeComprobacion = []
        for valor in listaDeValores:
            if valor == "0" or valor == ".":
                listaDeComprobacion.append(valor)
        self.assertEqual(len(listaDeValores), len(listaDeComprobacion))