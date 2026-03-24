# variables numericas
entero = 2 
print("Integer:", entero)
print("Tipo de variable enteros:", type(entero))

decimal = 2.5
print("Float:", decimal)
print("Tipo de variable float:", type(decimal))

booleano = True
print("Booeano",booleano)
print("Tipo de variable boolean:",booleano)

cadena = "Hola, Mundo"
print("Cadenas:",cadena)
print("Tipo de caruable string",type(cadena))

def pedirNumero(texto):
    print(texto)
    numero = input()
    return numero

def imprimirEdad():
    edad = pedirNumero("Introduce tu edad")
    int(edad)
    if edad < 18:
        print("Eres menor de edad")
    else: 
        print("Eres mayor de edad")
# imprimirEdad()


# peticion de datos
def calcularEdad():
    fechaNacimiento = input("En qué año naciste?")
    anioNacimiento = int(fechaNacimiento)
    print("Tienes" , 2026 - anioNacimiento,"años")
    print(type(anioNacimiento))

vf = 3.141592653589793238462638327950288419716939937510592307
print((vf))

vf=float("2.3")
print("vf: ",vf)
vf = 3.9

