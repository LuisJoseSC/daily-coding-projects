def suma (numero_1: int, numero_2: int)-> int:
    return abs(numero_1 + numero_2)
def resta (numero_1: int, numero_2: int) -> int:
    return numero_1 - numero_2
def multiplicacion (numero_1: int, numero_2: int) -> int:
    return numero_1 * numero_2
def division (numero_1: int, numero_2: int):
    
    try:
        return numero_1 / numero_2
    except ZeroDivisionError:
        return None