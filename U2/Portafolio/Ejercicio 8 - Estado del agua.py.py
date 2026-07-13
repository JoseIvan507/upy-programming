# Lee una temperatura en Celsius e imprime el estado fisico del agua
temp= float(input("Ingrese temperatura C°: "))
if temp <= 0:
    print("Solido (hielo)")
elif temp < 100:
    (print("Liquido (agua)"))
else:
    print("Gaseoso (vapor)")