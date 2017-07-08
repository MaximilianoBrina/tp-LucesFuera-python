import os

from datos import leerDAT
from modulosOperativos import dinamicaDelJuego
from modulosOperativos import opcionesDelUsuario
from tableros import *

valorDelamparaEncendida = int(leerDAT.leerDAT("puntaje", "lamparaEncendida")) #int(linecache.getline("configuracion.dat", 17)[0:3])
tableros = []
tableroEnJuego = {}
nivelEnJuego = 0


def inicioDelJuego(modo):
    """en donde se definen las variables de inicio..."""
    global turnos, nivelEnJuego, tableros, dimensionFilaDeTablero
    if modo == "predeterminado":
        dimensionFilaDeTablero = int(leerDAT.leerDAT("modoPredeterminado", "dimensionDeTablero"))
        tableros = generacionDeTableros.tablerosModoPredeterminado(dimensionFilaDeTablero)
        turnos = definirCantidadDeTurnos()
        nivel = 0
        desarrolloDelJuego(nivel)
    if modo == "aleatorio":
        dimensionFilaDeTablero = int(opcionesDelUsuario.menuModoAleatorio())
        tableros = generacionDeTableros.tablerosModoAleatorio(dimensionFilaDeTablero)
        turnos = definirCantidadDeTurnos()
        nivelEnJuego = 0
        desarrolloDelJuego(nivelEnJuego)


def definirCantidadDeTurnos():
    """la funcion define cantidad de turnos a partir de multiplicar dimension de linea de tablero  (que se obtiene de la division
    del total de elementos -lamparas- por su raiz cuadrada- por 3, de acuerdo a la captura de datos (lease 'pdf de Rosita')"""
    factorDeDefinicionDeTurnos = int(leerDAT.leerDAT("variablesDeInicio", "multiplicadorDeTurnos"))
    turnos = dimensionFilaDeTablero * factorDeDefinicionDeTurnos
    return turnos


def desarrolloDelJuego(nivelEnJuego):
    global turnos, tableros
    os.system("cls")
    turno = 1
    puntosDeNivel = 0
    tableroEnJuego = tableros[nivelEnJuego]
    for i in range(int(turnos)):
        dinamicaDelJuego.impresionDelTableroDeJuego.imprimirEncabezadoDelTablero(nivelEnJuego)
        dinamicaDelJuego.impresionDelTableroDeJuego.imprimirTurnoEnJuegoYTurnosRestantes(turno, turnos)
        dinamicaDelJuego.impresionDelTableroDeJuego.imprimirTableroDeJuego(dimensionFilaDeTablero, tableroEnJuego)
        dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario(opcionesDelUsuario.opcionDelUsuarioCoordenadas(puntosDeNivel), tableroEnJuego)
        puntosDeNivel = (int(lucesPrendidas(tableroEnJuego)) * valorDelamparaEncendida)
        if i == (int(turnos) - 1):
            dinamicaDelJuego.resultadosYEstados.perdedorSinMovimientos()
        if puntosDeNivel == 0:
            dinamicaDelJuego.resultadosYEstados.ganadorTodoApagado()
        turno += 1
        os.system("cls")
    nivelEnJuego += 1


def lucesPrendidas(tablero):
    return (list(tablero.values())).count(leerDAT.leerDAT("variablesDeInicio", "caracterDeLamparaEncendida"))


def mostrarMenuInicial():
    opcionesDelUsuario.opcionDelUsuarioMenuInicial()