#año bisiesto
year = int(input("Enter a year: ")) #str

if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print(f"{year} is Lap year")
else:
    print(f"{year} Is not lap year")
