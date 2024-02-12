def pila1(lista):
    pila1 = []
    print("La pila ha sido creada")
    for elemPi in lista:
        print(f'El elemento  "{elemPi}" esta entrando a la Pila')
        pila1.append(elemPi)
        print(pila1)
    Num = len(pila1) - 1
    print('\n')

    while pila1:
        print(f'El elemento {pila1[Num]} esta saliendo de la Pila')
        Num = Num - 1
        pila1.pop()
        print(pila1)

    while lista:
        final = lista.pop()
        pila1.append(final)

    print("\nLista invertida utilizando: ", pila1)


entrada_usuario = input("Ingrese una lista de números dejando espacio entre ellos: ")
lista = entrada_usuario.split()  # Convertir la entrada en una lista
pila1(lista)