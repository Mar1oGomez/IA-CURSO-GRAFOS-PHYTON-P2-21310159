from collections import deque  # Importar la clase deque desde el modulo collections

class Grafo:  # Definicion de la clase Grafo
    def __init__(self):  # Metodo de inicializacion de la clase
        self.grafo = {}  # Inicializacion del diccionario que representara el grafo

    def agregar_arista(self, u, v):  # Metodo para agregar una arista al grafo
        if u not in self.grafo:  # Verificar si el nodo u no esta en el grafo
            self.grafo[u] = []  # Agregar el nodo u al grafo
        self.grafo[u].append(v)  # Agregar la arista desde u hacia v

    def bfs(self, inicio, objetivo):  # Metodo de busqueda en amplitud
        visitado = set()  # Conjunto para almacenar los nodos visitados
        cola = deque([inicio])  # Cola para los nodos que se van a visitar
        while cola:  # Mientras la cola no este vacia
            nodo_actual = cola.popleft()  # Extraer el primer nodo de la cola
            print(nodo_actual, end=" ")  # Imprimir el nodo actual
            if nodo_actual == objetivo:  # Verificar si se ha encontrado el objetivo
                print("\nEl objetivo", objetivo, "se encontro")  # Imprimir mensaje de exito
                return True  # Devolver True si se encuentra el objetivo
            visitado.add(nodo_actual)  # Marcar el nodo actual como visitado
            for vecino in self.grafo.get(nodo_actual, []):  # Iterar sobre los vecinos del nodo actual
                if vecino not in visitado:  # Verificar si el vecino no ha sido visitado
                    cola.append(vecino)  # Agregar el vecino a la cola para visitar
        print("\nEl objetivo", objetivo, "no se encontro")  # Imprimir mensaje de fracaso si el objetivo no se encuentra
        return False  # Devolver False si el objetivo no se encuentra

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

# Realizar la busqueda en amplitud desde el nodo 2 al nodo 3
print("Busqueda en amplitud desde el nodo 2 al nodo 3:")
grafo.bfs(2, 3)

