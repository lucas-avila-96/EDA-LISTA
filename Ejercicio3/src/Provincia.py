
class Provincia:
    __nombre = ''
    __sup_afectada = ''

    def __init__(self, nombre, sup):
        self.__nombre = nombre
        self.__sup_afectada = sup

    def getSuperficie(self):
        return self.__sup_afectada

    def getNombre(self):
        return self.__nombre
    
    def acumular(self, n):
        self.__sup_afectada += n