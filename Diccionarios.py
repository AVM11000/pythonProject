#Crear diccionario
coche1={
    "marca":"Toyota",
    "matricula":"1234abc",
    "anyo_matriculacion": 2010,
    "modelo": "GLK",
    "km": 0.0,
    "tiene_aleron": True,
    "color":"Negro"
}

coche2 = {
    "marca":"Mercedes",
    "matricula":"4321PGH",
    "anyo_matriculacion": 2010,
    "modelo": "GLK",
    "km": 0.0,
    "tiene_aleron": True,
    "color":"Blanco"
}

#Yo quiero saber la marca de los coches
#get -> obtener el valor de una clave del diccionario
# print(coche.get("km"))


lista = ["rojo", "azul", "verde"]
lista[0]="amarillo"

# coche["marca"] = "skoda"
# coche["modelo"] = "fabia"
# print(coche)

#print("marca" in coche)

# Verificar que existe una clave en el diccionario
# tiene_marca = "marca" in coche


#len de un diccionario devuelve la cantidad de (clave:valor)
# print(len(coche))

#Añadir una clave con su valor a un diccionaio que ya existe
# coche ["num_puetas"] = 5
# print(coche)

#Eliminar el num de puertas
# coche.pop ("num puertas")
# print(coche)

#Eliminar la ultima clave
# coche.popitem()
# print(coche)

#del -> elimina por completo la variable
# del coche
# print(coche)

#Vamos a limpiar el diccionario
# coche.clear()
# print(coche)

#Creamos a parti de plantillav (copy)
# coche3= coche1_plantilla.copy()
# coche3["marca"] = "KIA"
# print(coche3)

#Ejemplo
palos = ["oro", "basto"]
valores= ["1", "rey", "caballo"]
list_cartas= []

# plantilla_carta = {
#     "palo": ""
#     "valor": ""
# }

# for palo in palos:
#     for valor in valores:
#         carta = plantilla_carta.copy()
#         carta["palo"] = palo
#         carta["valor"] =valor
#         print(carta)
#         list_cartas.append(carta)

# lista_ejemplo = list(("Hola", "Adios"))

# diccionario = dict()

#Keys -> devuelve la lista de claves del diccionario
# print(coche2.keys())

#Keys -> devuelve la lista de valores del diccionario
# print(coche2.values())

#Quiero crear un diccionaio a partir de las claves de otro
# coche3= dict.fromkeys(coche2)
# print(coche3)

#Items
# print(coche2.items())
