class Grafo: #clase llamada grafo
    def __init__(self): #metodo de inicializacion, diccionario vacio
        self.grafo = {}

    def agregar_arista(self, u, v): #agrega una arista entre los nodos u y v al grafo
        if u not in self.grafo: #verifica si el nodo u no esta precente en el grafo
            self.grafo[u] = [] #agrega el nodo u
        self.grafo[u].append(v) #agrega nodo v a la lista adyacente de u

    def dls(self, nodo, objetivo, limite, visitado): #define un metodo para realizar la Busqueda en Profundidad Limitada (DLS).
        if limite >= 0: #verifica si aun no se ha alcanzadoel limite de profundidad
            print(nodo, end=" ") #imprime el nodo actual
            if nodo == objetivo: #verifica el nodo
                return True
            visitado.add(nodo) #marca el nodo como visitado
            for vecino in self.grafo.get(nodo, []): #itera los vecinos del nodo
                if vecino not in visitado:
                    if self.dls(vecino, objetivo, limite - 1, visitado):#llama recursivamente al metodo dls con un limite de profundidida
                        return True
        return False

    def dfs_limitada(self, inicio, objetivo, limite):#define la busqueda de profundidad
        visitado = set() #crea un conjunto para almacenar los nodos
        if self.dls(inicio, objetivo, limite, visitado):#inicia la busqueda de profundidad
            print("\nEl objetivo", objetivo, "se encontro dentro del limite de profundidad", limite)
        else:
            print("\nEl objetivo", objetivo, "no se encontro dentro del limite de profundidad", limite)

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

# Realizar la busqueda en profundidad limitada desde el nodo 2 al nodo 3 con un limite de profundidad de 3
print("Busqueda en profundidad limitada desde el nodo 2 al nodo 3 con limite de profundidad 3:")
grafo.dfs_limitada(2, 3, 3)