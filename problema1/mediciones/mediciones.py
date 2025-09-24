import time
import matplotlib.pyplot as plt
import ast
import re

def problema1(lista, inicio, final):
    # caso base: si inicio es mayor a final, la condición no existe
    if inicio > final:  
        return "no existe i"
        
    mitad = inicio + (final - inicio) // 2    
    
    if lista[mitad] == mitad:
        return mitad
    
    if lista[mitad] > mitad:
        result = problema1(lista, inicio, mitad - 1)
        if result != "no existe i":
            return result
        return problema1(lista, lista[mitad] + 1, final)
    
    else:
        result = problema1(lista, inicio, mitad - 1)
        if result != "no existe i":
            return result
        return problema1(lista, mitad + 1, final)
    
def medir_tiempos(lista_arrays):
    tiempos = []
    for array in lista_arrays:
        print(f"Ejecutando para Array = {array}")

        inicio = time.perf_counter()            
        problema1(array, 0, len(array) - 1)     
        fin = time.perf_counter()               

        tiempo = fin - inicio                   
        print(f"Tiempo: {tiempo:.4f} segundos")
        tiempos.append(tiempo)

    return tiempos


def graficar_tiempos(lista_arrays, tiempos):
    # eje X: longitudes de cada array
    tamanios = [len(arr) for arr in lista_arrays]

    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos, 'o-', color='blue',
             label='Problema 1 - Tiempo de ejecución')
    plt.xlabel('Tamaño del array (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempos de ejecución - set de datos problema 1')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)

    # anotar cada punto con su tiempo
    for x, y in zip(tamanios, tiempos):
        plt.annotate(f"{y:.2f}s", (x, y),
                     textcoords="offset points", xytext=(0, 5), ha='center')

    plt.legend()
    plt.tight_layout()
    plt.savefig('problema1/mediciones/medicion.png', dpi=300)
    plt.show()
    print("Gráfico guardado como 'problema1/mediciones/medicion.png'")

def leer_set(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    
    # Buscar todos los patrones que parecen arrays
    patron = r'\[[^\]]*\]'
    arrays_encontrados = re.findall(patron, contenido)
    
    lista_arrays = [ast.literal_eval(arr) for arr in arrays_encontrados]
    return lista_arrays

if __name__ == "__main__":
    input_path = "problema1/pruebas/set_de_datos.txt"
    lista_arrays= leer_set(input_path)
    tiempos = medir_tiempos(lista_arrays)
    graficar_tiempos(lista_arrays, tiempos)
