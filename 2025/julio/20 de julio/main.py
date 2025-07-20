#20 de julio
#autor: Luis Jose Sanchez Carreño
#Objetivo: Progresar en el aprendizajde de programacion con la ayuda de ChatGPT como profesor.


#1. Warm up (se busca repasar temas pasados para entar en focus)

#1.1 Mini reto: Par/impar con salida temprana

def is_par_impar(my_list):
    """
    Calcula si el numero de una lista es par o impar, esta lista debe contener un solo 0 ccomo minimo.
    Se tiene que recorrer con For.
    Args:
        list (list): list of numbers.
    """
    for number in my_list:
        if number == 0:
            print("0 is not valid input")
            break
        elif number % 2 == 0:
            print("The number: " + str(number) + " is even")
        else:
            print("The number: " + str(number) + " is odd")
            
my_list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,0]
is_par_impar(my_list)