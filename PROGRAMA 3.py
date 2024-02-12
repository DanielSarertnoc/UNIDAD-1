class Queue:
    def __init__(self):
        self.items = []             #INICIO DE LISTA QUE SERVIRÁ COMO COLA

    def enqueue(self, item):
        self.items.append(item)     #AGREGAMOS DATOS AL FINAL DE LA COLA

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) #DEVULEVE Y QUITA EL PRIMER DATO DE LA COLA
        else:
            return None # SI NO TIENE CONTENIDO NOS DA none

    def is_empty(self):
        return len(self.items) == 0 #REVISA SI ESTA VACIA LA COLA

    def size(self):
        return len(self.items)

# FUNCIÓN DE REVERTIR DATOS - INICIO
def reverse_half_queue(queue):
    obtener = []
    tamaño = queue.size()
    half_size = tamaño // 2

    for _ in range(half_size):
        obtener.append(queue.dequeue())

    while obtener:
        queue.enqueue(obtener.pop())

    for _ in range(tamaño - half_size):
        queue.enqueue(queue.dequeue())

#El usuario podra ingerar sus datos
def get_queue_from_user():
    queue = Queue()
    CantNum = int(input("Cantidad de elementos para la cola: "))
    for n in range(CantNum):
        item = input(f"Ingrese el elemento {n + 1}: ")
        queue.enqueue(item)
    return queue

if __name__ == "__main__":
    queue = get_queue_from_user()
    print("La cola original es:", queue.items)  #IMPRIME LA COLA ORIGINAL

    reverse_half_queue(queue)
    print("Cola revertida:", queue.items) #NOS DA LA COLA REVERTIDA
