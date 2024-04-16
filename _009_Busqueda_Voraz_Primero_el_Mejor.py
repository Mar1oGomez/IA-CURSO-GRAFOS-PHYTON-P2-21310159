import heapq  # Importa la implementacion de la cola de prioridad desde el modulo heapq

class Nodo:  # Definicion de la clase Nodo
    def __init__(self, estado, heuristica):  # Metodo de inicializacion de la clase
        self.estado = estado  # Estado del nodo
        self.heuristica = heuristica  # Valor heuristico del nodo

    def __lt__(self, otro):  # Metodo para comparar nodos segun su heuristica
        return self.heuristica < otro.heuristica

class Grafo:  # Definicion de la clase Grafo
    def __init__(self):  # Mewtodo de inicializacion de la clase
        self.grafo = {}  # Inicializacion del diccionario que representara el grafo

    def agregar_arista(self, u, v, peso):  # Metodo para agregar una arista al grafo
        if u not in self.grafo:  # Verificar si el nodo u no esta en el grafo
            self.grafo[u] = []  # Agregar el nodo u al grafo
        self.grafo[u].append((v, peso))  # Agregar la arista desde u hacia v con su peso

    def voraz_primero_mejor(self, inicio, objetivo, heuristica):  # Metodo de busqueda voraz (Primero el Mejor)
        cola_prioridad = []  # Cola de prioridad para nodos a explorar
        heapq.heappush(cola_prioridad, Nodo(inicio, heuristica[inicio]))  # Agregar el nodo inicial a la cola de prioridad
        visitado = set()  # Conjunto para nodos visitados

        while cola_prioridad:  # Mientras la cola de prioridad no este vacia
            nodo_actual = heapq.heappop(cola_prioridad)  # Extraer el nodo de la cola de prioridad
            print(nodo_actual.estado, end=" ")  # Imprimir el estado del nodo actual

            if nodo_actual.estado == objetivo:  # Verificar si se ha encontrado el objetivo
                print("\nEl objetivo", objetivo, "se encontro")  # Imprimir mensaje de exito
                return True  # Devolver True si se encuentra el objetivo

            visitado.add(nodo_actual.estado)  # Marcar el nodo actual como visitado

            for vecino, _ in self.grafo.get(nodo_actual.estado, []):  # Iterar sobre los vecinos del nodo actual
                if vecino not in visitado:  # Verificar si el vecino no ha sido visitado
                    heapq.heappush(cola_prioridad, Nodo(vecino, heuristica[vecino]))  # Agregar el vecino a la cola de prioridad

        print("\nEl objetivo", objetivo, "no se encontro")  # Imprimir mensaje de fracaso si el objetivo no se encuentra
        return False  # Devolver False si el objetivo no se encuentra

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

# Realizar la busqueda voraz desde el nodo 'A' al nodo 'F'
print("Busqueda Voraz (Primero el Mejor) desde el nodo 'A' al nodo 'F':")
grafo.voraz_primero_mejor('A', 'D', heuristica)

