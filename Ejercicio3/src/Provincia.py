
class Provincia:
    __nombre = ''
    __sup_afectada = 0

    def __init__(self, nombre, sup):
        self.__nombre = nombre
        if sup == '':
            self.__sup_afectada += 0
        else:
            self.__sup_afectada = float(sup)

    def getSuperficie(self):
        return self.__sup_afectada

    def getNombre(self):
        return self.__nombre
    
    def actualizarSuperficie(self, n):
        if n == '':
            self.__sup_afectada += 0
        else:
            self.__sup_afectada += float(n)

    def __str__(self) -> str:
        out = ''
        out += self.__nombre + '\t'
        out += str(self.__sup_afectada) + '\n'
        return out