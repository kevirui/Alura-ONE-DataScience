import numpy as py 

nombreUsuario = input("Ingrese o seu nome de usuario: ")

def generarToken():
    token = py.random.randint(1000, 9998)
    if token % 2 == 0:
        return token
    else:
        return token + 1

print(f"Hola, {nombreUsuario}, tu token de acceso es: {generarToken()} ¡Bem-vindo!")
