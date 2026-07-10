#Ejercicio 2 valor dentro de un rango
LIMITE_INFERIOR = 10
LIMITE_SUPERIOR = 50

try:
    valor = float(input(f"Introduce un número entre {LIMITE_INFERIOR} y {LIMITE_SUPERIOR}: "))
    
    if valor >= LIMITE_INFERIOR and valor <= LIMITE_SUPERIOR:
        print(f"¡Perfecto! El número {valor} ESTÁ dentro del rango.")
    else:
        print(f"Error: El número {valor} se sale del rango permitido.")
except ValueError:
    print("Eso no es un número válido.")