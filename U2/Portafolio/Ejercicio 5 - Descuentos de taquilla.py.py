n=int(input(" Insert a number: "))
if n % 2== 0:
    print(f"{n} es par")
else:
    print(f"{n} no es par")
    

color= input("ingresa un color: ").lower()
if color == "red":
    print("alto")
elif color == "yellow" :
    print("cuidado")
elif color == "green":
    print("avance")