#verifique usuario y contraseña
usuario = input("Ingrese su usuario: ").lower()
if usuario == "admin":
    contraseña= input("Ingrese su contraeña: ")
    if contraseña == "1234":
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")