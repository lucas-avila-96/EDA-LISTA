
from src.classNodo import Nodo

class Lista:
    __comienzo = None
    __tamano = 0

    def __init__(self):
        self.__comienzo = None
        self.__tamano = 0

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
    
    def agregar(self, item):

        new_node = Nodo(item)
        new_node.setSiguiente(self.__comienzo)
        self.__comienzo = new_node
 

    def insertar(self, pos, item):
        if pos == 0:
            nuevo = Nodo(item)
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        else:
            nuevo = Nodo(item)
            actual = self.__comienzo
            anterior = None
            i = 0
            while i < pos and actual != None:
                i += 1
                anterior = actual
                actual = actual.getSiguiente()
            if i == pos:
                anterior.setSiguiente(nuevo)
                nuevo.setSiguiente(actual)
            else:
                print('Posicion fuera de rango')
    
    def mujeresDesignadasCargo(self, cargo):
        aux = self.__comienzo
        total = 0
        mujeresPorAnio = []
        while aux != None:
            designacion = aux.getDato()
            anio = designacion.getAnio()
            while anio == designacion.getAnio():
                if designacion.getCargo() == cargo:
                    total += int(designacion.getCantMujeres())
            aux = aux.getSiguiente()
            mujeresPorAnio.append((anio, total))
        return total

    def cantDesignadosMatCargoAnio(self, materia, cargo, anio):
        aux = self.__comienzo
        total = 0
        while aux != None:
            designacion = aux.getDato()
            if designacion.getMateria() == materia and designacion.getCargo() == cargo and designacion.getAnio() == anio:
                total += int(designacion.getCantMujeres())
                total += int(designacion.getCantHombres())
            aux = aux.getSiguiente()
        return total
    
    def suprimir(self, position):
        actual = self.__comienzo
        if position == 0:
            self.__comienzo = actual.getSiguiente()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = actual
                actual = actual.getSiguiente()
                pos += 1
            previous.setSiguiente(actual.getSiguiente())

    def recorrer(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

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