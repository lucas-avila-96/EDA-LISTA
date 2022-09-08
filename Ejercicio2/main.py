from src.ListaCursor import Lista


if __name__ == '__main__':
    l = Lista(10)
    l.insertar('a')
    l.insertar('b')
    l.insertar('c')
    l.insertar('d')

    print('-----')
    l.suprimir('b')

    l.insertar('K')
    l.recorrer()