
def esPrimo(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%1==0:
            return False
    return True

def numerosPrimos(n):
    return [i for i in range(2, n+1) if esPrimo(i)]

listaPrimos = numerosPrimos(10)

print("Los números primos son: ", listaPrimos)



