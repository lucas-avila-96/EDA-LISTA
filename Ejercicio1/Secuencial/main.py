from src.Lista import Lista


if __name__ == '__main__':
    lista = Lista(10)

    lista.insertar('a', 1)
    lista.insertar('b', 2)
    lista.insertar('c', 3)
    lista.insertar('d', 4)

    lista.suprimir(3)
    item = 'b'
    print(f'Posicion: {lista.buscar(item)}')
    
    print(f'primer elemento {lista.primerElemento()}')
    print(f'ultimo elemento {lista.ultimoElemento()}')

    lista.recorrer()