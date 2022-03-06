def saludo():
    print("Hola humano")

respuesta = str(input("Quieres que te salude?: "))

if respuesta == "si" or respuesta == "Si"\
or respuesta == "si " or respuesta == "Si "\
or respuesta == " si" or respuesta == " Si"\
or respuesta == " si " or respuesta == " Si ":
    saludo()
else: 
    print("Ta bien")
