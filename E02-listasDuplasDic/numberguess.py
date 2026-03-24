import random

numeroAAdivinar = random.randint(1,100)

numeroIntroducido = 0
while numeroAAdivinar != numeroIntroducido:
    numeroIntroducido = int(input("Introduce tu número:"))
    if numeroIntroducido > numeroAAdivinar:
        print("Más bajo")
    elif numeroAAdivinar > numeroIntroducido:
        print("Más alto")
print("Número adivinado")
