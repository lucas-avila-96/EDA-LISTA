
from src.Lista import Lista


if __name__ == '__main__':
    lista = Lista()
    for i in range(5):
        lista.insertar(i, i + 1)

    lista.recorrer()

    print(f'Posicion: {lista.buscar(3)}')

    

