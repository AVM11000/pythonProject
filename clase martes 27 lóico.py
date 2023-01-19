num1= 7
num2= 2


#Operadores lógicos

#Siempre devuelven un dato de tipo boolean (SI y NO)

#Mayor que
mayor_que = num1 > num2
#print(mayor_que)

#Menor que
menor_que = num1 < num2
#print(menor_que)

#Unir condiciones
#and
#print(mayor_que and menor_que)
#print(mayor_que and mayor_que)
#print(menor_que and menor_que)


#or
#print(menor_que or mayor_que) #True o False --->True
#print(mayor_que or mayor_que) #True or True --->True
#print(menor_que or menor_que)#False o False --->True
#not
#print(not menor_que or mayor_que) #False o False ---> False
#print (not(menor_que or mayor_que)) #False (se escibe así si queemos coger todas las conidiciones)
#print(not (mayor_que and menor_que)) #not (False)---> True

#Membresía
text1 = "Colegio Safa Reyes"
text2 = "Reyes"

list_1 =[1,2,3,4]
num_1 =6
#print(num_1 in list_1)
#print(text2 in text1)

#Conversiones
num = 3
text = "Viernes"
bol = True
decimal = 8.3
str ()#Pasar un dato a texto
int()#Pasar un dato a número
bool()#Pasar un dato a boolean
float()#Pasar un dato a decimal
#print(float(num))
#print(float(text))
#print(float(bol))

