# Ejercicio 1
# Ordenar lista de diccionarios por una clave indicada

autos = [
    {'brand': 'Toyota', 'model': 'Corolla', 'year': 2018},
    {'brand': 'Honda', 'model': 'Civic', 'year': 2020},
    {'brand': 'Ford', 'model': 'Focus', 'year': 2016},
    {'brand': 'Mazda', 'model': '3', 'year': 2019}
]

clave = 'year'

ordenados = sorted(autos, key=lambda x: x[clave])

print("Lista ordenada por", clave)
for a in ordenados:
    print(a)
# Salida esperada si clave = 'model':
# Lista ordenada por model