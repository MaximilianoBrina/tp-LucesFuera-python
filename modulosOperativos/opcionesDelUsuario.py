import os

from datos import logger, leerDAT
from modulosOperativos import estructuraDelJuego
from modulosOperativos.dinamicaDelJuego import *
from modulosOperativos.tableros import *
from multimedia import *


def opcionDelUsuarioMenuInicial():
    global modo
    opcionInicial = True
    while opcionInicial:
        os.system("cls")
        graficos.pantallaDeMenu()
        print("""
        1.Jugar Modo Predeterminado
        2.Jugar Modo Aleatorio
        3.Salir
        """)
        opcionInicial = input("Seleccionar opcion: ")
        if opcionInicial == "1":
            modo = "predeterminado"
            estructuraDelJuego.inicioDelJuego("predeterminado")
        elif opcionInicial == "2":
            modo = "aleatorio"
            estructuraDelJuego.inicioDelJuego("aleatorio")
        elif opcionInicial == "3":
            print("Amargo!!!")
            quit()
        elif opcionInicial != "":
            print("\n Opcion invalida. Reintentar")


def menuModoAleatorio():
    """menu del modo aleatorio, recoge la dimension del tablero a traves del input del usuario"""
    global opcionInicialAleatoria
    graficos.pantallaDeMenu()
    print("Menu Modo Aleatorio")
    opcionInicialAleatoria = True
    while opcionInicialAleatoria:
        opcionInicialAleatoria = (input("Seleccionar las dimensiones del tablero de juego entre 5 y 10 luces por linea o ingresar 'RE' para volver al menu principal: ")).upper()
        if opcionInicialAleatoria in dimensionesAleatoriasValidas():
            return opcionInicialAleatoria
        elif opcionInicialAleatoria == "RE":
            opcionDelUsuarioMenuInicial()
        elif opcionInicialAleatoria != "":
            print("\n Opcion invalida. Reintentar")


def opcionDelUsuarioCoordenadas(puntosDeNivel):
    """recibe y valida el input del usuario"""
    global modo, opcionInicialAleatoria
    if modo == "predeterminado":
        letrasValidas = leerDAT.leerDAT("modoPredeterminado", "ingresosValidos").split(",") #letrasValidas = coordenadasDeValidacion(int(leerDAT.leerDAT("modoPredeterminado", "dimensionDeTablero")))
    else:
        letrasValidas = coordenadasAleatoriasValidas()
    while True:
        opcion = (input("Elegir una celda del tablero usando LETRAS para las filas y NUMEROS para las columnas (ej: A3). O 'RE' para reiniciar o 'SA' para salir: ")).lower()
        if opcion in letrasValidas:
            if opcion == "re":
                resultadosYEstados.reiniciarNivel(puntosDeNivel)
            elif opcion == "sa":
                logger.guardar("El usuario arrugo", "")
                resultadosYEstados.abandonarJuego()
            else:
                return opcion
        else:
            logger.guardar("El usuario mando fruta: ", opcion)
            print("Entrada invalida. Reintentar")


def dimensionesAleatoriasValidas():
    dimensionesValidas = []
    for i in range(5, 11):
        dimensionesValidas.append(str(i))
    return dimensionesValidas


def coordenadasAleatoriasValidas():
    listaDeCoordenadas = generacionDeTableros.generarListaDeCoordenadas(opcionInicialAleatoria)
    coordenadasAleatorias = ["re","sa"]
    for i in range(0, len(listaDeCoordenadas)):
        coordenadasAleatorias.append((listaDeCoordenadas[i][0]) + str(listaDeCoordenadas[i][1]))
    return coordenadasAleatorias
