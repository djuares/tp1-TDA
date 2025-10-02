# Algoritmo de Subsecuencia con Suma Máxima

Este problema implementa un algoritmo en **Python** que encuentra la subsecuencia contigua con la suma máxima dentro de un arreglo de enteros.  
El código utiliza un enfoque de **backtracking** para explorar todas las combinaciones posibles.

---

## Lenguaje y versión mínima

- **Lenguaje:** Python  
- **Versión mínima requerida:** 3.8

---

## Bibliotecas requeridas

El programa utiliza únicamente librerías estándar incluidas en Python, por lo que **no es necesario instalar dependencias externas**:

- `time`
- `random`

---

## Instrucciones de ejecución

1. Abrir una terminal en la carpeta donde se encuentra el archivo.
2. Ejecutar el programa con:

```bash
python3 problema_3.py
```

---

## Ejemplo de Salida

Los dataset de ejemplo son aleatorios, se puede observar en el codigo: 


```bash
Ejemplo 1: [-6, 4, 4, -5, 2, 1, 3, 6, -7, 7, -7, -8, 4, -2, -9]

Resultados encontrados:
   -> Suma Máxima: 15
   -> Subsecuencia: [4, 4, -5, 2, 1, 3, 6] (índices 1 a 7)
Tiempo de ejecución: 0.000012 segundos.

------------------------------------------------------------

Ejemplo 2: [-9, -4, -10, -6, 9, -2, -10, 4, -5, -10, 4]

Resultados encontrados:
   -> Suma Máxima: 9
   -> Subsecuencia: [9] (índices 4 a 4)
Tiempo de ejecución: 0.000005 segundos.

------------------------------------------------------------

Ejemplo 3: [9, 1, 1, -10, 5, 1, 6, 3, 8, 8, -5, -5]

Resultados encontrados:
   -> Suma Máxima: 32
   -> Subsecuencia: [9, 1, 1, -10, 5, 1, 6, 3, 8, 8] (índices 0 a 9)
Tiempo de ejecución: 0.000005 segundos.

------------------------------------------------------------

Ejemplo 4: [-1, 7, -2, -8, 8, 5, 4, 3, 3]

Resultados encontrados:
   -> Suma Máxima: 23
   -> Subsecuencia: [8, 5, 4, 3, 3] (índices 4 a 8)
Tiempo de ejecución: 0.000005 segundos.

------------------------------------------------------------

Ejemplo 5: [4, 6, 8, 4, -2, 10, 2, -4, -7, 0, 8, -8]

Resultados encontrados:
   -> Suma Máxima: 32
   -> Subsecuencia: [4, 6, 8, 4, -2, 10, 2] (índices 0 a 6)
Tiempo de ejecución: 0.000007 segundos.

------------------------------------------------------------

Ejemplo 6: [-2, 1, 10, 4, -6, 9, -7, 2]

Resultados encontrados:
   -> Suma Máxima: 18
   -> Subsecuencia: [1, 10, 4, -6, 9] (índices 1 a 5)
Tiempo de ejecución: 0.000003 segundos.

```