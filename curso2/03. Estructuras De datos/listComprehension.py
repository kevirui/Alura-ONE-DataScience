def promedio(lista: list=[0]) ->float:
    """
    Calcula el promedio de una lista de números.
    
    :param lista: Lista de números.
    :return: Promedio de los números en la lista.
    """
    return sum(lista) / len(lista) if lista else 0

notas = [[8, 9, 10], [9, 7, 6], [10, 10, 9], [8, 8, 9]]
promedios = [round(promedio(nota), 1) for nota in notas]

nombres = ['Juan', 'Maria', 'Claudia', 'Ana']

estudiantes = list(zip(nombres, promedios))

candidatos = [estudiante[0] for estudiante in estudiantes if estudiante[1] >= 8]

print(candidatos)
