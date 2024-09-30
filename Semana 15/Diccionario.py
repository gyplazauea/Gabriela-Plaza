# Creación del diccionario con Datos personal
Datos_personales = {
    "nombre": "Gabriela Plaza",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Modificar el valor de la clave "ciudad"
Datos_personales["ciudad"] = "Guayaquil"

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in Datos_personales:
    Datos_personales["telefono"] = "09988595149"

# Eliminar la clave "edad"
del Datos_personales["edad"]

# Imprimir el diccionario resultante
print(Datos_personales)
