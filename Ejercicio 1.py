texto1= "Me gusta beber cerveza en la alameda"

cadena_en_mayuscula = texto1.upper()
print(cadena_en_mayuscula)

cadena_en_minuscula = texto1.lower()
print(cadena_en_minuscula)

cadena_separada = texto1.split(" ")
print(cadena_separada)



print(len(cadena_separada))

remplazo= texto1.replace(" ", "")
print(remplazo)

print(len(remplazo))
cadena_con_solo_i = texto1.replace("a", "i")\
    .replace("e", "i").replace("o","i").replace("u", "i").replace("A", "i")

print(cadena_con_solo_i)
