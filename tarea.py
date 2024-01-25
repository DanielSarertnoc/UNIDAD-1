print("PROGRAMA PARA PASAR DE GRADOS CELCIUS A FAHRENHEIT.")
cel = int(input("Ingrese la cantidad de grados celciusº: "))
formula = ((cel * (9/5))+32)
print("Fahrenheit:",formula,"Fº")


print("PROGRAMA QUE CALCULE LAS HORAS QUE HAN PASADO EN EL DÍA A SEGUNDOS.")
horas = int(input("Ingrese las horas del día: "))

tiempoS = horas*3600

print("Los segundos que han pasado en",horas,"horas, es de:",tiempoS,"s")


print("PROGRAMA QUE CONVIERTA DIVISAS, DOLARES A QUETZALES")
dolar = int(input("Ingrese los dolares: "))

quet = dolar*7.82

print("La cantidad que tiene en quetzales es de: Q",quet)


print("FORMULA CUADRATICA")
a = int(input("ingrese el valor de A: "))
b = int(input("ingrese el valor de B: "))
c = int(input("ingrese el valor de c: "))
det = ((b*b) - 4 * a * c)

formula1 = (-b + ((det)**1/2))/(2*a)
formula2 = (-b - ((det)**1/2))/(2*a)
print("resultado positivo: ",formula1)
print("resultado negativo: ",formula2)


print("IDENTIFICACIÓN DE UN DATO INGRESADO")

dato = input("Ingrese El Dato a corroborar su naturaleza: ")

try:
    dato_ent = int(dato)
    print("EL DATO ES TIPO ENTERO.")
except ValueError:
    try:
        dato_flot = float(dato)
        print("EL DATO ES TIPO FLOTANTE.")
    except ValueError:
        print("EL DATO ES UNA CADENA DE TEXTO")
