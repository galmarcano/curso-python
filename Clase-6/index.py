#FOR IN: nos permite iterar estructuras. Sintaxis: for variable in estructura_iterable

words = "Esto es una cadena de texto"

for letter in words:
    print(letter)

#Si quiero que recorra palabra a palabra tendría que convertir la cadena a lista con split o de forma artesanal:

words = "Esto es una cadena de texto "

word = ''
for letter in words:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ''

print("\n-----\n")

#Se puede romper el ciclo del for con break:

words = "Esto es una cadena de texto "

word = ''
for letter in words:
    if letter != ' ':
        print(letter)
    else:
        break

#El for también sirve para recorrer listas:

animals_list = ['gato', 'perro', 'pájaro', 'pez']
for animal in animals_list:
    print(animal)

#Para rangos:

list1 = range (2,3)
print(list1)
for number in range(1,10):
    print(number)

#range(1,10,3) indica que recorra el rango del 1 al 10 de 3 en 3.

list1 = range (2,3)
print(list1)
for number in range(1,10,3):
    print(number)