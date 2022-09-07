from src.Lista import Lista

if __name__ == '__main__':

    #a)
    l1 = Lista(20)
    l1.insertar(10, 1)
    l1.insertar(5, 2)
    l1.insertar(7, 3)
    l1.insertar(5, 4)
    l1.insertar(2, 5)
    l1.insertar(10, 6)
    
    
    p = l1.primeraPosicion()
    q = l1.ultimaPosicion()

    while p < q:
        q = l1.siguiente(p)
        while q <= l1.ultimaPosicion():
            if l1.recuperar(p) == l1.recuperar(q):
                l1.suprimir(q)
            else:
                q = l1.siguiente(q)
        p = l1.siguiente(p)
    

    l1.recorrer()


    #b) optimizacion para lista ordenada por contenido
    print('\n')
    l2 = Lista(100)
    l2.insertar(10, 1)
    l2.insertar(10, 2)
    l2.insertar(7, 3)
    l2.insertar(7, 4)
    l2.insertar(2, 5)
    l2.insertar(2, 6)

    p2 = l1.primeraPosicion()
    q2 = l1.ultimaPosicion()

    while p2 < l2.ultimaPosicion():
        q2 = l2.siguiente(p2)
        if l2.recuperar(p2) == l2.recuperar(q2):
            l2.suprimir(q2)
        p2 = l2.siguiente(p2)

    l2.recorrer()




