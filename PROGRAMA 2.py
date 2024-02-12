#programa 2
from collections import deque
import time

def lineaEsperaCli(clientes):
    queue = deque(clientes)
    while queue:
        print("Cliente siendo atendido.", queue.popleft())
        time.sleep(2)#Esto hace que espere el tiempo para mostrar en pantalla, para ser atendido

def clienteIngresado():
    clientes = []
    while True:
        cliente = input("Ingrese el nombre de los clientes a ser atendidos (enter para finalizar): ")
        if not cliente:
            break
        clientes.append(cliente)
    return clientes

print("B I E N V E N I D O ")
print("En breves momentos será atendido.")
clientesEsperando = clienteIngresado()
lineaEsperaCli(clientesEsperando)
print("Los clientes han sido atendidos correctamente")
print("Gracias por utilizar el programa")
