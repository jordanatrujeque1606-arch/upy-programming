#Ejercicio 1 año bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
try:
    anio = int(input("Introduce un año: "))
    
    if es_bisiesto(anio):
        print(f"¡El año {anio} es bisiesto!")
    else:
        print(f"El año {anio} no es bisiesto.")
except ValueError:
    print("Por favor, introduce un número válido.")