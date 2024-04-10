class Grafo:#defines una clase llamada grafo
    def __init__(self): #defines el metodo de inicializacion de la clase
        self.grafo = {} #deccionario vacio

    def agregar_arista(self, u, v): #defiene metodopara agregar arista entre nodos u y v al grafo
        if u not in self.grafo: #verifica si el nodo u no esta presente en el grafo
            self.grafo[u] = []
        self.grafo[u].append(v)#agrega el nodo v a la lista adyacente del nodo u

    def dfs_util(self, nodo, visitado): #Define un metodo de utilidad para realizar la busqueda en profundidad recursivamente
        visitado.add(nodo) #marca el nodo actual como visitado 
        print(nodo, end=" ") #imprime nodo actual

        for vecino in self.grafo.get(nodo, []):#Itera sobre los vecinos del nodo actual
            if vecino not in visitado: #verifica si el vecino no ha sido visitado
                self.dfs_util(vecino, visitado) #llama recursivamente al metodo dfs_util para explorar el vecino no visitado

    def dfs(self, inicio): #Define un metodo para realizar la busqueda en profundidad comenzando desde el nodo 'inicio'
        visitado = set() #crea un conjunto para almacenar los nodos visitados durante la busqueda
        self.dfs_util(inicio, visitado) #llama al metodo de utilidad 'dfs_util' para iniciar la busqueda en profundidad desde el nodo de inicio

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

# Realizar la busqueda en profundidad desde el nodo 2
print("Recorrido DFS empezando desde el nodo 2:")
grafo.dfs(2)

