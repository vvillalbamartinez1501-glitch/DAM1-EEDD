"""

1.1. Declare una lista L0 de forma que L0=[[1,2,3],['A','B','C'], "EED", "DAM"]
1.2 Obtener L1 de manera que L1=[[1,2,3,3,2,1],['ABCCBA'], "EEDDAM", "MADDEE"] 
L1 se obtendrá haciendo uso de rangos y con funciones como append, extend, sorted, etc.
No se considerará válida la obtención L1 de forma introduciendo sus elementos individualmente
o directamente copiando y pegando la definición de L1 (2 Ptos.)
"""

L0 = [[1, 2, 3], ['A', 'B', 'C'], "EED", "DAM"]
L1 = []
L1.append(L0[0] + L0[0][::-1])
L1.append(["".join(L0[1]) + "".join(L0[1])[::-1]])
L1.append(L0[2] + L0[3])
L1.append(L0[3][::-1] + L0[2][::-1])

print(L1)

"""
2.1.	Cree un diccionario dicc de forma que se asignen las claves ‘a’, ‘e’, ‘i’, ‘o’, ‘u’ a los valores 0, 1, 2, 3 y 4 ( 0,5 Ptos.)
2.2.	Determinar el valor correspondiente a la clave más alta (orden alfabético) (0,5 Ptos.)
2.3.    Solicite al usuario la introducción de una cadena y muestre el resultado de su cifrado. La cadena resultante siempre estará en minúsculas.
        Ejemplo: Si el usuario introduce "Hola", la cadena resultante será "h3l0" (1 Pto.)
"""
dicc = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

valor_max = dicc[max(dicc.keys())]

cadena = input("Introduzca una cadena: ").lower()
cifrado = "".join([str(dicc.get(letra, letra)) for letra in cadena])
print("Cadena cifrada: ")
print(cifrado)


"""
3.	Escriba un código que sume una lista con varias subListas de valores ENTEROS
    El código obtendrá la suma de todos los elementos de forma iterativa (no recursiva) de manera que:
	Si algún elemento de una sublista no es valor entero se tratará como si fuera 0
	Si la lista principal no contiene una sublista de valores enteros en alguna de sus posiciones se tratará como valor 0.
	Las comprobaciones anteriores SE RESOLVERÁN MEDIANTE EXCEPCIONES (3 puntos)
	Ejemplo de uso:
	  L1=[ [0,1,2], [2,2,2], [2,1] ]
	  Se obtendrá el valor 12
	  L2=[ 'no soy una sublista de enteros', [2,2,'no soy un valor entero'], [2, 99.9999999999] ]
	  Se obtendrá el valor 6
"""

L2 = ['no soy una sublista de enteros', [2, 2, 'no soy un valor entero'], [2, 99.9999999999]]
suma_total = 0

for sublista in L2:
    try:
        if isinstance(sublista, str):
            raise TypeError
        for elemento in sublista:
            try:
                if type(elemento) is not int:
                    raise ValueError
                suma_total += elemento
            except ValueError:
                pass
    except TypeError:
        pass

print(suma_total)


