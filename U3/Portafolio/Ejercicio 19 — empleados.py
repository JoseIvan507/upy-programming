#19 emplados.csv  nombre,sueldo, y fila por empleado , calcular la suma de todos los sueldos 

import csv

with open ("empleados.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["nombre", "sueldo"])
    writer.writerow(["Ana", 1800])
    writer.writerow(["Jorge", 2800])
    writer.writerow(["Rodrigo", 3000])
    writer.writerow(["Didier", 2300])
    writer.writerow(["Francisco", 4000])

total = 0
with open ("empleados.csv", "r") as f:
    for fila in csv.DictReader(f):
        total = total + int(fila["sueldo"])
         
print(total)

