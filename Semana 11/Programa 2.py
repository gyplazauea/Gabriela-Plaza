# Definición de una matriz 3x3
matriz = [
    [3, 1, 2],
    [9, 7, 8],
    [6, 5, 4]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz_a_ordenar, indice_fila):
    n = len(matriz_a_ordenar[indice_fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz_a_ordenar[indice_fila][j] > matriz_a_ordenar[indice_fila][j+1]:
                matriz_a_ordenar[indice_fila][j], matriz_a_ordenar[indice_fila][j+1] = matriz_a_ordenar[indice_fila][j+1], matriz_a_ordenar[indice_fila][j]
    return matriz_a_ordenar

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila específica (por ejemplo, la fila 1)
fila_a_ordenar = 1
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
