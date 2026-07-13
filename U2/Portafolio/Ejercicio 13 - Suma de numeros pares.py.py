#13 suma de números pares
#sumar numeros pares hasta el número N

n = int(input("Ingresa un número: "))
res = 0
for i in range (2, n + 1, 2):
    res = res + i
    
print("El resultado de la suma es: ", res)