def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de múltiples ciudades.

    Parámetros:
    datos_temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades y los valores
                               son listas con las temperaturas semanales.

    Retorna:
    dict: Un diccionario con las ciudades y sus respectivas temperaturas promedio.
    """
    promedio_ciudades = {}

    for ciudad, temperaturas in datos_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedio_ciudades[ciudad] = promedio

    return promedio_ciudades


# Ejemplo de uso:
datos_temperaturas = {
    'Ciudad1': [13, 55, 52, 20],
    'Ciudad2': [30, 12, 29, 51],
    'Ciudad3': [18, 40, 19, 37]
}

resultado = calcular_temperatura_promedio(datos_temperaturas)
print(resultado)
