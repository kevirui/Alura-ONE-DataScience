lista = [2172.54, 3701.35, 3518.09, 3456.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
porcentaje = 0.0

def promedioGastos(lista):
    return sum(lista) / len(lista)

def mayoresA3000(lista):
    mayores = []
    for gasto in lista:
        if gasto > 3000:
            mayores.append(gasto)
            porcentaje = calcularPorcentaje(gasto)
            print(f"Gasto: {gasto} - Porcentaje: {porcentaje:.2f}%")
    print(f"Las compras realizadas por encima de los 3000 reales son: {mayores}")

def calcularPorcentaje(numero):
    return (numero * 100) / sum(lista)

print(f"El total de gastos es: {sum(lista):.2f}")
print(f"El promedio de gastos es: {promedioGastos(lista):.2f}")
mayoresA3000(lista)
