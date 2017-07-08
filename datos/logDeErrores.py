import datetime

error = ""

def abrir(nombre_log):
	archivo_log = open(nombre_log, "a")
	guardar(archivo_log,"Iniciando registro de errores", error)
	return archivo_log

def guardar(archivo_log, mensaje, error):
	hora_actual = str(datetime.datetime.now())
	archivo_log.write("[{}] {} {} \n".format(hora_actual, mensaje, error))


def cerrar(archivo_log):
	guardar(archivo_log, "Fin del registro de errores", error)
	archivo_log.close()