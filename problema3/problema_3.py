import time
import random

def generar_set_de_datos(n, semilla, min_val, max_val):
    random.seed(semilla)
    return [random.randint(min_val, max_val) for _ in range(n)]


def subsecuence_max(num_array):

    if not num_array:
        return 0, -1, -1

    array_lenght = len(num_array)
    
    max_suma_global = float('-inf') 
    mejor_inicio = -1
    mejor_fin = -1


    for i in range(array_lenght):
        suma_actual = 0
        
        for j in range(i, array_lenght):
            
            suma_actual += num_array[j]

            if suma_actual > max_suma_global:
                max_suma_global = suma_actual
                mejor_inicio = i
                mejor_fin = j
    
    return max_suma_global, mejor_inicio, mejor_fin


if __name__ == "__main__":

    print("🔹 Ejecucion de 6 datasets aleatorios\n")

    
    for idx in range(1, 7):
        datos = generar_set_de_datos(
            n=random.randint(8, 15),     
            semilla=idx * 100,          
            min_val=-10,                 
            max_val=10
        )

        print(f"Ejemplo {idx}: {datos}\n")

        inicio_tiempo = time.time()
        suma, inicio, fin = subsecuence_max(datos)
        fin_tiempo = time.time()

        duracion = fin_tiempo - inicio_tiempo

        if inicio != -1:
            subsecuencia = datos[inicio : fin + 1]
            print(f"Resultados encontrados:")
            print(f"   -> Suma Maxima: {suma}")
            print(f"   -> Subsecuencia: {subsecuencia} (indices {inicio} a {fin})")
        else:
            print("El array esta vacio, no se encontro ninguna subsecuencia.")
        
        print(f"Tiempo de ejecucion: {duracion:.6f} segundos.\n")
        print("-" * 60 + "\n")