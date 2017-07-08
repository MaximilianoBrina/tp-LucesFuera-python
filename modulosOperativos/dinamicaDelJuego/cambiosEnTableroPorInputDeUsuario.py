from datos import leerDAT
from tableros import *


nivel = 0
nivelEnJuego = 0
puntos = 0
tableroEnJuego = {}

def efectoDelInputDelUsuario(opcion, tableroEnJuego):
    """la funcion ejecuta los 5 cambios correspondientes a la coordenada que ingresa el usuario segun el modelo:
            cambio2
    cambio3 coordenada cambio4
            cambio5
    """
    # descomponer opcion
    letra = opcion[0]
    numero = opcion[1]
    # cambios 1
    interruptorPrenderApagar(opcion, tableroEnJuego)

    # cambio2
    numero2 = str(int(numero) - 1)
    if int(numero2) >= 0:
        interruptorPrenderApagar((letra + numero2), tableroEnJuego)

    # cambio5
    numero5 = str(int(numero)+1)
    if int(numero5) < 5:
        interruptorPrenderApagar((letra + numero5), tableroEnJuego)

    # cambios 3 y 4
    listaDeLetrasValidas = generacionDeTableros.rangoDeLetrasAZminuscula(int(len(tableroEnJuego) ** 0.5))
    #listaDeLetrasValidas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if int((listaDeLetrasValidas.index(letra)) - 1) >= 0:
        letra3 = listaDeLetrasValidas[int(listaDeLetrasValidas.index(letra)) - 1]
        cambio3 = str(letra3) + str(numero)
        interruptorPrenderApagar(cambio3, tableroEnJuego)

    if int((listaDeLetrasValidas.index(letra)) + 1) <= 4:
        letra4 = listaDeLetrasValidas[int(listaDeLetrasValidas.index(letra)) + 1]
        cambio4 = str(letra4) + str(numero)
        interruptorPrenderApagar(cambio4, tableroEnJuego)
    return tableroEnJuego


def interruptorPrenderApagar(cambio, tableroEnJuego):
    """la funcion 'enciende' o 'apaga' las lamparas del tablero a partir de la coordenada ingresada por el usuario"""
    if tableroEnJuego[cambio] == leerDAT.leerDAT("variablesDeInicio", "caracterDeLamparaEncendida"):
        tableroEnJuego[cambio] = leerDAT.leerDAT("variablesDeInicio", "caracterDeLamparaApagada")
    else:
        tableroEnJuego[cambio] = leerDAT.leerDAT("variablesDeInicio", "caracterDeLamparaEncendida")

def dimensionFilaDeTablero(tableroEnJuego):
    """la funcion obtiene la dimension de tablero a partir de la raiz cuadrada del total de sus elementos"""
    dimensionFilaDeTablero = int(len(tableroEnJuego) ** 0.5)
    return dimensionFilaDeTablero
