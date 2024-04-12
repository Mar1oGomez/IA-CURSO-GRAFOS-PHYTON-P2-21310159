class Grafo:  # Definicion de la clase Grafo
    def __init__(self):  # Metodo de inicializacion de la clase
        self.grafo = {}  # Inicializacion del diccionario que representara el grafo

    def agregar_arista(self, u, v):  # Metodo para agregar una arista al grafo
        if u not in self.grafo:  # Verificar si el nodo u no esta en el grafo
            self.grafo[u] = []  # Agregar el nodo u al grafo
        self.grafo[u].append(v)  # Agregar la arista desde u hacia v

    def dfs(self, inicio, objetivo, max_profundidad):  # Metodo de busqueda en profundidad iterativa
        for profundidad in range(max_profundidad + 1):  # Iterar sobre los limites de profundidad
            visitado = set()  # Conjunto para almacenar los nodos visitados en esta iteracion
            if self.dls(inicio, objetivo, profundidad, visitado):  # Realizar busqueda DFS limitada
                print("\nEl objetivo", objetivo, "se encontro a profundidad", profundidad)  # Imprimir mensaje si se encuentra el objetivo
                return True  # Devolver True si se encuentra el objetivo
        print("\nEl objetivo", objetivo, "no se encontro dentro de la profundidad maxima")  # Imprimir mensaje si no se encuentra el objetivo
        return False  # Devolver False si no se encuentra el objetivo dentro de la profundidad maxima

    def dls(self, nodo, objetivo, limite, visitado):  # Metodo de busqueda en profundidad limitada
        if limite >= 0:  # Verificar si el limite de profundidad no se ha alcanzado
            print(nodo, end=" ")  # Imprimir el nodo actual
            if nodo == objetivo:  # Verificar si se ha alcanzado el objetivo
                return True  # Devolver True si se ha encontrado el objetivo
            visitado.add(nodo)  # Marcar el nodo actual como visitado
            for vecino in self.grafo.get(nodo, []):  # Iterar sobre los vecinos del nodo actual
                if vecino not in visitado:  # Verificar si el vecino no ha sido visitado
                    if self.dls(vecino, objetivo, limite - 1, visitado):  # Realizar busqueda DFS limitada para el vecino
                        return True  # Devolver True si se ha encontrado el objetivo
        return False  # Devolver False si no se ha encontrado el objetivo o se ha alcanzado el limite de profundidad

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

# Realizar la busqueda en profundidad iterativa desde el nodo 2 al nodo 3 con una profundidad maxima de 3
print("Busqueda en profundidad iterativa desde el nodo 2 al nodo 3 con profundidad maxima 3:")
grafo.dfs(2, 3, 3)

