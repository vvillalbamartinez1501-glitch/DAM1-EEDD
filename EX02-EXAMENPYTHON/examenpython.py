# 1

L0 = [[1, 2, 3], ['A', 'B', 'C'], "EED", "DAM"]
L1 = []
L1.append(L0[0] + L0[0][::-1])
L1.append(["".join(L0[1]) + "".join(L0[1])[::-1]])
L1.append(L0[2] + L0[3])
L1.append(L0[3][::-1] + L0[2][::-1])

print(L1)


# 2

dicc = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

valor_max = dicc[max(dicc.keys())]

cadena = input("Introduzca una cadena: ").lower()

cifrado = "".join([str(dicc.get(letra, letra)) for letra in cadena])
print("Cadena cifrada: ")
print(cifrado)

# 3

L1=[ [0,1,2], [2,2,2], [2,1] ]


L2 = ['no soy una sublista de enteros', [2, 2, 'no soy un valor entero'], [2, 99.9999999999]]
suma_total = 0

def sumar_sublistas(lista_principal):
    suma_total = 0
    for sublista in lista_principal:
        try:
            if isinstance(sublista, str) or not hasattr(sublista, '__iter__'):
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
    return suma_total

print("Ejemplo lista de enteros:")
print(L1)
print(sumar_sublistas(L1))

print("Ejemplo lista de no enteros:")
print(L2)
print(sumar_sublistas(L2))