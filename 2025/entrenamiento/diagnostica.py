def edad(edad)->str:
    
    if edad < 18:
        return "eres menor de edad"
    elif 18 <= edad < 65:
        return "eres mayor de edad"
    else:
        return "eres adulto mayor"


def clasificar_numero(n: int) -> str:
    """
    Retorna si el número es positivo, negativo o cero.
    """
    if n >0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"


def es_par(n: int) -> bool:
    """
    Devuelve True si el número es par, False si es impar.
    """
    return n % 2 == 0

def es_bisiesto(anio: int) -> bool:
    """
    Un año es bisiesto si es divisible por 4 y (no divisible por 100 o sí divisible por 400).
    """
    return (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0)


def convertir_a_celsius(fahrenheit: float) -> float:
    """
    Convierte una temperatura de Fahrenheit a Celsius.
    """
    
    return (fahrenheit - 32) * (5/9)


def area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo usando la fórmula: (base * altura) / 2
    """
    return (base + altura)/2

def contar_vocales(cadena: str) -> int:
    """
    Cuenta cuántas vocales hay en una cadena de texto (sin importar mayúsculas).
    """
    cadena = cadena.lower()
    vocales = [letra for letra in cadena if letra in "aeiou"]
    return len(vocales)

def obtener_pares(lista: list[int]) -> list[int]:
    """
    Retorna una nueva lista con solo los números pares de la lista dada.
    """
    return [numero for numero in lista if numero % 2 == 0]


def invertir_diccionario(diccionario: dict) -> dict:
    """
    Retorna un nuevo diccionario invirtiendo claves y valores del original.
    """
    return {valor: clave for clave, valor in diccionario.items()}

def es_palindromo(cadena: str) -> bool:
    """
    Verifica si una cadena es un palíndromo (se lee igual al derecho y al revés).
    Ignora mayúsculas y espacios.
    """
    pass

def analizar_temperaturas(temperaturas: list[float]) -> dict:
    """
    Retorna un diccionario con:
    - 'promedio': promedio de las temperaturas
    - 'max': temperatura máxima
    - 'min': temperatura mínima
    - 'dias_frios': cuántos días estuvieron por debajo de 18°C
    """
    pass

