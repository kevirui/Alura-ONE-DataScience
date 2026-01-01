# 1- Crea un codigo para imprimir la suma de los elementos de cada una de las listas contenidas en la siguiente lista: 
listaDeListas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
sumaElementos = [sum(lista) for lista in listaDeListas]

# 2- Crea un codigo para generar una lista que almacene el tercer elemento de cada tupla contenida en la siguiente lista de tuplas:
listaDeTuplas = [('Pedro', 1.74, 81), ('Julia', 1.65, 67), ('Otavio', 1.81, 83)]
tercerElemento = [tupla[2] for tupla in listaDeTuplas]

# 3- a partir de la siguiente lista, crea un codigo para generar una lista de tuplas en la que cada tupla tenga el primer elemento como la oposicion del nombre en la lista original y el segundo elemento siendo el propio nombre
lista = ['Pedro', 'Julia', 'Otavio', 'Eduardo']
posicionNombre = [(i+1, nombre) for i, nombre in enumerate(lista)]

# 4- Crea una lista usando al comprension de listas que almacene solo el valor numerico de cada tupla en caso de que el primer elemento sea 'Apartamento', a partir de la siguiente lista de tuplas:
alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
soloAlquiler = [alquiler[1] for alquiler in alquiler if alquiler[0] == 'Apartamento']

# 5- Crea un diccionario usando la comprension de diccionarios en el que las claves esten en la lista meses y los valores esten en gasto
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
mesYgasto = zip(meses, gasto)
gastosMensuales = {mes: valor for mes, valor in mesYgasto}

# 6- Una tienda tiene una base de datos con la informacion de venta de cada representante y de cada año y necesita filtrar solo los datos del año 2022 con ventas mayores a 6000. la tienda proporciono una muestra con solo las columnas de los años y los valores de venta para que puedas ayudar a realizar la filtracion de los datos a traves de un codigo
ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

ventas2022 = [(anio, venta) for anio, venta in ventas if anio == '2022' and venta > 6000]

# 7- Una clinica analiza datos de pacientes y almacena el valor numerico de la glucosa en una base de datos y le gustaria etiquetar los datos de la siguiente manera: Glucosa igual o inferio a 70: 'Hipoglicemia', Glucosa entre 70 y 99: 'Normal', Glucosa entre 100 y 125: 'Alterada', Glucosa superior a 125: 'Diabetes'. La clinica proprciono parte de los valores y tu tarea es crear una lista de tuplas usando la comprension de listas que contenga la etiqueta y el valor de la glucemia en cada tupla
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

glicemiaEtiquetada = [(valor, etiqueta) for valor in glicemia for etiqueta in ['Hipoglicemia' if valor <= 70 else 'Normal' if 70 < valor <= 99 else 'Alterada' if 100 <= valor <= 125 else 'Diabetes' if valor > 125 else None]]

# 8- Un comercio electronico tiene informacion de id de venta, cantidad vendida y precio del producto divididos en las isguientes listas:
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15,12,1,15,2,11,2,12,2,4]
precio = [93.0,102.0,18.0,41.0,122.0,14.0,71.0,48.0,14.0,144.0]

# la plataforma necesita estructura estos datos en una tabla que contenga el valor total de la venta, que se obtiene multiplicando la cantidad por el precio unitario. ademas, la tbla debe contener un encabezado indicando las columasn: 'id', 'cantidad', 'precio', y 'total'
# Crea una lista de tuplas en la que cada tupla tenga id, cantidad, precio, y valor total, siendo la primera tupla el encabezado de la tabla
valorTotalVenta = [(id, cantidad, precio, round(cantidad * precio)) for id, cantidad, precio in zip(id, cantidad, precio)]
print("ID\tCantidad\tPrecio\tTotal")
for id, cantidad, precio, total in valorTotalVenta:
    print(f"{id}\t{cantidad}\t\t{precio}\t{total}")

