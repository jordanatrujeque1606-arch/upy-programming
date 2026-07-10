numero = int(input("Introduce un número entero: "))
if numero > 0:
    estado_signo = "POSITIVO"
elif numero < 0:
    estado_signo = "NEGATIVO"
else:
    estado_signo = "CERO"
    
if numero % 2 == 0:
    estado_paridad = "PAR"
else:
    estado_paridad = "IMPAR"
if numero == 0:
    print("El número ingresado es CERO (y es PAR).")
else:
    print(f"El número {numero} es {estado_signo} e {estado_paridad}.")