#15 primer multiplo de 7 entre 1 rango /break y continues/
#ingrese 2 números, A y B. %7, break/ para parar el codigo

a = int(input("Ingresa un número para epezar el rango: "))
b = int(input("Ingresa un número para finalizar el rango: "))

for n in range (a, b+1):
    if n %7 == 0:
        print("Primer multiplo de 7: ",n)
        break