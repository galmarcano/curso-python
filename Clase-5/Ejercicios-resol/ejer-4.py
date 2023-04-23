#4. Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
#    Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), 
#    forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.
#	-Compañeros dicen que se hace con tupla

mes = int(input("Ingrese mes del año en número (1-12): "))

if mes >= 1 and mes <= 3:
    print("El mes ", mes, "forma parte del primer trimestre")
elif mes >=4 and mes <= 6:
    print("El mes ", mes, "forma parte del segundo trimestre")
elif mes >=7 and mes <= 9:
    print("El mes ", mes, "forma parte del tercer trimestre")
elif mes >=10 and mes <= 12:
    print("El mes", mes, "forma parte del cuarto trimestre")
else:
    print("Número de mes ingresado es incorrecto")