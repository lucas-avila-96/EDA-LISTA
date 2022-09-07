from src.secuencial.Lista import ListaSecuencialPorContenido
from src.encadenada.Lista import ListaEncadendaPorContenido

if __name__ == '__main__':
    lista = ListaSecuencialPorContenido(10)
    #ordenada por contenido de mayor a menor
    lista.insertar(1)
    lista.insertar(5)
    lista.insertar(2)
    lista.insertar(3)
    lista.insertar(4)

    lista.recorrer()

    print('\n')

    lista2 = ListaEncadendaPorContenido()

    lista2.insertar('a')
    lista2.insertar('d')
    lista2.insertar('f')
    lista2.insertar('b')
    lista2.insertar('e')
    lista2.insertar('c')


    lista2.recorrer()

    