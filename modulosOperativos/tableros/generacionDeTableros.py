import itertools
from random import randint

import modulosOperativos
from datos import leerDAT


def generarListaDeCoordenadas(dimensionFilaDeTablero):
    """la funcion devuelve la lista de coordenadas (en el formato 'a0', 'a1', etc) que conformaran el tablero a
    partir de la dimension ingresada por el usuario (entre cino y seis) o cinco para el modo predeterminado del juego"""
    numerosCoordenadasDelTablero = list(range(0, int(dimensionFilaDeTablero)))
    coordenadasDeTablero = list(itertools.product(rangoDeLetrasAZminuscula(dimensionFilaDeTablero), numerosCoordenadasDelTablero)) #https://docs.python.org/3/library/itertools.html
    return coordenadasDeTablero

def lucesNivelPredeterminado():
    """la funcion abre y lee el archivo archivoDeTableros.txt que las 125 luces correspondientes los 5 niveles del modo aleatorio en formato
    '0' (encendida) o '.' (apagada), distribuido en cinco lineas (1 linea = 1 nivel predeterminado), devuelve una lista de cinco
    elementos cada uno de los cuales contiene las luces de un nivel del modo predeterminado"""
    with open("modulosOperativos/tableros/archivoDeTableros.txt") as archivoDeTableros:
        lucesDeTablerosModoPredeterminado = []
        for nivel in archivoDeTableros:
            nivel = nivel.rstrip("\n")
            lucesDeTablerosModoPredeterminado.append(nivel)
            modulosOperativos.tableros.validacionDeFuncionLectoraDeArchivo.validacionDeFuncionLectoraDeArchivo(lucesDeTablerosModoPredeterminado)
        return lucesDeTablerosModoPredeterminado


def tablerosModoPredeterminado(dimensionFilaDeTablero):
    """la funcion toma la lista de coordenadas de cada uno de los niveles predeterminados y les asigna la lampara correspondiente
    a partir de la lista de niveles obtenida por la funcion 'lucesNivelesPredeterminado(), devuelve lista de cinco diccionarios
    cada uno de los cuales es un nivel predeterminado"""
    tablerosModoPredeterminado = []
    cantidadNivelesPredeterminados = 5
    nivel = 0
    for i in range(cantidadNivelesPredeterminados):
        coordenadasConLucesPredeterminado = {}
        for i in range(0, len(generarListaDeCoordenadas(dimensionFilaDeTablero))):
            coordenadasConLucesPredeterminado[(str(generarListaDeCoordenadas(dimensionFilaDeTablero)[i][0]) + str(generarListaDeCoordenadas(dimensionFilaDeTablero)[i][1]))] = lucesNivelPredeterminado()[nivel][i]
        nivel += 1
        tablerosModoPredeterminado.append(coordenadasConLucesPredeterminado)
    return tablerosModoPredeterminado

def tablerosModoAleatorio(dimensionFilaDeTablero):
    """la funcion crea lista de cinco diccionarios, cada uno de los cuales es uno de los niveles del modo aleatorio, a partir de la dimension ingresada
    por el usuario"""
    tableros=[]
    cantidadDeNiveles = int(leerDAT.leerDAT("variablesDeInicio", "cantidadDeNiveles"))
    for i in range(cantidadDeNiveles):
        tableros.append(asignarLucesACoordenadas(generarListaDeCoordenadas(dimensionFilaDeTablero)))
    return tableros


def asignarLucesACoordenadas(coordenadasDeTablero):
    coordenadasConLuces = {}
    print("")
    for i in range(0, len(coordenadasDeTablero)):
        coordenadasConLuces[(str(coordenadasDeTablero[i][0]) + str(coordenadasDeTablero[i][1]))] = generarLamparaAleatoria()
    return coordenadasConLuces


def generarLamparaAleatoria():
    """la funcion devuelve las lamparas que se utilizaran en el tablero del modo aleatorio, apagadas o encendidas aleatoriamente"""
    lampara = randint(1, 2)
    if lampara == 1:
        lampara = leerDAT.leerDAT("variablesDeInicio", "caracterDeLamparaEncendida")
    else:
        lampara = leerDAT.leerDAT("variablesDeInicio", "caracterDeLamparaApagada")
    return lampara


def rangoDeLetrasAZminuscula(dimensionFilaDeTablero):
    """la funcion permite devuelve en forma de lista un rango alfabetico en minuscula, de la 'a' a la 'z' (az), para utilizar
    en la generacion de coordenadas del tablero"""
    AZ = []
    for i in range(97, 123):
        AZ.append(chr(i))
    rangoAZ = AZ[0:int(dimensionFilaDeTablero)]
    return rangoAZ

