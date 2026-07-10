# Ejercicio: Suma de 1 a N
n = int(input("Introduce un número entero límite (N): "))
suma_total = 0
for i in range(1, n + 1):
    suma_total = suma_total + i

print(f"La suma de todos los números desde 1 hasta {n} es: {suma_total}")