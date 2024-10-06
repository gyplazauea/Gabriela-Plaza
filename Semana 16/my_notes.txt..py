# Crear un archivo de texto y escribir tres líneas de notas personales
# Abro el archivo my_notes.txt en modo escritura ("w") para crear o sobrescribir el archivo
with open("my_notes.txt", "w") as archivo:
    archivo.write("Nota 1: Hoy practiqué cómo manejar archivos en Python.\n")
    archivo.write("Nota 2: Es importante cerrar los archivos después de usarlos.\n")
    archivo.write("Nota 3: Estoy empezando a sentirme más cómodo con el uso de archivos.\n")

# Leer el archivo de texto línea por línea
# Ahora abro el archivo my_notes.txt en modo lectura ("r")
with open("my_notes.txt", "r") as archivo:
    # Leo e imprimo cada línea del archivo usando un bucle
    linea = archivo.readline()  # Leo la primera línea
    while linea:  # Mientras haya contenido en la línea
        print(linea, end='')  # Muestro la línea sin agregar un salto de línea adicional
        linea = archivo.readline()  # Leo la siguiente línea
