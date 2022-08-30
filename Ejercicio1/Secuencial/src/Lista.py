import numpy as np


class Lista:
    __items = None
    __numItems = 0

    def __init__(self, max):
        self.__items = np.empty(max, str)
        self.__max = max
        self.__numItems = 0

    def insertar(self, item, index):
       if self.__numItems <= self.__max:
            if index >= 1 and index <= self.__numItems + 1:
                for pos in range(self.__numItems, index, -1):
                    self.__items[pos + 1] = self.__items[pos]
                self.__items[index - 1] = item
            self.__numItems += 1

    def suprimir(self, index):
        if index >= 1 and index <= self.__numItems:
            for pos in range(index, self.__numItems):
                self.__items[pos - 1] = self.__items[pos]
            self.__numItems -= 1

    def recuperar(self, p):
        if p >= 1 and p <= self.__numItems:
            return self.__items[p - 1]
                
    def vacia(self):
        return self.__numItems == 0

    def buscar(self, item):
        ret = -1
        i = 0
        if not self.vacia():
            while i < self.__numItems:
                if item == self.__items[i]:
                    ret = i + 1
                i += 1
            return ret

    def primerElemento(self):
        if not self.vacia():
            return self.__items[0]

    def ultimoElemento(self):
        if not self.vacia():
            return self.__items[self.__numItems - 1]

    def siguiente(self, p):
        pass

    def anterior(self):
        pass

    def recorrer(self):
        for i in range(self.__numItems):
            print(self.__items[i])

