# Ejercicio 3
# Calcular la matriz transpuesta de X

X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta = list(map(lambda *fila: list(fila), *X))

print("Matriz original:")
for fila in X:
    print(fila)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)

# Salida esperada:  

# Matriz original:
# [1, 2, 3]             
# [4, 5, 6]
# [7, 8, 9]                     

# Matriz
# transpuesta:
# [1, 4, 7] 
# [2, 5, 8]
# [3, 6, 9]