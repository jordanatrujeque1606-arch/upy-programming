# Ejercicio: Descuentos en taquilla
PRECIO_BASE = 100  
edad = int(input("Introduce la edad del cliente: "))

if edad < 5:
        precio_final = 0
        print(f"¡Entrada gratis por ser menor de 5 años! Precio: ${precio_final}")
elif edad <= 17:
        precio_final = PRECIO_BASE * 0.50  # 50% de descuento
        print(f"Descuento de estudiante/niño (50%). Precio final: ${precio_final}")
elif edad <= 64:
        precio_final = PRECIO_BASE  # Precio completo
        print(f"Entrada normal de adulto. Precio final: ${precio_final}")
else:
        precio_final = PRECIO_BASE * 0.70  # 30% de descuento (paga el 70%)
        print(f"Descuento de adulto mayor (30%). Precio final: ${precio_final}")


   