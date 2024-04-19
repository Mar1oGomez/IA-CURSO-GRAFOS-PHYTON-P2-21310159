import math  # Importa el modulo math para operaciones matematicas
import random  # Importa el modulo random para generar numeros aleatorios

def funcion_objetivo(x, y):  # Define una funcion objetivo ficticia
    return -(x ** 2) - (y ** 2)  # Retorna el valor negativo de la suma de los cuadrados de x e y

def generar_vecino(solucion_actual, rango):  # Define una funcion para generar un vecino aleatorio
    x = solucion_actual[0] + random.uniform(-rango, rango)  # Genera una coordenada x cercana a la solucion actual
    y = solucion_actual[1] + random.uniform(-rango, rango)  # Genera una coordenada y cercana a la solucion actual
    return [x, y]  # Retorna el vecino generado

def temple_simulado(solucion_inicial, temperatura_inicial, rango, pasos_por_temperatura, enfriamiento, funcion_objetivo):  # Define la funcion de Temple Simulado
    mejor_solucion = solucion_inicial  # Inicializa la mejor solucion con la solucion inicial
    mejor_valor = funcion_objetivo(*mejor_solucion)  # Calcula el valor de la mejor solucion

    temperatura_actual = temperatura_inicial  # Inicializa la temperatura actual con la temperatura inicial

    for _ in range(pasos_por_temperatura):  # Itera a lo largo del numero de pasos por temperatura
        vecino = generar_vecino(mejor_solucion, rango)  # Genera un vecino aleatorio cercano a la mejor solucion actual
        valor_vecino = funcion_objetivo(*vecino)  # Calcula el valor del vecino generado

        diferencia_valor = valor_vecino - mejor_valor  # Calcula la diferencia de valor entre el vecino y la mejor solucion

        if diferencia_valor > 0 or random.random() < math.exp(diferencia_valor / temperatura_actual):  # Verifica si se acepta el vecino como nueva mejor solucion
            mejor_solucion = vecino  # Actualiza la mejor solucion si se acepta el vecino
            mejor_valor = valor_vecino  # Actualiza el valor de la mejor solucion si se acepta el vecino

        temperatura_actual *= enfriamiento  # Aplica el enfriamiento para reducir la temperatura

    return mejor_solucion, mejor_valor  # Retorna la mejor solucion y su valor

# Punto de inicio aleatorio en un rango de (-10, 10) para cada dimension
solucion_inicial = [random.uniform(-10, 10), random.uniform(-10, 10)]

# Parametros del Temple Simulado
temperatura_inicial = 100.0
rango = 1.0
pasos_por_temperatura = 100
enfriamiento = 0.9

# Realiza la busqueda de Temple Simulado
mejor_solucion, mejor_valor = temple_simulado(solucion_inicial, temperatura_inicial, rango, pasos_por_temperatura, enfriamiento, funcion_objetivo)

# Imprime el resultado
print("Busqueda de Temple Simulado:")
print("Mejor solucion encontrada:", mejor_solucion)
print("Mejor valor encontrado:", mejor_valor)

