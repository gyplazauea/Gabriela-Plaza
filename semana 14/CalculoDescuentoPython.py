# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Retornar el monto del descuento
    return descuento

# Programa principal
def main():
    # Llamada 1: Usando el valor predeterminado de descuento (10%)
    monto_total1 = 150  # Puedes cambiar este valor
    descuento1 = calcular_descuento(monto_total1)
    monto_final1 = monto_total1 - descuento1
    print(f"Monto total: ${monto_total1:.2f}")
    print(f"Descuento (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Llamada 2: Proporcionando un porcentaje de descuento personalizado
    monto_total2 = 250  # Cambia este valor según sea necesario
    porcentaje_descuento2 = 15  # Cambia este porcentaje
    descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
    monto_final2 = monto_total2 - descuento2
    print(f"Monto total: ${monto_total2:.2f}")
    print(f"Descuento ({porcentaje_descuento2}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")

if __name__ == "__main__":
    main()

