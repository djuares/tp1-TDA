def busqbin(lista, inicio, final):

    # caso base: si inicio es mayor a final, la condición no existe
    if inicio > final:  
        return "no existe i"
        
    mitad = inicio + (final - inicio) // 2    
   
    if lista[mitad] == mitad:
        return mitad
    
    if lista[mitad] > mitad:
        result = busqbin(lista, inicio, mitad - 1)
        if result != "no existe i":
            return result
        return busqbin(lista, lista[mitad] + 1, final)
    
    else:
        result = busqbin(lista, inicio, mitad - 1)
        if result != "no existe i":
            return result
        return busqbin(lista, mitad + 1, final)

print(busqbin([0,3,4,5,6,9], 0, 5))

