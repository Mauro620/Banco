import numpy as np

# Paso 1: Asignar números a las letras y caracteres
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
asignacion = {letra: i + 1 for i, letra in enumerate(alfabeto)}

# Paso 2: Recibir un mensaje y crear la matriz A
mensaje = input("Ingrese un mensaje: ")
mensaje = mensaje.upper()  # Convertir a mayúsculas
mensaje = mensaje.replace(".", "").replace(",", "")  # Eliminar puntos y comas

while len(mensaje) % 3 != 0:
    mensaje += " "  # Agregar espacios para que sea divisible por 3

n = len(mensaje)
A = np.zeros((n // 3, 3), dtype=int)

for i in range(n):
    fila = i // 3
    columna = i % 3
    A[fila][columna] = asignacion.get(mensaje[i], 0)

# Mostrar la matriz A
print("Matriz A:")
print(A)

# Paso 3: Crear una matriz fija B de 3x3 con valores aleatorios entre 1 y 5
# B = np.random.randint(1, 6, (3, 3))
B = [[1, -1, 2], [5, 2, 3], [-2, -1, 1]]

# Mostrar la matriz B
print("\nMatriz B:")
print(B)

# Paso 4: Multiplicar A por B para obtener C
C = np.dot(A, B)

# Mostrar la matriz C
print("\nMatriz C (Resultado de A * B):")
print(C)

# Paso 5: Obtener la matriz inversa de B y multiplicarla por C
try:
    D = np.linalg.inv(B)
    final = np.dot(C, D)
    final = np.round(final).astype(int)

    # Mostrar la matriz D
    print("\nMatriz D (Inversa de B):")
    print(D)

    # Mostrar la matriz final
    print("\nMatriz final (Resultado de C * D):")
    print(final)
except np.linalg.LinAlgError:
    print("\nLa matriz B no es invertible.")

# Paso 6: Convertir la matriz resultante en un mensaje
mensaje_final = ""
for fila in final:
    for valor in fila:
        letra = [k for k, v in asignacion.items() if v == valor][0]
        mensaje_final += letra

# Paso 7: Mostrar el mensaje final
print("\nMensaje final:")
print(mensaje_final)
