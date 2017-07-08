from tableros import *

nivel = 0
nivelEnJuego = 0
puntos = 0
tableroEnJuego = {}

def imprimirEncabezadoDelTablero(nivelEnJuego):
    """la funcion imprime el encabezado de la pantalla de juego"""
    print("Modo Predeterminado :: Nivel ", (nivelEnJuego + 1))


def imprimirTurnoEnJuegoYTurnosRestantes(turno,turnos):
    """la funcion imprime el turno actual y los restantes"""
    print("Turno ", turno, ", quedan ", ((int(turnos) - turno)))


def imprimirTableroDeJuego(dimensionFilaDeTablero,tableroEnJuego):
    """la funcion imprime en pantalla el tablero de juego"""
    print(impresionDeTableroEnPantalla.generaEncabezadoDeTablero(dimensionFilaDeTablero))
    print(impresionDeTableroEnPantalla.generalineasDeTablero(dimensionFilaDeTablero))
    for i in range(dimensionFilaDeTablero):
        print(' '.join(str(linea) for linea in (impresionDeTableroEnPantalla.generafilasRestantesDeTablero(dimensionFilaDeTablero, tableroEnJuego)[i])))
    print(impresionDeTableroEnPantalla.generalineasDeTablero(dimensionFilaDeTablero))