import operaciones as op

condicion = True
print("Esta aplicacion solo es capaz de operar con 2 numeros.")
while condicion == True:
    print("Seleccione una opcion:")
    print("1. Suma.")
    print("2. resta.")
    print("3. Multiplicacion.")
    print("4. Division.")
    print("0. salir")
    
    try:
        opcion = int(input("Seleccion: "))
    except ValueError:
        print("No es una opcion valida, ingrese un numero entero.")
        continue
    if opcion == 0:
        condicion = False
        print("Gracias por usar la aplicacion.")
    elif opcion == 1:
        a = int(input("Ingrese el numero 1: "))
        b = int(input("Ingrese el numero 2: "))
        print(op.suma(a,b))
    elif opcion == 2:
        a = int(input("Ingrese el numero 1: "))
        b = int(input("Ingrese el numero 2: "))
        print(op.resta(a,b))
    elif opcion == 3:
        a = int(input("Ingrese el numero 1: "))
        b = int(input("Ingrese el numero 2: "))
        print(op.multiplicacion(a,b))
    elif opcion == 4:
        a = int(input("Ingrese el numero 1: "))
        b = int(input("Ingrese el numero 2: "))
        resultado = op.division(a,b)
        if resultado == None:
            print("No ingrese divisiones por 0, vuelva a intentarlo.")
        else:
            print(resultado)
    else:
        print("¿?")