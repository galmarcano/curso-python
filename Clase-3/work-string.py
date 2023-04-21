first_name = "Génesis"
last_name = "Marcano"
print(first_name + " " + last_name)

#Para replicar mensajes
mensaje1 = ("Hola ") * 3
print(mensaje1)

#Concatenar string
mensaje3 = "Daniela"
print(mensaje3)
mensaje3 += " es mi seg nombre"
print(mensaje3)
mensaje3 += "bueno?"
print(mensaje3)

#Imprime longitud de la cadena
print(len(mensaje3))
print(len(mensaje1))

#Para buscar algo dentro de la cadena
cadena = "la pelota azul de Zero"
posicion = cadena.find("verde")
print("verde está en:" , posicion)
posicion = cadena.find("azul")
print("azul está en:" , posicion)

#Lower, función para colocar en minúsculas una cadena
cadena = "LETRAS MAYÚSCULAS"
cadena_minusculas = cadena.lower()
print(cadena_minusculas)

#Replace, función para reemplazar algo dentro de la cadena
cadena = "Génesis Pérez"
cadena_modificada = cadena.replace("Pérez", "Marcano")
print(cadena_modificada)

print("-----Listas-----")
empty_list = []
print(empty_list)
fulfilled_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Richar"}, (1, 3, 5)]
print(fulfilled_list)

second_list = list()
print(second_list)

#List también convierte a lista
print(list("Concurso"))

range_one = range(50)
print(list(range_one))

#Función append, agregar elemento al final de la lista
numeros = [1, 4, 6]
print(numeros)
numeros.append(10)
print(numeros)

#Para buscar dentro de una lista, entre corchetes la posición que quiero buscar, recordar que 
#comienza en 0.
print(numeros[2])

#Para insertar un número en una posición específica
numeros = [1, 2, 3]
numeros.insert(2, 10)
print(numeros)

#Iterar en una lista. Repetir el mismo proceso para cada elemento de la lista:
lista = ["a", "hola", "j", 4, 5]

for elemento in lista:
    print(elemento)

#Eliminar elemento de una lista
lista = ["manzana", "naranja", "pera", "sandía"]
lista.remove("pera")
print(lista)

#Averiguar el del para eliminar de la lista

#o se puede hacer usando el índice
lista = ["manzana", "naranja", "pera", "sandía"]
lista.pop(2)
print(lista)

#Para modificar una lista, hay varias opciones:
lista = ["manzana", "naranja", "pera", "sandía"]
lista[2] = "uva"
lista.extend(["mango", "piña"])
print(lista)

#También está la siguiente, donde se pueden indicar varios índices a reemplazar
lista = ["manzana", "naranja", "pera", "sandía"]
lista[1:3] = ["melón", "cereza"]
print(lista)

#Para tuplas. Inmutables
#Todas las variables y todos los tipos de datos en Python son tipados dinámicamente, dentro de
#sus elementos pueden almacenar diferentes tipos de datos
print("----Tuplas----")

empty_tupla = ()
fulfilled_tupla = (1, 2, "Gene")
print(empty_tupla, fulfilled_tupla)

print(type(fulfilled_tupla))

#De un solo elemento son string, no son tuplas, si necesito que sea una tupla con 
#un solo elemento le agrego una coma al final
one_tupla = ("Juan")
print(type(one_tupla))

one_tuple = ("Juan",)
print(type(one_tuple))

#Se puede imprimir tupla vacía
empty_tuple_2 = tuple()
print(empty_tuple_2)

list_to_convert = [2, 6, 7, 10]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)

#Función reverse: invierte el orden de los elementos
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

#Cuál es la diferencia con función reversed?

#Append. Agrega un elemento a la lista:
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)

#Extend. Extender con varios elementos, lista dentro de listas