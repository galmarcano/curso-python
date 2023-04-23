# 3. Escriba un programa que calcule el máximo común divisor entre dos números enteros.

print("Máximo común divisor entre dos números enteros")

def mcd():
    while True:
        try:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Solo puede ingresar un número entero")
        
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

max_cd = mcd()
print("El máximo común divisor es:", max_cd)