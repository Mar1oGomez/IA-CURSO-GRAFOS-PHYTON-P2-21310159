import heapq  # Importa la implementacion de la cola de prioridad desde el modulo heapq

class Nodo:  # Definicion de la clase Nodo
    def __init__(self, estado, costo_acumulado, heuristica):  # Metodo de inicializacion de la clase
        self.estado = estado  # Estado del nodo
        self.costo_acumulado = costo_acumulado  # Costo acumulado para llegar al nodo
        self.heuristica = heuristica  # Valor heuristico del nodo

    def __lt__(self, otro):  # Metodo para comparar nodos segun su heuristica
        return (self.costo_acumulado + self.heuristica) < (otro.costo_acumulado + otro.heuristica)

class Grafo:  # Definicion de la clase Grafo
    def __init__(self):  # Metodo de inicializacion de la clase
        self.grafo = {}  # Inicializacion del diccionario que representara el grafo

    def agregar_arista(self, u, v, peso):  # Metodo para agregar una arista al grafo
        if u not in self.grafo:  # Verificar si el nodo u no esta en el grafo
            self.grafo[u] = []  # Agregar el nodo u al grafo
        self.grafo[u].append((v, peso))  # Agregar la arista desde u hacia v con su peso

    def a_estrella(self, inicio, objetivo, heuristica):  # Metodo de busqueda A*
        cola_prioridad = []  # Cola de prioridad para nodos a explorar
        heapq.heappush(cola_prioridad, Nodo(inicio, 0, heuristica[inicio]))  # Agregar el nodo inicial a la cola de prioridad
        visitado = set()  # Conjunto para nodos visitados

        while cola_prioridad:  # Mientras la cola de prioridad no este vacia
            nodo_actual = heapq.heappop(cola_prioridad)  # Extraer el nodo de la cola de prioridad

            if nodo_actual.estado == objetivo:  # Verificar si se ha encontrado el objetivo
                return nodo_actual.costo_acumulado  # Devolver el costo acumulado si se encuentra el objetivo

            if nodo_actual.estado not in visitado:  # Verificar si el nodo actual no ha sido visitado
                visitado.add(nodo_actual.estado)  # Marcar el nodo actual como visitado

                for vecino, peso in self.grafo.get(nodo_actual.estado, []):  # Iterar sobre los vecinos del nodo actual
                    nuevo_costo = nodo_actual.costo_acumulado + peso  # Calcular el nuevo costo acumulado
                    heapq.heappush(cola_prioridad, Nodo(vecino, nuevo_costo, heuristica[vecino]))  # Agregar el vecino a la cola de prioridad

        return float('inf')  # Devolver infinito si no se encuentra el objetivo

    def ao_estrella(self, inicio, objetivo, heuristica, lambda_=1.0):  # Metodo de busqueda AO*
        cola_prioridad = []  # Cola de prioridad para nodos a explorar
        heapq.heappush(cola_prioridad, Nodo(inicio, 0, heuristica[inicio]))  # Agregar el nodo inicial a la cola de prioridad
        visitado = set()  # Conjunto para nodos visitados

        while cola_prioridad:  # Mientras la cola de prioridad no este vacia
            nodo_actual = heapq.heappop(cola_prioridad)  # Extraer el nodo de la cola de prioridad

            if nodo_actual.estado == objetivo:  # Verificar si se ha encontrado el objetivo
                return nodo_actual.costo_acumulado  # Devolver el costo acumulado si se encuentra el objetivo

            if nodo_actual.estado not in visitado:  # Verificar si el nodo actual no ha sido visitado
                visitado.add(nodo_actual.estado)  # Marcar el nodo actual como visitado

                for vecino, peso in self.grafo.get(nodo_actual.estado, []):  # Iterar sobre los vecinos del nodo actual
                    nuevo_costo = nodo_actual.costo_acumulado + peso  # Calcular el nuevo costo acumulado
                    nueva_heuristica = (1 - lambda_) * heuristica[vecino] + lambda_ * nuevo_costo  # Calcular la nueva heuristica
                    heapq.heappush(cola_prioridad, Nodo(vecino, nuevo_costo, nueva_heuristica))  # Agregar el vecino a la cola de prioridad

        return float('inf')  # Devolver infinito si no se encuentra el objetivo

# ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B', 2)
grafo.agregar_arista('A', 'C', 3)
grafo.agregar_arista('B', 'D', 4)
grafo.agregar_arista('C', 'D', 5)
grafo.agregar_arista('C', 'E', 6)
grafo.agregar_arista('D', 'F', 7)
grafo.agregar_arista('E', 'F', 8)

# Definir heuristica para el grafo de ejemplo (valores ad-hoc)
heuristica = {'A': 7, 'B': 6, 'C': 5, 'D': 2, 'E': 3, 'F': 0}

# Realizar la busqueda A* desde el nodo 'A' al nodo 'F'
print("Busqueda A* desde el nodo 'A' al nodo 'F':")
costo_a_estrella = grafo.a_estrella('A', 'F', heuristica)
print("Costo total encontrado por A*:", costo_a_estrella)

# Realizar la busqueda AO* desde el nodo 'A' al nodo 'F' con lambda=0.5
print("\nBusqueda AO* desde el nodo 'A' al nodo 'F' con lambda=0.5:")
costo_ao_estrella = grafo.ao_estrella('A', 'F', heuristica, lambda_=0.5)
print("Costo total encontrado por AO*:", costo_ao_estrella)

