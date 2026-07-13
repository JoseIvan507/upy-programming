#18 cuadricula de multiplicación
#Lee un #, se imprime una cuadricula #*#, un número que contendra una fila y una columna

n = int(input("Ingresa un número: "))
for r in range (1, n + 1):
    row = ""
    
    for c in range (1, n + 1):
        linea = linea + str(r + c) + "\t"
        print(linea)
    