import random

def crear_baraja ():
    palos = ["oro", "espada", "basto", "copas"]
    tipos= [1, 2, 3, 4, 5, 6, 7, "sota", "caballo", "rey"]
    valores= [0.0]
    list_cartas =[]

    plantilla_carta= {
        "tipo":"",
        "palo":"",
        "valor":"",
    }
    for palo in palos:
        for tipo in tipos:
            plantilla_carta["palo"] = palo
            plantilla_carta["tipo"] = tipo
            if tipo == "sota" or tipo =="caballo" or tipo == "rey":
                plantilla_carta["valor"] = 0.5
            else:
                plantilla_carta["valor"] = tipo
            carta = plantilla_carta.copy()
            list_cartas.append(carta)
            print(carta)
    return list_cartas


crear_baraja()

def barajar ():
    cartas= crear_baraja()
    cartas_barajadas =[]
    for carta in cartas:
        x=random.randint (0, len(cartas_barajadas))
        cartas_barajadas.insert(x, carta)
    return cartas_barajadas
print(barajar())