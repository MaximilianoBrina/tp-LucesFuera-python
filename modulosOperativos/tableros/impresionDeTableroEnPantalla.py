import modulosOperativos


def imprimirTableroDeJuego(dimensionFilaDeTablero,tableroEnJuego):
    """la funcion imprime en pantalla el tablero de juego"""
    print(generaEncabezadoDeTablero(dimensionFilaDeTablero))
    print(generalineasDeTablero(dimensionFilaDeTablero))
    for i in range(dimensionFilaDeTablero):
        print(' '.join(str(linea) for linea in (generafilasRestantesDeTablero(dimensionFilaDeTablero, tableroEnJuego)[i])))
    print(generalineasDeTablero(dimensionFilaDeTablero))


def generaEncabezadoDeTablero(dimensionFilaDeTablero):
    """la funcion devuelve la primera fila del tablero de juego a partir de su extension"""
    EncabezadoDeTablero=[" ", " "]
    for i in range(dimensionFilaDeTablero):
        EncabezadoDeTablero.append(str(i))
    EncabezadoDeTablero = ' '.join(EncabezadoDeTablero)
    return EncabezadoDeTablero


def generalineasDeTablero(dimensionFilaDeTablero):
    """la funcion devuelve la segunda y ultima fila del tablero de juego a partir de su extension"""
    lineasDeTablero=[" ", " "]
    for i in range(dimensionFilaDeTablero):
        lineasDeTablero.append("_")
    lineasDeTablero = ' '.join(lineasDeTablero)
    return lineasDeTablero


def generafilasRestantesDeTablero(dimensionFilaDeTablero,tableroEnJuego):
    """la funcion devuelve las filas restantes, de la tercera en adelante, del tablero de juego a partir de su extension"""
    lamparasDeTableroDeJuego = list(reversed(list(tableroEnJuego.values())))
    lamparasDeTableroDeJuego = ([lamparasDeTableroDeJuego[i:i + dimensionFilaDeTablero] for i in range(0, len(lamparasDeTableroDeJuego), dimensionFilaDeTablero)])
    filasRestantes=[]
    contador = 0
    letras = [''.join(letra) for letra in
              list([letra for letra in rangoDeLetras] for rangoDeLetras in (reversed(
                  modulosOperativos.tableros.generacionDeTableros.rangoDeLetrasAZminuscula(dimensionFilaDeTablero))))]
    for i in letras:
        filaDeTablero = ["|", "|"]
        filaDeTablero.insert(0, i)
        for i in range(dimensionFilaDeTablero):
            filaDeTablero.insert(2, lamparasDeTableroDeJuego[contador][i])
        contador += 1
        filasRestantes.append(list(filaDeTablero))
    return list(reversed(list(filasRestantes)))