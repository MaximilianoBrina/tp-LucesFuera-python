import os

from datos import leerDAT
from modulosOperativos import opcionesDelUsuario
from modulosOperativos.opcionesDelUsuario import *

nivel = 0
nivelEnJuego = 0
puntos = 0
tableroEnJuego = {}

def perdedorSinMovimientos():
    """la funcion avisa al usuario que se quedo sin movimientos, muestra puntaje y nivel adquirido"""
    global puntos, nivelEnJuego
    os.system("cls")
    puntos = int(puntos) + int(leerDAT.leerDAT("puntaje", "ganador")) #int(linecache.getline("configuracion.dat", 23)[0:4]) + puntos
    print("Sin movimientos. Perdiste")
    print("Nivel alcanzado:", nivelEnJuego + 1)
    print("Puntaje final: ", puntos)
    print("")
    input("Ingresar 's' para continuar ")
    opcionesDelUsuario.opcionDelUsuarioMenuInicial()


def ganadorTodoApagado():
    """la funcion avisa al usuario que completo el nivel o los cinco del juego, muestra puntaje y nivel adquirido"""
    os.system("cls")
    global puntos, nivelEnJuego, tableroEnJuego
    puntos = int(puntos) + int(leerDAT.leerDAT("puntaje", "ganador"))
    print("Felicitaciones. Completaste el nivel", nivelEnJuego + 1)
    print("Puntaje parcial: 500")
    print("Puntaje total: ", puntos)
    input("Ingresar 's' para continuar ")
    if nivelEnJuego == 4:
        print("Todos los niveles completados")
        input("Ingresar 's' para continuar ")
        opcionesDelUsuario.opcionDelUsuarioMenuInicial()
    nivelEnJuego = int(nivelEnJuego) + 1
    estructuraDelJuego.desarrolloDelJuego(nivelEnJuego)


def reiniciarNivel(puntosDeNivel):
    """la funcion implementa el reinicio de un nivel, muestra mensaje, nivel y puntaje correspondientes"""
    os.system("cls")
    global puntos, nivelEnJuego, nivel
    puntos = puntos + puntosDeNivel
    print("Reiniciar Nivel ", nivelEnJuego + 1)
    print("Puntos totales: ", puntos)
    print("Puntos de nivel: ", puntosDeNivel)
    input("Ingresar 's' para continuar ")
    estructuraDelJuego.desarrolloDelJuego(nivelEnJuego)


def abandonarJuego():
    """la funcion implementa el abandono del juego, muestra mensaje, nivel y puntaje correspondientes"""
    global puntos, nivelEnJuego
    print("")
    print("Juego abortado")
    print("Nivel alcanzado ", (nivelEnJuego + 1))
    print("Puntaje final: ", puntos)
    print("")
    input("Ingresar 's' para continuar ")
    estructuraDelJuego.mostrarMenuInicial()