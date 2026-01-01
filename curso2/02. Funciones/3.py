lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# 3. Crear una nueva lista con los elementos que son multiplos de 3
nuevaLista = map(lambda x: x if x%3 == 0 else None, lista)
print(nuevaLista)
