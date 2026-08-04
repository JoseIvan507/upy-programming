#18 archivo .png construir una ruta de respaldo = respaldos (.bak) verificar si existe o no 
import os

archivo = "foto.png"
nombre, ext = os.path.splitext(archivo)
respaldo = os.path.join("respaldos", nombre + ".bak")
print("respaldo:", respaldo)
print("original:", os.path.exists(archivo))