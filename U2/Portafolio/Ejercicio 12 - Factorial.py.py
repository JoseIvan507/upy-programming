#12 factorial

n = int(input("Ingresa un número: "))
total = 1
i = 1

while (i <= n):
    total= total * i
    i = i + 1
    
print("El factorial es igual a: ", total)