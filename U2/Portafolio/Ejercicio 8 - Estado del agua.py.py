#Estado del agua
temperatura = float(input("Introduce la temperatura del agua en °C: "))
if temperatura <= 0:
        print("El agua está en estado SÓLIDO (Hielo).")
elif temperatura < 100:
        print("El agua está en estado LÍQUIDO (Agua). 💧")
else:
        print("El agua está en estado GASEOSO (Vapor). 💨")

