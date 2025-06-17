# herramientas/compresiones_listas.py

# Bucle implícito: elevar al cuadrado
cuadrados = [x**2 for x in range(10)]

# Con condición (solo pares)
pares = [x for x in range(20) if x % 2 == 0]

# Con string (vocales de una palabra)
vocales = [letra for letra in "murciélago" if letra in "aeiou"]

# Genera un diccionari ocon las claves y los valores invertidos
diccionario = {"uno": 1, "dos": 2, "tres": 3}
invertido = {valor: clave for clave, valor in diccionario.items()}

