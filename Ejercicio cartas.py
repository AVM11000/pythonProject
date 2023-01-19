#Ejercicio 1
"""Se desea realizar un método que a partir de las tres listas que se van a mostrar a continuación,
devuelva una lista de diccionario de cartas. Las listas que toma como partida son:
tipo = [1,2,3,4,5,6,7, Sota, Caballo, Rey] (Cadenas)
palos= [“Oro”, “Basto”, “Copa”, “Espadas”]
El diccionario que compondría la carta sería el siguiente:
carta = {
tipo: “1”,
palo: “Oro”,
valor: 0.0
}
Se tiene que devolver una lista de diccionarios, con todas las cartas de los 4 palos de la
baraja."""
import random


def crear_baraja ():
    palos = ["oro", "espada", "basto", "copas"]
    tipos= ["1", "2", "3", "4", "5", "6", "7", "sota", "caballo", "rey"]
    valores= [0.0]
    list_cartas =[]

    plantilla_carta= {
        "tipo":"",
        "palo":"",
        "valor":"",
    }
    for palo in palos:
        for tipo in tipos:
            for valor in valores:
                plantilla_carta["palo"] = palo
                plantilla_carta["tipo"] = tipo
                plantilla_carta["valor"] = valor
                carta = plantilla_carta.copy()
                list_cartas.append(carta)
                print(carta)
    return list_cartas


crear_baraja()

"""Se desea realizar un método que reciba una lista de diccionarios de cartas y ponga las cartas
en posiciones aleatorias, simulando la acción de barajar. El método también devuelve una
lista de diccionarios con las cartas barajadas."""
def barajar ():
    cartas= crear_baraja()
    cartas_barajadas =[]
    for carta in cartas:
        x=random.randint (0, len(cartas_barajadas))
        cartas_barajadas.insert(x, carta)
    return cartas_barajadas
print(barajar())

"""Se desea realizar un método que simule la acción de repartir. Para ello el método recibe tres
parámetros:
● num_jugadores (int)
● num_cartas_por_jugador (int)
● baraja (list[diccionario])
El método debe devolver tantas listas como jugadores, y cada lista con el número de cartas
por jugador, sin repetir ninguna carta entre los jugadores. Además nada más empezar el
método hay que comprobar que el número de jugadores y las cartas que toca a cada jugador,
no supere el tamaño de la baraja. En el caso de no cumplirse la condición el método
devolverá un mensaje diciendo “Número de jugadores y cartas no válido”."""

def repartir (num_jugadores, num_cartas_jugador):
    monton = []
    crear_baraja = barajar()
    if num_jugadores + num_cartas_jugador > len(crear_baraja):
        return "Número de jugadores y cartas no válidos"
    for jugador in range(num_jugadores):
        montones= crear_baraja[0:num_cartas_jugador]
        monton.append(montones)
        crear_baraja=crear_baraja[num_cartas_jugador:]
        print("jugador" + str(jugador) + "-->"+ str(montones))
    return monton
repartir(3,3)
