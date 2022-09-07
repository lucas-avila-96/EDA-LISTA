from src.classNodo import Nodo
import numpy as np


class Lista:
    __arreglo = None
    __disponible = 0
    __comienzo = -1

    def __init__(self, max):
        self.__arreglo = np.empty(max, dtype=Nodo)
        self.__max = max
        for i in range(max - 1):
            nodo = Nodo(None)
            nodo.setNext(i + 1)
            self.__arreglo[i] = nodo
        nodo = Nodo(None)
        nodo.setNext(-1)
        self.__arreglo[max - 1] = nodo

    def insertar(self, item, pos):
        
    



    