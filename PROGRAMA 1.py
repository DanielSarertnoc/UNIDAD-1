class Queue:
    def __init__(self):
        self.items = []     #ES LA LISTA QUE USAMOS COMO COLA
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) #ESTO QUITA EL PRIMER DATO Y NOS LO REGRESA
        else:
            return None        # SI NO TIENE CONTENIDO NOS DA none
    def front(self):
        if not self.is_empty():
            return self.items[0]  #REGRESA EL PRIMER ELEMENTO SIN QUITARLO
        else:
            return None
    def is_empty(self):
        return len(self.items) == 0 #REVISA SI ESTA VACIA LA COLA
    def size(self):
        return len(self.items)
    
def proceso_atencion(fila):
    while not fila.is_empty():
        AtenderCliente = fila.dequeue()
        print("Cliento siendo atendido: ", AtenderCliente) #SE ATIENDE AL CLIENTE

def get_queue_from_user():
    queue = Queue()
    numeroDeClientes = int(input("Ingrese el número de clientes para antender: "))
    for i in range(numeroDeClientes):
        nomClientes = input(f"Ingrese el nombre del cliente {i + 1}: ")
        queue.enqueue(nomClientes)
    return queue


if __name__ == "__main__":
    clientes_atendiendo = get_queue_from_user()
    print("Iniciando la atención a clientes: ")
    proceso_atencion(clientes_atendiendo)