class Nodo:
    __data = None
    __next = None

    def __init__(self, val):
        self.__data = val

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, val):
        self.__data = val

    def setNext(self, val):
        self.__next = val