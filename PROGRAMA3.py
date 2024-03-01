#Escribe un programa que pida al usuario una lista de números y luego imprima la suma de los números pares en la lista.
def suma_lista(lista):
    return sum(lista)# DEFINIMOS LA CLASE QUE UTILIZAREMOS PARA LA SUMA

def inverso_palabra(palabra):#ESTO NOS INDICARA CUANDO DEBE DE REGRESAR LA PALABRA
    return palabra[::-1]

def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:#AQUÍ ENCONTRARA QUE NÙMERO ES PAR 
            suma += num
    return suma

numeros = input("Ingrese una lista de números separados por espacios: ").split()
numeros = [int(num) for num in numeros]

print("La suma de los números pares es:", suma_pares(numeros))