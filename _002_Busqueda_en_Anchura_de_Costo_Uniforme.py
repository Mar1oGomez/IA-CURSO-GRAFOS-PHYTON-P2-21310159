import heapq #proporciona implementaciones de colas de prioridad

class Grafo: #defines una clase
    def __init__(self): #define el metodo de inicializacion de la clase,es un atributo vacio
        self.grafo = {}

    def agregar_arista(self, u, v, peso): #define metodo para agregar arista entre u y v
        if u not in self.grafo: #agrega el nodo u el grafo
            self.grafo[u] = [] #agrega una tupla a la lista de adyacencia del nodo u
        self.grafo[u].append((v, peso))

    def bfs_costo_uniforme(self, inicio, objetivo): #metodo de busqueda
        cola = [(0, inicio)]  # Inicializar la cola de prioridad con el nodo de inicio y su costo
        visitado = set()  # Conjunto para almacenar nodos visitados

        while cola:#comienza un bucle mientras haya elementos
            costo, nodo = heapq.heappop(cola)  # Extraer el nodo con el menor costo de la cola
            if nodo == objetivo: #verifica si el nodo actual es el objetivo
                return costo  # Devolver el costo si se alcanza el objetivo
            if nodo not in visitado:
                visitado.add(nodo)  # Marcar el nodo como visitado
                for vecino, peso in self.grafo.get(nodo, []):
                    if vecino not in visitado:
                        heapq.heappush(cola, (costo + peso, vecino))  # Agregar vecinos a la cola de prioridad

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B', 4)
grafo.agregar_arista('A', 'C', 2)
grafo.agregar_arista('B', 'C', 5)
grafo.agregar_arista('B', 'D', 10)
grafo.agregar_arista('C', 'D', 3)

# Realizar la busqueda en anchura de costo uniforme
costo = grafo.bfs_costo_uniforme('A', 'D')
print("Costo minimo de A a D:", costo)
