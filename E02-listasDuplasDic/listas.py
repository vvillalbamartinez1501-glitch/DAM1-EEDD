colores=[] #Lista vacía
colores=['Rojo', 'Verde', 'Azul']
print("colores:", colores)
print("colores[0]:",colores[0])
colores[0]='Blanco'
print(f"colores: {colores}, colores[0]: {colores[0]}")
colores.append('Amarillo')
print("colores:", colores)

for i in colores:
    print(i)

coloresMin=[ i.lower() for i in colores ]
print(coloresMin)

#color= input("Dime un color...")
color="VERde"
try: 
    
    pos=coloresMin.index(color.lower())
    print(f"{color} está en la lista en la posicion {pos}")
except Exception as e: 
    print(f"{color} no está en la lista")
    
colores.insert(1, "Gris")
print("colores:", colores)

try:
    colores.remove("Grises")
except:
    print(f"El color a borrar no está en la lista")

print("colores:", colores)

del colores[1] #Elimina el elemento en la posición 1 de la lista
print("colores:", colores)

listaNum1= [12, 4, 15, 6, 7, 23, 34, 66, 2, 1, 22]
print("listaNum1:", listaNum1)

listaNum1.sort() #Modifica la lista
print("listaNum1:", listaNum1)

listaNum1.sort(reverse=True)
print("listaNum1:", listaNum1)

listaNum2= [12, 4, 15, 6, 7, 23, 34, 66, 2, 1, 22]
print("listaNum2:", listaNum2)


#sorted es una función (no es un método como sort)
listaNum2Ord= sorted(listaNum2)  #listaNum2 queda si modificar
print("listaNum2:", listaNum2)
print("listaNum2Ord:", listaNum2Ord)

print("Num elementos listaNum1:", len(listaNum1))
listaNum3 = [1, 2] + [3, 4]
print("listaNum3:", listaNum3)

listaNum3.extend([5, 6])
print("listaNum3:", listaNum3)

listaNum3.extend(listaNum3)
print("listaNum3:", listaNum3)

listaNum4= listaNum3[1:6]
print("listaNum4:", listaNum4)

listaNum5Pares= listaNum3[1:len(listaNum3):2]
print("listaNum5Pares:", listaNum5Pares)

# [indice de comienzo::]
print("Rango listaNum3:",listaNum3[:2:])

