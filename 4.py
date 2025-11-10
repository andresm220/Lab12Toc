# Ejercicio 4
# Eliminar elementos de una lista usando lambda

colores = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
a_eliminar = ['amarillo', 'café', 'blanco']

filtrados = list(filter(lambda c: c not in a_eliminar, colores))

print("Lista original:", colores)
print("Elementos a eliminar:", a_eliminar)
print("Resultado:", filtrados)

                                                        