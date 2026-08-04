palabra = input("Ingrese una palabra en infinitivo: ")
pronombres = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]
terminaciones = {
    "ar": ["o", "as", "a", "amos", "áis", "an"],
    "er": ["o", "es", "e", "emos", "éis", "en"],
    "ir": ["o", "es", "e", "imos", "ís", "en"],
}
raiz = palabra[:-2]
final = palabra[-2:]
if final in terminaciones:
    for pronombre, sufijo in zip(pronombres, terminaciones[final]):
        print(f"{pronombre} {raiz}{sufijo}")
