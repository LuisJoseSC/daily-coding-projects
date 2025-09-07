""" 
Septiembre 7 de 2025, dia de programacion y avance propio.
temas a repasar: 
    - metodos
    - POO
    - clases
    - herencia
    - encapsulacion
    - modulos
Todo esto en python 3.8.5.
"""

""" 
Ejercicio 1: (puesto por ChatGPT).

Haz un programa que:

Pida un número al usuario.

Intente convertirlo a entero con int().

Si el usuario mete algo inválido (ej: “perro”), que capture el error y muestre un mensaje.

Use else para imprimir el número válido si no hubo error.

Use finally para imprimir "Fin del programa" siempre.
"""

"""
numero = input("Ingrese un numero: (si pone algo diferente su papa no lo quiere, esta avisado pirobo)")
    
try:
    numero = int(numero)
except ValueError:
    print("Error: El dato ingresado no es un numero.")
else:
    print("El numero ingresado es valido. Su numero es:", numero)
finally:
    print("Fin del programa.")
"""
""" 
Ejercicio 2: (puesto por ChatGPT).

Crea un programa que:

Use un while True para pedir números al usuario.

Si el usuario escribe "salir", usa break para terminar el bucle.

Si mete algo que no sea un número, captura el error con try/except y muestra un mensaje.

Si mete un número válido, imprímelo al cuadrado (n ** 2).

Al salir, usa finally para mostrar "Programa finalizado".
"""
"""
while True:
    numero = input("Ingrese un numero: ")
    if numero == "salir":
        break
    try:
        numero = int(numero)
    except ValueError:
        print("Error: El dato ingresado no corresponde a un numero.")
    else:
        print(numero ** 2)
    finally:
        print("Programa finalizado.")
"""
# Programacion orientada a objetos (POO)

""" 
Ejercicio 3: (puesto por ChatGPT).

Crea una clase Estudiante con:

Atributos: nombre, edad, materias (lista), notas (lista).

Método mostrar_materias() que use enumerate para listar materias con índice.

Método promedio() que use sum y len para calcular el promedio de notas.

Método materias_con_notas() que use zip para mostrar pares (materia, nota).

Método mejores_notas() que use sorted para ordenar notas de mayor a menor.
"""

class Estudiante:
    def __init__ (self, nombre, edad, materias, notas):
        self.nombre = nombre
        self.edad = edad
        self.materias = materias
        self.notas = notas
    
    def mostrar_materias(self):
        for indice, materia in enumerate(self.materias):
            print (f"Materia {indice + 1}: {materia}")
    def promedio(self):
        return sum(self.notas) / len(self.notas)
    def materias_con_notas(self):
        return zip(self.materias, self.notas)
    def mejores_notas(self):
        return sorted(self.notas, reverse=True)