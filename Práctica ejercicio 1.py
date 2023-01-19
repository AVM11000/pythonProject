
def divisor (numero):
    lista = []
    lista.append(numero)
    if (numero -1) % 2 ==1 and numero>0:
        while numero>1 and (numero - 1) % 2 == 1:
            numero = numero/2
            lista.append(int(numero))

        if lista[-1]==1:
            print("El número es divisible")
        else:
            print("Estos son los numeros conseguidos")
    else:
        print("Este numero no es divisible")
    return (lista)
print(divisor(100))





divisor(2)

