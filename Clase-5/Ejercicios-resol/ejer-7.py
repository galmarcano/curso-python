#7. Cree una función notaFinal, que calcule la nota final de un estudiante en función de dos parámetros: una nota para el examen y 
#una cantidad de proyectos completados.
#    Esta función debe tomar dos argumentos: examen - calificación del examen (de 0 a 100); proyectos - número de proyectos 
#completados (de 0 en adelante);
#    Esta función debería devolver un número (calificación final). Hay cuatro tipos de calificaciones finales:
#    100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
#    90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
#    75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2.


def notaFinal(examen, proyectos):
    while examen < 0 or proyectos < 0:
        print("Ingrese solo valores positivos (nota de examen de 0 a 100, n° de proyectos de 0 en adelante)")
        examen = int(input("Ingrese la calificación del examen: "))
        proyectos = int(input("Ingrese n° de proyectos completados: "))

    if examen > 90 or proyectos > 10:
        return 100
    elif examen > 75 and proyectos >= 5:
        return 90
    elif examen > 50 and proyectos >= 2:
        return 75
    else:
        return 0

n_examen = int(input("Ingrese la calificación del examen: "))
c_proyectos = int(input("Ingrese n° de proyectos completados: "))
calificacion_final = notaFinal(n_examen, c_proyectos)
print("Su nota final es:", calificacion_final)