
#def opera_cadenas(texto1):
    #cadena_en_mayuscula = texto1.upper()
    #print(cadena_en_mayuscula)

    #cadena_en_minuscula = texto1.lower()
    #print(cadena_en_minuscula)

    #cadena_separada = texto1.split(" ")
    #print(cadena_separada)

    #print(len(cadena_separada))

    #remplazo = texto1.replace(" ", "")
    #print(remplazo)

    #print(len(remplazo))
    #cadena_con_solo_i = texto1.replace("a", "i") \
        #.replace("e", "i").replace("o", "i").replace("u", "i").replace("A", "i")

    #print(cadena_con_solo_i)

#Vamos a hacer una llamada al método
#opera_cadenas("Me llamo Julio")

#Suma de dos números
def suma_dos_numeros(numero1,numero2):
    return (numero1+numero2)

def calcula_nota_media_tipo_test(nota_test1, nota_test2):
    # Sumar todas las notas
    suma_notas = suma_dos_numeros(nota_test1,nota_test2)

    # Las divido /2
    nota_media = suma_notas /2
    return nota_media

#Ejecutar nota media
print(calcula_nota_media_tipo_test(7.3, 8.7))