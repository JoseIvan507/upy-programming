usuarios = {
    "jperez": {"password": "1234", "rol": "alumno", "nombre": "Juan Perez"},
    "amartin": {"password": "1234", "rol": "alumno", "nombre": "Ana Martín"},
    "dgimenez": {"password": "1234", "rol": "alumno", "nombre": "Didier Gimenez"},
    "cmedina": {"password": "1234", "rol": "alumno", "nombre": "Camila Medina"},
    "vcachon": {"password": "1234", "rol": "alumno", "nombre": "Veronica Cachon"},
    "falcocer": {"password": "1234", "rol": "alumno", "nombre": "Fabio Alcocer"},
    "mlopez": {"password": "1234", "rol": "maestro", "nombre": "Maria López"},
    "rgarcia": {"password": "1234", "rol": "coordinador", "nombre": "Rosa García"},
}
materias = ("Matemáticas", "Programación", "Inglés")
calificaciones = {
    "jperez": {"Matemáticas": 8.5, "Programación": 9.0, "Inglés": 7.5},
    "amartin": {"Matemáticas": 10.0, "Programación": 8.0, "Inglés": 5.0},
    "dgimenez": {"Matemáticas": 9.0, "Programación": 8.5, "Inglés": 9.0},
    "cmedina": {"Matemáticas": 7.0, "Programación": 10.0, "Inglés": 10.0},
    "vcachon": {"Matemáticas": 7.8, "Programación": 9.0, "Inglés": 7.0},
    "falcocer": {"Matemáticas": 8.7, "Programación": 8.0, "Inglés": 8.0},
}
while True:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    datos_user = usuarios.get(usuario)
    if datos_user and datos_user["password"] == contraseña:
        break
    print("Usuario o Contraseña incorrecta")
rol = datos_user["rol"]
nombre = datos_user["nombre"]
print(f"Bienvenido, {nombre} ({rol})")
if rol == "alumno":
    materias_aprobadas = set()
    materias_reprobadas = set()
    califs_alumno = calificaciones.get(usuario, {})
    print(f"Boleta de {nombre}")
    for materia, calif in califs_alumno.items():
        print(f"{materia} : {calif}")
        if calif >= 8:
            materias_aprobadas.add(materia)
        else:
            materias_reprobadas.add(materia)
    print(f"Materias aprobadas: {materias_aprobadas}")
    print(f"Materias reprobadas: {materias_reprobadas}")
elif rol == "maestro":
    alumno = input("Ingrese el usuario del alumno deseado: ")
    materia = input("Ingrese la materia deseada: ")
    calificacion = float(input("Ingrese la nueva calificación: "))
    if alumno in calificaciones:
        calificaciones[alumno][materia] = calificacion
        print(f"Alumno: {alumno}\nMateria: {materia}\nNueva calificación: {calificacion}\nCalificación actualizada.")
    else:
        print("El alumno no existe.")
else:
    for u in usuarios.values():
        if u["rol"] == "maestro":
            print(f"Maestra/o {u['nombre']}")
    for materia in materias:
        print(materia)
    for est_id, califs in calificaciones.items():
        nom_est = usuarios[est_id]["nombre"]
        print(f"Estudiante {nom_est}: {califs}")
