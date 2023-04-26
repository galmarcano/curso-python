#Funciones, primera función:

def saludar(name):
    print(f'Hola {name}!')

saludar('Génesis')
saludar('Sebas')

#con dos parámetros:

def saludar_dos(name, lastname):
    print(f'Hola {name}, {lastname}!')

saludar_dos('Gene', 'Marcano')
saludar_dos('Marcano', 'Gene')
saludar_dos(lastname= 'Marcano', name = 'Gene')

#función multiplicar texto: si no defino multiplier hay que establecerlo al llamar la función, si lo defino pero luego al llamar 
#la función coloco otro valor, va a tomar el nuevo valor.

def multiplicar_texto(texto, multiplier = 2):
    print(texto * multiplier)

multiplicar_texto('Holo', 5)

#varietal acepta n parametros, y a partir del último que declares acepta cualquier cant de parámetros de cualquier tipo, 
# a partir de *others hace lo indicado anteriormente.

def varietal (param1, param2, *others):
    print(param1)
    print(param2)
    print(others)

varietal('1A', '2B', 0, 'XX', [1, 2])

#Al pasar doble asterisco en varietal produce un diccionario:
def varietal (param1, **others):
    print(param1)
    print(others)

varietal('1A', id = 0, name = 'Gene')
