word = "La"
word2 = "de estos numeros es:"
word3 = """Elige una opcion

    0: suma
    1: resta
    2: multiplicacion
    3: division

Eliges... : """


def suma(x,y):
    suma = round(x + y) 
    print(f"{word} suma {word2} {suma}")

def resta(x,y):
    resta = round(x - y) 
    print(f"{word} resta {word2} {resta}")

def multi(x,y):
    multi = round(x * y) 
    print(f"{word} multiplicacion {word2} {multi}")

def divi(x,y):
    divi = round(x / y)
    print(f"{word} division {word2} {divi}")

x = float(input("inserta un numero:\n"))
y = float(input("inserta otro:\n"))
z = int(input(word3))

if z == 0:
    suma(x,y)
elif z == 1:
    resta(x,y)
elif z == 2:
    multi(x,y)
elif z == 3: 
    divi(x,y)