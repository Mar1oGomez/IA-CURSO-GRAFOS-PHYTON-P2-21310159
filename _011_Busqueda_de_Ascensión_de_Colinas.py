import random  # Importa el modulo random para generar numeros aleatorios

def objetivo_fn(x):  # Define una funcion objetivo ficticia
    return -(x ** 2)  # Retorna el valor negativo del cuadrado de x

def generar_vecino(actual, paso):  # Define una funcion para generar un vecino aleatorio
    return actual + random.uniform(-paso, paso)  # Retorna un valor cercano al actual

def ascension_colinas(punto_inicial, paso, objetivo_fn):  # Define la funcion de Busqueda de Ascension de Colinas
    mejor_punto = punto_inicial  # Inicializa el mejor punto con el punto inicial
    mejor_valor = objetivo_fn(mejor_punto)  # Calcula el valor del mejor punto

    iteraciones = 0  # Inicializa el contador de iteraciones
    while True:  # Ciclo infinito (se rompera cuando no se encuentre un vecino mejor)
        vecino = generar_vecino(mejor_punto, paso)  # Genera un vecino aleatorio
        valor_vecino = objetivo_fn(vecino)  # Calcula el valor del vecino

        if valor_vecino > mejor_valor:  # Verifica si el vecino es mejor que el mejor punto actual
            mejor_punto = vecino  # Actualiza el mejor punto
            mejor_valor = valor_vecino  # Actualiza el mejor valor
        else:
            break  # Rompe el ciclo si no se encuentra un vecino mejor

        iteraciones += 1  # Incrementa el contador de iteraciones

    return mejor_punto, mejor_valor, iteraciones  # Retorna el mejor punto, su valor y el numero de iteraciones

# Punto de inicio aleatorio
punto_inicial = random.uniform(-10, 10)

# Tamano del paso para generar vecinos
paso = 0.5

# Realiza la busqueda de ascension de colinas
mejor_punto, mejor_valor, iteraciones = ascension_colinas(punto_inicial, paso, objetivo_fn)

# Imprime el resultado
print("Busqueda de Ascension de Colinas:")
print("Mejor punto encontrado:", mejor_punto)
print("Mejor valor encontrado:", mejor_valor)
print("Iteraciones realizadas:", iteraciones)

