#2. utilizando dos while anidados, construya la tablas de mutiplicacion, ejemplo
#    Ejemplo whiole anidados:
#    while codicion1
#        while codicion2
#            .....

print("Tablas de multiplicación")

tabla = 1
tablafin = 10

while tabla <= tablafin:
    numero = 1
    while numero <= tablafin:
        print(tabla, "x", numero, "=", tabla*numero)
        numero += 1
    tabla += 1