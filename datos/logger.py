from datos import logDeErrores

nombre_archivo_log = "errores.txt"
archivo_log = None

def abrir():
    global archivo_log, nombre_archivo_log
    archivo_log = logDeErrores.abrir(nombre_archivo_log)


def guardar(mensaje, error):
    global archivo_log
    logDeErrores.guardar(archivo_log, mensaje, error)


def cerrar():
    global archivo_log
    logDeErrores.cerrar(archivo_log)