from collections import defaultdict #es una subclase de diccionario que proporciona un valor predeterminado para las claves que aun no estan en el diccionario, eliminando asi la necesidad de manejar las excepciones KeyError.

class Grafo: # define una clase
    def __init__(self): #metodo de inicialixacion
        self.grafo = defaultdict(list) 

    def agregar_arista(self, u, v): # se define el metodo para agregar una arista entre nodos u y v
        self.grafo[u].append(v)

    def bfs(self, inicio): #busqueda de anchura
        visitado = [False] * (max(self.grafo) + 1)  # Inicializar todos los nodos como no visitados
        cola = []  # Cola para realizar BFS

        cola.append(inicio) #agrega nodo inicial a la cola
        visitado[inicio] = True #nodo visitado

        while cola: #ejerce un bucle mientras haya nodos en la cola
            nodo = cola.pop(0) #elimina y devuelve el elemento a la cola
            print(nodo, end=" ")

            # Obtener los nodos adyacentes y agregarlos a la cola si no han sido visitados
            for i in self.grafo[nodo]:#itera sobre los nodos adyacentes
                if not visitado[i]:
                    cola.append(i)
                    visitado[i] = True

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido BFS empezando desde el nodo 2:")
grafo.bfs(2)
