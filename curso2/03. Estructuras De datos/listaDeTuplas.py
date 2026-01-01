from random import randint
nombres = ['Juan', 'Maria', 'Claudia', 'Ana']

def generaNumero():
    return randint(0, 999)

generaNumero()

codigoEstudiantes = []

for i in range(len(nombres)):
    codigoEstudiantes.append((nombres[i], nombres[i][0]+str(generaNumero())))


print(codigoEstudiantes)


