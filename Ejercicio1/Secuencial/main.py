from src.Lista import Lista


if __name__ == '__main__':
    lista = Lista(10)
    
    lista.insertar('a', 1)
    lista.insertar('b', 2)
    lista.insertar('c', 3)
    lista.insertar('d', 4)
    lista.insertar('e', 5)
    lista.insertar('f', 6)
    lista.insertar('g', 7)

    lista.insertar('E', 4)

    lista.recorrer()
    print('---')
    lista.suprimir(4)
    lista.suprimir(2)
    lista.recorrer()

    item = 'f'
    print(f'Posicion: {lista.buscar(item)}')
    
    print(f'primer elemento {lista.primerElemento()}')
    print(f'ultimo elemento {lista.ultimoElemento()}')

    lista.recorrer()
    '''
    '''