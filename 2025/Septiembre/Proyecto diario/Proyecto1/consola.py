from operaciones import Calculadora
calculadora = Calculadora()
condicion = True
print("Esta aplicacion solo es capaz de operar con 2 numeros.")
while condicion == True:
    print("Seleccione una opcion:")
    print("1. Suma.")
    print("2. resta.")
    print("3. Multiplicacion.")
    print("4. Division.")
    print("5. Potencia.")
    print("6. Modulo.")
    print("0. salir")
    
    try:
        opcion = int(input("Seleccion: "))
    except ValueError:
        print("No es una opcion valida, ingrese un numero entero.")
        continue
    if opcion == 0:
        condicion = False
        print("Gracias por usar la aplicacion.")
    elif opcion in [1,2,3,4,5,6,7,8]:
        a = int(input("Ingrese el numero 1: "))
        b = int(input("Ingrese el numero 2: "))
        if opcion == 1:
            print("Resultado: ", calculadora.sumar(a,b))
        elif opcion == 2:
            print("Resultado: ", calculadora.restar(a,b))
        elif opcion == 3:
            print("Resultado: ", calculadora.multiplicar(a,b))
        elif opcion == 4:
            print(f"Resultado: {calculadora.dividir(a,b)}")
        elif opcion == 5:
            print(f"Resultado: {calculadora.potencia(a,b)}")
        elif opcion == 6:
            print(f"Resultado: {calculadora.modulo(a,b)}")