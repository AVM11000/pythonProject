#Ejercicio 1
# num1= 5
# num2 = 8
# def numero_mayor(num1, num2):
#     return num1 > num2



#Ejercicio 2

# def interes_en_banco(dinero_ingresar):
#     dinero_anyo_1 = dinero_ingresar * 1.05
#     dinero_anyo_2 = dinero_anyo_1* 1.05
#     dinero_anyo_3 = dinero_anyo_2 * 1.05
#     return dinero_anyo_3 - dinero_ingresar
#print(interes_en_banco(100))
# def interes_en_banco_2(dinero_ingresar):
#     porct_ganancia = 0.05 ** 3
#     return dinero_ingresar * porct_ganancia
# print(interes_en_banco_2(100))
# def interes_en_banco_3(dinero_ingresar):
#     ganancia_total = 0
#     dinero_actual= dinero_ingresar
#     for a in range(anyos):
#         ganancia_anyo = dinero_actual *0.05
#         dinero_actual += ganancia_anyo
#         ganancia_total += ganancia_anyo
#         return ganancia_total
#     print(interes_en_banco_3(100, 10))
# #Ejecicio 3
# def serie(num_inicio, intervalo, total_nums):
#
#     #Pintar el primer número de la serie
#     # print(num_inicio)
#
#     #Declaro una variable para saber el número por el que voy
#     num_por_el_que_voy =num_inicio
#     #Ir sumando al número por el que voy el intervalo
#     num_por_el_que_voy += intervalo
#     # print(num_por_el_que_voy)
#     #Pinto el siguiente número
#     # print(num_por_el_que_voy)
#
#     #Lo voy a hacer tantas veces como me diga el total números
#     for indice in range(total_nums -1):
#         num_por_el_que_voy += intervalo
#         # print(num_por_el_que_voy)
# #1,2,3,4,5,6
# serie(1,1,6)
# #Ejercicio 4
#
# def amazon(cant_peq, cant_med, cant_gran):
#
#     #Multiplicar cantidad pequeño * su peso
#     #->Peso de todos los pequeños
#     total_peques = cant_peq * 5
#     #Multiplicar cantidad medianos * su peso
#     #->Peso de todos los medianos
#     total_medianos = cant_med * 12.5
#     #Multiplicar cantidad grande * su peso
#     #->Peso de todos los grande
#     total_grandes = cant_gran * 25
#
#
#     #Sumar todos los pesos
#     peso_total = total_peques + total_medianos + total_medianos
#
#
#     #Calcular todos los camiones necesarios(peso máximo 1000kg)
#     numero_camiones = peso_total/1000
#
#     #Si el numerro de camiones da decimales -> suma 1 (Parte entera)
#     if isinstance(numero_camiones,float):
#         print(numero_camiones)
#     #SINO cojo la parte entera del numero
#     else:
#         numero_camiones = int(numero_camiones)
#
#     return numero_camiones
#
#
#
# print(amazon(200,0,0))
#Ejercicio 5

def cuenta_palabras(texto):

    #Pasar el texto a lista
    lista_palabras = texto.split("")

    #Contadores de palabras
    cont_1_letra =0
    cont_2_letra =0
    cont_3_letra =0
    cont_4_letra =0
    cont_5_letra =0
    cont_6_letra=0
    cont_7_letra=0
    cont_mas_7_letra=0
    #for each para recorrer cada palabra de la lista de palabras
#     for palabra in lista_palabras:
#
#         tamanyo_palabra = len(palabra)
#
#         if tamanyo_palabra ==1:
#             cont_1_letra +=1
#         if tamanyo_palabra ==2:
#             cont_1_letra +=1
#         if tamanyo_palabra ==3:
#             cont_1_letra +=1
#         if tamanyo_palabra ==4:
#             cont_1_letra +=1
#         if tamanyo_palabra ==5:
#             cont_1_letra +=1
#         if tamanyo_palabra ==6:
#             cont_1_letra +=1
#         if tamanyo_palabra ==7:
#             cont_1_letra +=1
#         if tamanyo_palabra >7:
#             cont_1_letra +=1
#
#
#     print("El número de palabras de 1 letra es:" +str (cont_1_letra))
#     print("El número de palabras de 1 letra es:" +str (cont_2_letra))
#     print("El número de palabras de 1 letra es:" +str (cont_3_letra))
#     print("El número de palabras de 1 letra es:" +str (cont_4_letra))
#     print("El número de palabras de 1 letra es:" +str (cont_5_letra))
#     print("El número de palabras de 1 letra es:" +str (cont_6_letra))
#     print("El número de palabras de 1 letra es:" +str (cont_7_letra))
#     print("El número de palabras de 1 letra es:" +str (cont_mas_7_letra))
#
# cuenta_palabras("""“Hoy se celebra en Sevilla la carrera llamada Nocturna del Guadalquivir , por
# lo que algunas calles sufrirán cortes a determinadas horas del día""")

#Otra manera de hacerlo
list_contadores = [0,0,0,0,0,0,0]

