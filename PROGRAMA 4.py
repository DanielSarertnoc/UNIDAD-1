def parentbala(cadena):
    PILA = []                        #SE ALMACENAN LOS PARENTESIS


    #interaciones para comenzar con los parentesis
    for sim in cadena:
        if sim == '(':     
            PILA.append(sim)
        elif sim == ')':
            if len(PILA) == 0:
                return False
            else:
                PILA.pop()


    return len(PILA) == 0


c1 = input("Cadena1: ")
c2 = input("Cadena2: ")
c3 = input("Cadena3: ")
c4 = input("Cadena4: ")
c5 = input("Cadena5: ")

#Por medio de los print comprobamos si las cadenas estan balanceadas o no para mostrarlas
print("Cadena 1 correcta y balanceada:", parentbala(c1))
print("Cadena 2 correcta y balanceada:", parentbala(c2))
print("Cadena 3 correcta y balanceada:", parentbala(c3))
print("Cadena 4 correcta y balanceada:", parentbala(c4))
print("Cadena 5 correcta y balanceada:", parentbala(c5))
