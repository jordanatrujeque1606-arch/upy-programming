# Ejercicio: Clasificación simple por peso
peso = float(input("Introduce tu peso en kg: "))
if peso < 50:
    print("Clasificación: Peso ligero")
elif peso <= 75:
    print("Clasificación: Peso promedio / normal")
elif peso <= 100:
    print("Clasificación: Peso elevado")
else:
    print("Clasificación: Peso muy elevado")