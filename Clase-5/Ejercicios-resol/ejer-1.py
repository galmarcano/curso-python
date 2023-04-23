#1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra 
#asociada con esa calificación. con al siguiente tabla
#    0   - 2     D
#    2.1 - 5     C
#    5.1 - 6     B
#    6.1 - 7     A

print("Ingrese solo valores del 0 - 7, por favor")
puntaje1 = float(input("Ingrese puntaje 1: "))
puntaje2 = float(input("Ingrese puntaje 2: "))
puntaje3 = float(input("Ingrese puntaje 3: "))
promedio = (puntaje1+puntaje2+puntaje3)/3
if promedio >= 6.1 and promedio <= 7:
    print("Tu promedio es A")
elif promedio >= 5.1 and promedio <= 6:
    print("Tu promedio es B")
elif promedio >= 2.1 and promedio <= 5:
    print("Tu promedio es C")
elif promedio >= 0 and promedio <= 2:
    print("Tu promedio es D")
else:
    print("No se reconoce el valor")