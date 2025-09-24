import ast

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

if __name__ == "__main__":
    input_path = "problema1/pruebas/set_de_datos.txt"
    output_path = "problema1/pruebas/resultados_set_de_Datos.txt"
    
    with open(input_path, "r") as f:
        lines = f.readlines()
    
    data_str = ""
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("#"):
            data_str += stripped + " "
            
    array_strs = data_str.split(";")
    
    results = []
    for array_str in array_strs:
        array_str = array_str.strip()
        if array_str:
            try:
                arr = ast.literal_eval(array_str)
                resultado = problema1(arr, 0, len(arr) - 1)
                results.append(f"{arr} -> {resultado}")
            except Exception as e:
                results.append(f"Error en array '{array_str}': {e}")
    
    with open(output_path, "w") as f:
        for line in results:
            f.write(line + "\n")
    
    print("Procesamiento completado. Revisar el archivo de resultados.")
