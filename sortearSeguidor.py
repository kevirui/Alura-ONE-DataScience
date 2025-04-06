import numpy as py

numeroParticipantes = int(input("Quantos participantes tem? "))
numeroSorteado = py.random.randint(1, numeroParticipantes)

print("Sorteando um numero entre 1 e", numeroParticipantes)
print("O numero sorteado foi:", numeroSorteado)


