import unittest


#letrasCoordenadasDelTablero = ["a","b","c","d","e","f"]
#dimensionFilaDeTablero = 6

class test_generarLamparaAleatoria(unittest.TestCase):

    def test_funcionDevuelve_ResultadosDiferentes(self):
        listaDeResultados1 = []
        listaDeResultados2 = []
        for resultado in range(50):
            listaDeResultados1.append(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria())
            listaDeResultados2.append(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria())
        self.assertNotEqual(listaDeResultados1, listaDeResultados2)

    def test_funcionDevuelve_ResultadosAleatorios_v2(self):
        porcentajeDeResultadosIguales=[]
        for i in range(100):
            listaDeResultados1 = []
            listaDeResultados2 = []
            for resultado in range(100):
                listaDeResultados1.append(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria())
                listaDeResultados2.append(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria())
            resultadosIguales=[]
            for indice in range(len(listaDeResultados1)):
                if listaDeResultados1[indice] == listaDeResultados2[indice]:
                    resultadosIguales.append(listaDeResultados1[indice])
            if len(resultadosIguales) < 40:
                porcentajeDeResultadosIguales.append(1)
        self.assertTrue(len(porcentajeDeResultadosIguales) < 60)


    def test_funcionDevuelve_ResultadosAleatorios_v1(self):
        listaDeResultados1 = []
        listaDeResultados2 = []
        for resultado in range(100):
            listaDeResultados1.append(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria())
            listaDeResultados2.append(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria())
        resultadosIguales=[]
        for indice in range(len(listaDeResultados1)):
            if listaDeResultados1[indice] == listaDeResultados2[indice]:
                resultadosIguales.append(listaDeResultados1[indice])
        self.assertTrue(len(resultadosIguales) < 60)


    def test_funcionDevuelve_soloUnElemento(self):
        self.failIf(len(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria()) != 1)


    def test_funcionDevuelve_soloEncendidoOApagado(self): #encendido=0, apagado=.
        listaDeResultados1 = []
        for resultado in range(50):
            listaDeResultados1.append(modulosOperativos.tableros.generacionDeTableros.generarLamparaAleatoria())
        niEncencidoNiapagado=[]
        for elemento in listaDeResultados1:
            if elemento != "." or "0":
                niEncencidoNiapagado.append(elemento)
        self.assertTrue(len(niEncencidoNiapagado), 0)
