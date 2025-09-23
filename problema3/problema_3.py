import time
import random

def generar_set_de_datos(n, semilla, min_val, max_val):
    random.seed(semilla)
    return [random.randint(min_val, max_val) for _ in range(n)]


def subsecuence_max(num_array):
    # Manejo de caso borde: si el array está vacío, no hay subsecuencia.
    if not num_array:
        return 0, -1, -1

    array_lenght = len(num_array)
    
    max_suma_global = float('-inf') # Inicializamos con el valor más pequeño posible.
    mejor_inicio = -1
    mejor_fin = -1

    # 1. Backtracking - Nivel 1: Fijar el inicio de la subsecuencia
    # Probamos cada índice 'i' como un posible punto de partida.
    for i in range(array_lenght):
        suma_actual = 0
        
        # 2. Backtracking - Nivel 2: Extender la subsecuencia desde 'i'
        # A partir del 'i' fijado, exploramos todas las subsecuencias posibles
        # extendiendo el final 'j' hasta el final del array.
        for j in range(i, array_lenght):
            
            suma_actual += num_array[j]

            # Si la suma de la subsecuencia actual (de i a j) es la mejor
            # que hemos encontrado hasta ahora, la guardamos como la mejor solución.
            if suma_actual > max_suma_global:
                max_suma_global = suma_actual
                mejor_inicio = i
                mejor_fin = j
    
    return max_suma_global, mejor_inicio, mejor_fin


if __name__ == "__main__":

    datos_ejemplo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    datos_ejemplo_1 = [2, 3, -6, 7, -2, 4, -1, 2, 1, -5, 4]

    print(f"Analizando el array: {datos_ejemplo_1}\n")

    inicio_tiempo = time.time()

    suma, inicio, fin = subsecuence_max(datos_ejemplo_1)

    fin_tiempo = time.time()

    duracion = fin_tiempo - inicio_tiempo

    if inicio != -1:
        subsecuencia = datos_ejemplo_1[inicio : fin + 1]
        print(f"✅ Resultados encontrados:")
        print(f"   -> Suma Máxima: {suma}")
        print(f"   -> Subsecuencia: {subsecuencia} (índices {inicio} a {fin})")
    else:
        print("❌ El array está vacío, no se encontró ninguna subsecuencia.")
    
    print(f"\n⏱️  Tiempo de ejecución: {duracion:.6f} segundos.")