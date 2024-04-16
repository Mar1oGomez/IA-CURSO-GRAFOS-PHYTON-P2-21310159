import random  # Importa el modulo random para generar numeros aleatorios

def objetivo_fn(x, y):  # Define una funcion objetivo ficticia
    return -(x ** 2) - (y ** 2)  # Retorna el valor negativo de la suma de los cuadrados de x e y

def generar_vecino(actual, rango):  # Define una funcion para generar un vecino aleatorio
    return actual + random.uniform(-rango, rango)  # Retorna un valor cercano al actual dentro del rango especificado

def busqueda_tabu(punto_inicial, pasos, iteraciones, objetivo_fn):  # Define la funcion de Busqueda Tabu
    mejor_punto = punto_inicial  # Inicializa el mejor punto con el punto inicial
    mejor_valor = objetivo_fn(*mejor_punto)  # Calcula el valor del mejor punto

    lista_tabu = []  # Inicializa la lista tabu

    for _ in range(iteraciones):  # Itera a lo largo del numero de iteraciones especificadas
        vecino = [generar_vecino(mejor_punto[i], pasos[i]) for i in range(len(punto_inicial))]  # Genera un vecino aleatorio para cada dimension
        valor_vecino = objetivo_fn(*vecino)  # Calcula el valor del vecino

        if vecino not in lista_tabu and valor_vecino > mejor_valor:  # Verifica si el vecino no esta en la lista tabu y su valor es mejor
            mejor_punto = vecino  # Actualiza el mejor punto
            mejor_valor = valor_vecino  # Actualiza el mejor valor

        lista_tabu.append(vecino)  # Agrega el vecino a la lista tabu
        if len(lista_tabu) > 10:  # Verifica si la lista tabu supera su tamano maximo
            lista_tabu.pop(0)  # Elimina el primer elemento de la lista tabu

    return mejor_punto, mejor_valor  # Retorna el mejor punto y su valor

# Punto de inicio aleatorio en un rango de (-10, 10) para cada dimension
punto_inicial = [random.uniform(-10, 10), random.uniform(-10, 10)]

# Tamano del paso para generar vecinos en cada dimension
pasos = [0.1, 0.5]

# Numero de iteraciones a realizar
iteraciones = 100

# Realiza la busqueda tabu
mejor_punto, mejor_valor = busqueda_tabu(punto_inicial, pasos, iteraciones, objetivo_fn)

# Imprime el resultado
print("Busqueda Tabu:")
print("Mejor punto encontrado:", mejor_punto)
print("Mejor valor encontrado:", mejor_valor)

