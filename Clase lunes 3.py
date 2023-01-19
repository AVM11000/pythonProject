#Declaración de lisats
# lista_numeros = [3, 4, 7, 89, 90]
# lista_frutas = ["melón", "sandía", "plátano", "uva"]

#Acceder a los datos de una lista

# num = lista_numeros[2]
# fruta = lista_frutas[0]
# ultima_fruta = lista_frutas[-2]
# print(num)
# print(fruta)
# print(ultima_fruta)

#Acceso a rango de elementos o sublistas
# tres_ultimos_elementos = lista_frutas[:-1]
# print(tres_ultimos_elementos)

#Modiicar elementos
# lista_frutas [1] = "Manzana"
# var_manzana = lista_frutas[1]
# print(var_manzana)
#Añadi elementos a una lista
# lista_frutas.append("kiwi")
# lista_frutas.insert(2, "zanahoria")
# print(lista_frutas)

#Eliminar elementos
# lista_frutas.remove("zanahoria")
# lista_frutas.pop (-1)
# print(lista_frutas)

#Borrar una lista completa
# del(lista_frutas)
# print(lista_frutas)
# lista_frutas.clear()
# print(lista_frutas)
# del lista_frutas[1]
# print(lista_frutas)

#Combinar y unir listas
# lista_frutas_1 =["manzana", "sandía"]
# lista_verduras =["pimiento", "cebolla"]
# lista_fruteria = []
# lista_fruteria.append(lista_frutas_1)
# print(lista_fruteria)

# lista_fruteria.extend(lista_frutas_1)
# lista_fruteria.extend(lista_verduras)
# print(lista_fruteria)

#Orden inverso
# lista_invertida = lista_fruteria.copy()
# lista_invertida.reverse()
# lista_fruteria.reverse()
# print(lista_fruteria)
# print(lista_invertida)

#Construcor de listas
# lista_3= list (("azul", "rojo", "verde"))
# print(lista_3)

#Ordenación de listas
# lista_fruteria.sort()
# print(lista_fruteria)

#Tamaño de lista
# print(len(lista_fruteria))

#Contar elementos
# print(lista_3.count("rojo"))

#Saber índice de un elemento
# print(lista_3.index("rojo"))

#Elemento está en una lista
# esta_contenido="amarillo" in lista_3
# print(esta_contenido)
# print(lista_3.index("amarillo"))

#Bucles con listas
# for color in lista_3:
#         if color=="rojo":
#             count_rojo+=1
# print("Encontrado" + str (count_rojo))