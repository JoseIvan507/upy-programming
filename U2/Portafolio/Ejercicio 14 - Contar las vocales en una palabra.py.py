#14 vocales dentro de una palabra

palabra = input("Ingresa una palabra: ")
contador = 0
for i in palabra.lower():
    if i in "aeiou":
        contador = contador + 1
print(f"La palabra {palabra} tiene ",contador," vocales")