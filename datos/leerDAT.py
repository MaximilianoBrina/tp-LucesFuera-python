def leerDAT(seccion, clave):
    import configparser
    config = configparser.ConfigParser()
    config.read('datos/lucesFuera.dat')
    return config[seccion][clave]


#print(leerDAT("modoPredeterminado","dimensionDeTablero"))
#print(leerDAT('modoPredeterminado','ingresosValidos').split(","))

