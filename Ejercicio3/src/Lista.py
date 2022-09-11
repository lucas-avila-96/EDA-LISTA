
from src.classNodo import Nodo

class Lista:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None

    def primerElemento(self):
        return self.__comienzo.getDato()
    
    def ultimoElemento(self):
        aux = self.__comienzo
        while aux != None:
            ret = aux
            aux=aux.getSiguiente()
        return ret.getDato()

    def siguiente(self, pos):
        pass

    def anterior(self):
        pass

    def insertar(self, item):
        nodo = Nodo(item)

        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            anterior = None
            encontrado = False
            while actual != None and not encontrado:
                prov = actual.getDato()
                if item.getNombre() == prov.getNombre():
                    encontrado = True
                anterior = actual
                actual = actual.getSiguiente()
            if encontrado:
                prov.actualizarSuperficie(item.getSuperficie())
            else:
                anterior.setSiguiente(nodo)
                nodo.setSiguiente(actual)
    
    def ordenar():
        pass
        
    def suprimir(self, item):
        actual = self.__comienzo
        anterior = None
        encontrado = False
        while actual is not None and not encontrado:
            if actual.getDato() is item:
                encontrado = True
            else:
                anterior = actual
                actual = actual.getSiguiente()
        if encontrado:
            if anterior is None:
                self.__comienzo = actual.getSiguiente()
            else:
                anterior.setSiguiente(actual.getSiguiente())
        

    def recorrer(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux=aux.getSiguiente()

    def esVacia(self):
        return self.__comienzo is None

    def buscar(self, item):
        actual = self.__comienzo
        pos = 0
        encontrado = False
        while actual is not None and not encontrado:
            if actual.getDato() is item:
                encontrado = True
            else:
                actual = actual.getSiguiente()
                pos += 1
        if not encontrado:
            pos = None
        return pos