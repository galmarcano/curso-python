#5. Escriba un programa que eliminar un signo de exclamación del final de una cadena. 
#    puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

cadena = input("Ingrese su texto: ")
if cadena[-1] == "!":
    print(cadena[:-1])
else:
    print(cadena)
