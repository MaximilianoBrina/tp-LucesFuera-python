def pantallaDeMenu():
    with open("multimedia\graficos.dat") as archivo:
        for i, linea in enumerate(archivo):
            linea = linea.rstrip("\n")
            print(linea)