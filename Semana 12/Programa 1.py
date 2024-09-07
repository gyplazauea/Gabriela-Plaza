# Importar librería para operaciones matemáticas
import numpy as np

# Definir los datos de la matriz 3D para las temperaturas
# Matriz [ciudades][días de la semana][semanas]
temperaturas = np.random.randint(15, 35, (3, 7, 4))  # Ejemplo con 3 ciudades, 7 días, y 4 semanas

# Definir nombres de las ciudades
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]

# Paso 2: Iteración con bucles anidados para calcular el promedio semanal
promedios_semanales = []

for i in range(len(temperaturas)):  # Iterar sobre cada ciudad
    promedios_ciudad = []
    for j in range(len(temperaturas[i][0])):  # Iterar sobre cada semana
        suma_temperaturas = 0
        for k in range(len(temperaturas[i])):  # Iterar sobre cada día de la semana
            suma_temperaturas += temperaturas[i][k][j]
        promedio_semanal = suma_temperaturas / len(temperaturas[i])
        promedios_ciudad.append(promedio_semanal)
    promedios_semanales.append(promedios_ciudad)

# Paso 3: Mostrar los resultados en pantalla
for i in range(len(ciudades)):
    print(f"Promedios semanales para {ciudades[i]}:")
    for j in range(len(promedios_semanales[i])):
        print(f"Semana {j + 1}: {promedios_semanales[i][j]:.2f}°C")
    print()
