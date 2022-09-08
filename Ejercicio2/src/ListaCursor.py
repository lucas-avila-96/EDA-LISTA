
from src.classNodo import Nodo
import numpy as np


class Lista:
    __cursorespace = None
    __tamano = 0

    def __init__(self, max):
        self.__cursorespace = np.empty(max, dtype=Nodo)
        self.__tamano = max
        for i in range(max - 1):
            nodo = Nodo(None)
            nodo.setNext(i + 1)
            self.__cursorespace[i] = nodo
        nodo = Nodo(None)
        nodo.setNext(0)
        self.__cursorespace[max - 1] = nodo

    def cursoralloc(self):
        p = self.__cursorespace[0].getNext()
        self.__cursorespace[0].setNext(self.__cursorespace[p].getNext())
        return p

    def insertar(self, item):
        tmp = self.cursoralloc()
        if tmp == 0:
            print('Error')
        else:
            nodo = Nodo(item)
            nodo.setNext(self.__cursorespace[0].getNext())
            self.__cursorespace[tmp] = nodo

    
    def cursorLibre(self, p):
        for i in range(self.__cursorespace[p].getNext(), self.__tamano):
            if self.__cursorespace[i].getNext() == self.__cursorespace[0].getNext():
                self.__cursorespace[i].setNext(p)
                break
        self.__cursorespace[p].setNext(self.__cursorespace[0].getNext())
        self.__cursorespace[p].setData(None)
        self.__cursorespace[0].setNext(p)

    def encontrarAnterior(self, x):
        p = 0
        if self.__cursorespace[1].getData() == x:
            return 0
        i = 0
        while x != self.__cursorespace[i].getData():
            i += 1
        p = self.__cursorespace[i].getNext()

        j = 0
        while p != self.__cursorespace[i].getNext():
            j += 1
        
        p = i

        return p
    
    def suprimir(self, x):
        p = self.encontrarAnterior(x)
        if p == 0:
            tmp = 1
            self.cursorLibre(tmp)
        else:
            tmp = self.__cursorespace[p].getNext()
            next = self.__cursorespace[tmp].getNext()
            self.__cursorespace[p].setNext(next)
            self.cursorLibre(tmp)

    def recorrer(self):
        for i in range(self.__tamano):
            print(f'{i}\t{self.__cursorespace[i].getData()}\t {self.__cursorespace[i].getNext()} \n')


    