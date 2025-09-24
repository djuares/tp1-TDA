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
    
#Auxiliares para leer y escribir archivos
def leer_set(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    
    patron = r'\[[^\]]*\]'
    arrays_encontrados = re.findall(patron, contenido)
    
    lista_arrays = [ast.literal_eval(arr) for arr in arrays_encontrados]
    return lista_arrays

def escribir_resultados_set(resultados, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for array in resultados:
            archivo.write(f"Resultado: {array}\n")
    return True

if __name__ == "__main__":
    input_path = "problema1/pruebas/set_de_datos.txt"
    output_path = "problema1/pruebas/resultados_set_de_Datos.txt"

    lista_arrays = leer_set(input_path)

    resultados=[]
    for array in lista_arrays:
            resultados += [problema1(array, 0, len(array) - 1)]

    escribir_resultados_set(resultados, output_path)

    
    print("Procesamiento completado. Revisar el archivo de resultados.")
