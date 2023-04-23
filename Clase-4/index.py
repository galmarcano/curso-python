print("----Trabajando con diccionarios----")

empty_dict = {}
fullfiled_dict = {
    "name" : "Gene",
    "last_name" : "Marcano",
    "favourite_color" : "blue",
    "id" : 8,
}

print(empty_dict)
print(fullfiled_dict)

list_1 = ['a1', 'b2']
dict_converted = dict(list_1)
print(list_1, dict_converted)

tuple_1 = ('a1', 'b2')
print(tuple_1, dict(tuple_1))

list_dimensional = [['a', 1], ['b', 2]]
print(list_dimensional, dict(list_dimensional))

#Obtener un elemento
color = fullfiled_dict["favourite_color"]
print(color)

#Añadir un elemento
fullfiled_dict["pets_name"] = "Zero"
print(fullfiled_dict)

#Modificar un elemento
fullfiled_dict["last_name"] = "Pérez"
print(fullfiled_dict)

#Eliminar un elemento
del fullfiled_dict["id"]
print(fullfiled_dict)

fullfiled_dict.pop("favourite_color")
print(fullfiled_dict)

#Lista vacía

empty_dict2 = dict()
print(empty_dict2)

#No funciona, revisar
#fullfiled_dict_2 = (
   # nom = "Gene",
  #  ap = "Marcano"
#)
#print(fullfiled_dict_2)

empleado = {
    "nombre" : "Gene",
    "apellido" : "Marcano",
    "color favorito" : "blue",
    "edad" : 8,
}

#Recorrer el diccionario por valores
print(empleado)
for variables in empleado.values():
    print(variables)

#Recorrer el diccionario por clave y valor, se puede colocar a y b
#Cualquier nombre para las variables
print(empleado)
for clave, valor in empleado.items():
    print(clave, valor)


print("----Trabajando con condicionales----")

edad = 50
if edad < 50:
    print("Eres viejo")
    print("Disfruta igual")

print ("Holoo")

temperatura = 60
if temperatura >= 60:
    print("Temperatura alta")
else:
    print("Temperatura normal")

temperatura = 20
if temperatura < 10:
    print("Es altamente probablemente que llueva")
elif temperatura >= 10 and temperatura <= 20:
    print("Es medianamente prob que llueva")
else:
    print("No hay probabilidad de que llueva")

print("---Ejercicio con if---")
puede_volar = "no"
es_humano = "si"
mascara = "si"
if puede_volar == "si" and es_humano == "si" and mascara == "si":
    print("El personaje es Falcon")
elif puede_volar == "si" and es_humano == "si" and mascara == "no":
    print("El personaje es Iron Man")
elif puede_volar == "si" and es_humano == "no" and mascara == "si":
    print("El personaje es Silver Surfer")
elif puede_volar == "si" and es_humano == "no" and mascara == "no":
    print("El personaje es Rocket Raccoon")
elif puede_volar == "no" and es_humano == "si" and mascara == "si":
    print("El personaje es Deadpool")
elif puede_volar == "no" and es_humano == "si" and mascara == "no":
    print("El personaje es Black Widow")
elif puede_volar == "no" and es_humano == "no" and mascara == "si":
    print("El personaje es Thanos")
elif puede_volar == "no" and es_humano == "no" and mascara == "no":
    print("El personaje es Hulk")
else:
    print("No puedo encontrar el personaje")

print("---TRABAJANDO CON CICLOS, WHILE 1---")

want_exit = "n"
while want_exit == "n":
    print("Hola, como estás?")
    want_exit = input("Quieres salir?")
print("Fuera del while")

print("---TRABAJANDO CON CICLOS, WHILE 2---")
#Break, nos permite romper el ciclo
want_exit = "n"
num_questions = 0
while want_exit =="n":
    print("Hola, como estás?")
    want_exit = input("Quieres salir S/N?")
    num_questions += 1
    if num_questions == 3:
        print("Alcanzaste el máximo")
        break
print("Fuera del while")




