from datos import logger


def validacionDeFuncionLectoraDeArchivo(tableros):
    numeroTotalDeElementosEsCuadrado(tableros)
    totalLucesDivididoPorTotalDeTableros(tableros)
    return True

def numeroTotalDeElementosEsCuadrado(tableros):
    """la funcion confirma que el nro. de elementos (luces) de cada uno de los tableros predeterminados recuperadas del archivo de tableros
    sea un nro. cuadrado resultante de un nro. analogo de elementos en el eje vertical y horizontal (ej: 5x5, 3x3, 7x7, etc"""
    for i in range(len(tableros)): #metodo 2 -evalua total de elementos-: ''.join(tableros)
        extensionDeTableroFloat = (len(tableros[i])) ** 0.5 #math.sqrt(len(tableros[i]))
        extensionDeTableroInt = int(extensionDeTableroFloat)
        if extensionDeTableroFloat != extensionDeTableroInt:
            return mensajeDeError()
    return True


def totalLucesDivididoPorTotalDeTableros(tableros):
    """la funcion confirma que la division del total de elementos (luces) por el nro. de listas (tableros) devuele un entero y, de esa,
    forma, que es regular"""
    totalDeElementos = len(''.join(tableros))
    cantidadDeTableros = len(tableros)
    if totalDeElementos/cantidadDeTableros != int(totalDeElementos/cantidadDeTableros):
        return mensajeDeError()
    return True


def mensajeDeError():
    mensajeErrorLecturaDeArchivo = "Archivo de configuracion corrupto. Comuniquese con soporte_tecnico@llamaquetevanaatender.com"
    logger.guardar("El usuario mando fruta: ", )
    print(mensajeErrorLecturaDeArchivo)

