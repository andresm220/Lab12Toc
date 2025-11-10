# Ejercicio 2
# Calcular la potencia n-ésima de cada elemento de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3  # potencia a aplicar

potencias = list(map(lambda x: x ** n, numeros))

print(f"Potencia {n} de cada número: {potencias}")
# Salida esperada:
# Potencia 3 de cada número: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

