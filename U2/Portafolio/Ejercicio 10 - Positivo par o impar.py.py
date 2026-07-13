#lee un numero
num = int(input("Ingrese un numero: "))
if num >0:
    if num % 2 == 0:
        print("Positivo par")
    else:
        print("Positivo impar")
else:
    print("El numero no es positivo")