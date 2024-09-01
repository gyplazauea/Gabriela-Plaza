# Definición de una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función de búsqueda
def buscar_valor(matriz_busqueda, valor):
    for i in range(len(matriz_busqueda)):
        for j in range(len(matriz_busqueda[i])):
            if matriz_busqueda[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz."

# Definir el valor a buscar
valor_a_buscar = 5

# Realizar la búsqueda y mostrar el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)
