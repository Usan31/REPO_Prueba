x = float(input("inserta un numero"))
y = float(input("inserta otro"))
z = int(input("elige una opcion"))

if z == 0:
    suma = x + y
    suma = round(suma) 
    print(f"la suma de estos numeros es: {suma}")
elif z == 1:
    resta = x - y
    resta = round(resta)
    print(f"la resta de estos numeros es: {resta}")
elif z == 2:
    multi = x * y
    multi = round(multi)
    print(f"la multiplicacion de estos numeros es: {multi}")
elif z == 3: 
    divi = x / y
    divi = round(divi)
    print(f"la division de estos numeros es{divi}")
