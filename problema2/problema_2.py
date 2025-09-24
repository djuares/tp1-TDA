# Devuelve un diccionario con la suma de números desde la posición i hasta el final del arreglo
def suma_positivos_final(arr):
    resultados = {}
    suma = 0

    for i in range(len(arr)):
        resultados[i] = 0
        suma = 0
        max = float("-inf")
        for j in range(i + 1, len(arr)):
            suma += arr[j]
            if suma > max:
                max = suma
        resultados[i] = max
    
    resultados[len(arr)-1] = 0
    return resultados

def algoritmo_greedy(arr):
    pos = suma_positivos_final(arr)
    suma_int = 0
    elems_int = 0
    cant_ints = 0

    for i, x in enumerate(arr):
        suma_int += x
        elems_int += 1

        # caso 1: intervalo sin sentido (demasiado chico y no se puede extender)
        if elems_int <= 1 and suma_int + pos[i] <= 0:
            suma_int = 0
            elems_int = 0
            continue

        # caso 2: todavía conviene seguir extendiendo (hay chance mas adelante por pos)
        if suma_int + pos[i] > 0:
            continue

        # caso 3: hay que cerrar el intervalo
        cant_ints += 1
        suma_int = 0
        elems_int = 0

    # Último intervalo válido
    if suma_int > 0 and elems_int > 1:
        cant_ints += 1

    return cant_ints
