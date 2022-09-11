import csv
from src.Lista import Lista
from src.Designacion import Designacion

if __name__ == '__main__':
    lista = Lista()
    archivo = open('Ejercicio4/file.csv')
    reader = csv.reader(archivo, delimiter=',')
    next(reader)
    for fila in reader:
        designacion = Designacion(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
        lista.agregar(designacion)
    archivo.close()
    #cantidad de mujeres designadas en ese cargo por año.
    #Leer una materia, un cargo y un año y mostrar la cantidad de agentes designados en ese cargo, esa materia en ese año.

    materia = input('Materia: ')
    cargo2 = input('Cargo: ')
    anio = input('Año: ')

    cantDesignados = lista.cantDesignadosMatCargoAnio(materia, cargo2, anio)
    print(f'Cantidad designados: {cantDesignados}')
    
    cargo = input('Cargo: ')
    cantMujeres = lista.mujeresDesignadasCargo(cargo)
    print(f'Cantidad de mujeres {cantMujeres}')

    