def subsequence_max_dynamic_programming(arr):
    if not arr:  # Manejar array vacío
        return 0, -1, -1

    # Inicialización con el primer elemento
    max_sum = arr[0]
    max_start = 0
    max_end = 0
    current_sum = arr[0]
    current_start = 0

    # Iterar desde el segundo elemento
    for i in range(1, len(arr)):
        # Decidir si empezar nuevo subarray o extender el actual
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            current_start = i
        else:
            current_sum += arr[i]

        # Actualizar la solución global si encontramos una suma mayor
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i

    # Extraer la secuencia óptima
    # max_sequence = arr[max_start:max_end + 1]

    return max_sum, max_start, max_end

if __name__ == "__main__":
    import sys

    # Verificar si se proporcionan argumentos
    if len(sys.argv) < 2:
        print("Uso: python3 problema_4.py <num1> <num2> ...")
        print("Ejemplo: python problema_4.py -2 1 3 -1 5")
        sys.exit(1)

    # Convertir argumentos de la línea de comandos a una lista de enteros
    try:
        input_array = [int(x) for x in sys.argv[1:]]
    except ValueError:
        print("Error: Todos los argumentos deben ser números enteros.")
        sys.exit(1)

    # Ejecutar el algoritmo
    suma, max_start, max_end = subsequence_max_dynamic_programming(input_array)

    # Imprimir resultados
    print(f"Suma máxima: {suma}")
    print(f"Secuencia: {input_array[max_start:max_end + 1]}")