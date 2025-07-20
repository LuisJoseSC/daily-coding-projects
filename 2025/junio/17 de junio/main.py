# ---------------------------------------------
#   DAILY CODING JOURNEY
#   Autor: Luis José
#   Lenguaje: Python
#   Fecha: 2025-06-17
#   Día: 1 - Tema: Bucles
#   Descripción:
#       Exploración práctica de estructuras de control (while, for).
#
#   Parte del reto diario de maestría en programación.
#   Repositorio: github.com/luisJoseSC/daily_coding_projects
# ---------------------------------------------

#Ejercicio 1
i = 1
while i<11:
    #print(i)
    i += 1

#Ejercicio 2
i = 10
while i>0:
    #print(i)
    i -= 1

#Ejercicio 3
i = 0

while i < 21:
    #if i%2 == 0:
        #print(i)
    i += 1

#Ejercico 4
i = 0
suma = 0
while i < 101:
    suma += i
    i += 1
#print("la suma total es: ", suma)

#for
#Ejercico 5

#for i in range(1,11):
    #print(i)
    
#Ejercicio 6
frutas = ["manzana", "pera", "naranja", "limon", "durazno"]
#print("lista de frutas: ")
for fruta in frutas:
    i = i
    #print(fruta)

#Ejercico 7
palabra = "codigo"
for letra in palabra:
    s = 1
    #print("letra: ", letra)
    
#Nuevos metodos
#Ejercico 8
for i in range(1,11):
    if i == 5:
        break
    #print(i)

#Ejercico 9
for i in range(1,11):
    if i % 3 == 0:
        continue
    #print(i)
    
#Ejercico 10
lista = [3,8,1,4,9]
num  = 7
for i in lista:
    if num == i:
        #print("el numero fue encontrado")
        break
else:
    s = 1
    #rint("el numero no fue encontrado")


#Ejercico final bucles
numero = 6
intentos = 5

while intentos > 0:
    
    num = int(input("Escribe el numero: "))
    if num == numero:
        print("Correcto")
        break
    if num > 20 or num < 1:
        print("Número fuera de rango, intenta de nuevo.")
        continue
    elif num != numero:
        intentos -= 1
        print("incorrecto, intentos restantes: ", intentos)
else:
    print("No lo lograste, el numero era: ", numero)