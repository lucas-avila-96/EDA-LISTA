import csv
from src.Lista import Lista
from src.Provincia import Provincia


if __name__ == '__main__':
    lista = Lista(200)
    archivo = open('Ejercicio3/file.csv')
    reader = csv.reader(archivo, delimiter=';')
    next(reader)
    for fila in reader:
        provincia = Provincia(fila[3], fila[6])
        lista.insertar(provincia)
    lista.recorrer()
    archivo.close()