class Grafo:  # definicion de la clase Grafo
    def __init__(self):  #metodo de inicializacin de la clase
        self.grafo = {}  #inicializacion del diccionario que representara el grafo

    def agregar_arista(self, u, v):  #metodo para agregar una arista al grafo
        if u not in self.grafo:  #verificar si el nodo u 
            self.grafo[u] = []  # Agregar el nodo u al grafo
        self.grafo[u].append(v)  # Agregar la arista desde u hacia v

    def bfs(self, inicio, objetivo):  #mrtodo de busqueda en amplitud
        cola_inicio = [inicio]  # Cola para los nodos visitados desde el nodo inicial
        cola_objetivo = [objetivo]  # Cola para los nodos visitados desde el nodo objetivo
        visitado_inicio = set([inicio])  # Conjunto para los nodos visitados desde el nodo inicial
        visitado_objetivo = set([objetivo])  # Conjunto para los nodos visitados desde el nodo objetivo

        while cola_inicio and cola_objetivo:  # Mientras haya nodos en ambas colas
            if self.encuentra_interseccion(visitado_inicio, visitado_objetivo):  # Verificar si hay interseccion
                print("Interseccion encontrada")  # Imprimir mensaje si se encuentra interseccion
                return True  # Devolver True si se encuentra interseccion
            
            # Exploracion desde el nodo inicial
            for _ in range(len(cola_inicio)):
                nodo_actual = cola_inicio.pop(0)  # Extraer el primer nodo de la cola
                for vecino in self.grafo.get(nodo_actual, []):  # Iterar sobre los vecinos del nodo actual
                    if vecino not in visitado_inicio:  # Verificar si el vecino no ha sido visitado desde el nodo inicial
                        visitado_inicio.add(vecino)  # Marcar el vecino como visitado desde el nodo inicial
                        cola_inicio.append(vecino)  # Agregar el vecino a la cola de nodos visitados desde el nodo inicial
            
            # Exploracion desde el nodo objetivo
            for _ in range(len(cola_objetivo)):
                nodo_actual = cola_objetivo.pop(0)  # Extraer el primer nodo de la cola
                for vecino in self.grafo.get(nodo_actual, []):  # Iterar sobre los vecinos del nodo actual
                    if vecino not in visitado_objetivo:  # Verificar si el vecino no ha sido visitado desde el nodo objetivo
                        visitado_objetivo.add(vecino)  # Marcar el vecino como visitado desde el nodo objetivo
                        cola_objetivo.append(vecino)  # Agregar el vecino a la cola de nodos visitados desde el nodo objetivo
        return False  # Devolver False si no se encuentra interseccion

    def encuentra_interseccion(self, visitado_inicio, visitado_objetivo):  #metodo para encontrar interseccion
        return bool(visitado_inicio.intersection(visitado_objetivo))  # Devolver True si hay interseccion, False de lo contrario

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

# Realizar la busqueda bidireccional desde el nodo 2 al nodo 3
print("Busqueda bidireccional desde el nodo 2 al nodo 3:")
if grafo.bfs(2, 3):
    print("Se encontro un camino entre el nodo 2 y el nodo 3")
else:
    print("No se encontro un camino entre el nodo 2 y el nodo 3")

