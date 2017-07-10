import os

from datos import leerDAT
from modulosOperativos import dinamicaDelJuego
from modulosOperativos import opcionesDelUsuario
from modulosOperativos.tableros import *

valorDelamparaEncendida = int(leerDAT.leerDAT("puntaje", "lamparaEncendida")) #int(linecache.getline("configuracion.dat", 17)[0:3])
tableros = []
tableroEnJuego = {}
nivelEnJuego = int(leerDAT.leerDAT("variablesDeInicio", "nivelEnJuego"))


def inicioDelJuego(modo):
    """en donde se definen las variables de inicio..."""
    global turnos, nivelEnJuego, tableros, dimensionFilaDeTablero
    if modo == "predeterminado":
        dimensionFilaDeTablero = int(leerDAT.leerDAT("modoPredeterminado", "dimensionDeTablero"))
        tableros = generacionDeTableros.tablerosModoPredeterminado(dimensionFilaDeTablero)
        turnos = definirCantidadDeTurnos()
        desarrolloDelJuego(nivelEnJuego)
    if modo == "aleatorio":
        dimensionFilaDeTablero = int(opcionesDelUsuario.menuModoAleatorio())
        tableros = generacionDeTableros.tablerosModoAleatorio(dimensionFilaDeTablero)
        turnos = definirCantidadDeTurnos()
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
    ContadorDeTurnos = int(leerDAT.leerDAT("variablesDeInicio", "valorInicialDeContadorDeTurnos"))
    puntosDeNivel = int(leerDAT.leerDAT("puntaje", "puntajeInicial"))
    tableroEnJuego = tableros[nivelEnJuego]
    for i in range(int(turnos)):
        dinamicaDelJuego.impresionDelTableroDeJuego.imprimirEncabezadoDelTablero(nivelEnJuego)
        dinamicaDelJuego.impresionDelTableroDeJuego.imprimirTurnoEnJuegoYTurnosRestantes(ContadorDeTurnos, turnos)
        dinamicaDelJuego.impresionDelTableroDeJuego.imprimirTableroDeJuego(dimensionFilaDeTablero, tableroEnJuego)
        dinamicaDelJuego.cambiosEnTableroPorInputDeUsuario.efectoDelInputDelUsuario(opcionesDelUsuario.opcionDelUsuarioCoordenadas(puntosDeNivel), tableroEnJuego)
        puntosDeNivel = (int(lucesPrendidas(tableroEnJuego)) * valorDelamparaEncendida)
        if i == (int(turnos) - int(leerDAT.leerDAT("variablesDeInicio", "factorDeCompensacionContadorDeTurnos"))):
            dinamicaDelJuego.resultadosYEstados.perdedorSinMovimientos()
        if puntosDeNivel == 0:
            dinamicaDelJuego.resultadosYEstados.ganadorTodoApagado()
        ContadorDeTurnos += int(leerDAT.leerDAT("variablesDeInicio", "valorDeIncrementoDeTurnos"))
        os.system("cls")
    nivelEnJuego += int(leerDAT.leerDAT("variablesDeInicio", "valorDeIncrementoDeNiveles"))


def lucesPrendidas(tablero):
    return (list(tablero.values())).count(leerDAT.leerDAT("variablesDeInicio", "caracterDeLamparaEncendida"))


def mostrarMenuInicial():
    opcionesDelUsuario.opcionDelUsuarioMenuInicial()