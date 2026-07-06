#problema10
num = int(input("Ingresa un número entero: "))
if num > 0:
    if num % 2 == 0:
        print("Positivo par")
    else:
        print("Positivo impar")
else:
    print("No es positivo")