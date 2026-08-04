import csv

# 1. Crear el archivo de ejemplo "ventas.csv"
with open("ventas.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["producto", "unidades", "precio"])
    w.writerow(["Lapiz", 10, 5])
    w.writerow(["Cuaderno", 3, 30])

# 2. Leer con DictReader, calcular el total y escribir en "reporte.csv" con DictWriter
with open("ventas.csv", "r") as ent, open("reporte.csv", "w", newline="") as sal:
    lector = csv.DictReader(ent)
    # Definimos los campos originales más la nueva columna "total"
    escritor = csv.DictWriter(sal, fieldnames=["producto", "unidades", "precio", "total"])
    escritor.writeheader()
    
    for fila in lector:
        # Convertimos a entero para realizar la multiplicación aritmética
        fila["total"] = int(fila["unidades"]) * int(fila["precio"])
        escritor.writerow(fila)

# 3. Mostrar el contenido del reporte generado
with open("reporte.csv", "r") as f:
    print(f.read())

# Output:
# producto,unidades,precio,total
# Lapiz,10,5,50
# Cuaderno,3,30,90