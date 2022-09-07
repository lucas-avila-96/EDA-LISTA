import numpy as np


class Lista:
    __items = None
    __numItems = 0
    __max = 0

    def __init__(self, max):
        self.__items = np.empty(max, int)
        self.__max = max
        self.__numItems = 0

    def validarPosicion(self, p):
        ret = False
        if p >= 1 and p <= self.__numItems:
            ret = True
        return ret

    def primeraPosicion(slef):
        return 1
    
    def ultimaPosicion(self):
        return self.__numItems

    def insertar(self, item, index): 
        if self.__numItems <= self.__max:
            if index >= 1 and index <= self.__numItems + 1:
                for pos in range(self.__numItems, index - 1, - 1):
                    self.__items[pos + 1] = self.__items[pos]
                self.__items[index] = item
            self.__numItems += 1

    def suprimir(self, index):
        ret = None
        if self.vacia():
            pass
        else:
            if index >= 1 and index <= self.__numItems:
                ret = self.recuperar(index)
                for pos in range(index, self.__numItems):
                    self.__items[pos] = self.__items[pos + 1]
                self.__numItems -= 1
        return ret

    def recuperar(self, index):
        if index >= 1 and index <= self.__numItems:
            return self.__items[index]
                
    def vacia(self):
        return self.__numItems == 0

    def buscar(self, item):
        ret = None
        i = 1
        encontrado = False
        if not self.vacia():
            while i < self.__numItems and not encontrado:
                if item == self.__items[i]:
                    ret = i
                    encontrado = True
                i += 1
        return ret

    def primerElemento(self):
        if not self.vacia():
            return self.__items[1]

    def ultimoElemento(self):
        if not self.vacia():
            return self.__items[self.__numItems]

    def siguiente(self, index):
        if index >= 1 and index <= self.__numItems:
            p1 = index + 1
        return p1

    def anterior(self, index):
        if index >= 1 and index <= self.__numItems:
            p1 = index - 1
        return p1

    def recorrer(self):
        for i in range(1, self.__numItems + 1):
            print(self.__items[i])

