# Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los elementos de la lista
def suma_lista(lista):
    return sum(lista)

def inverso_palabra(palabra):
    return palabra[::-1]

def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

numeros = input("Ingrese una lista de números separados por espacios: ").split()
numeros = [int(num) for num in numeros]

print("La suma de los números pares es:", suma_pares(numeros))