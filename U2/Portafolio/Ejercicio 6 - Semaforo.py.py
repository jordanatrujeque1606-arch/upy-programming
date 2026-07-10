# Ejercicio: Control de un semáforo
color = input("¿De qué color está el semáforo? (rojo / amarillo / verde): ").lower()
if color == "rojo":
    print("¡ALTO! No puedes pasar.")
elif color == "amarillo":
    print("¡PRECAUCIÓN! Baja la velocidad y prepárate para frenar.")
elif color == "verde":
    print("¡SIGA! Puedes avanzar de forma segura.")
else:
    print("Color no reconocido. Por favor, escribe rojo, amarillo o verde.")

