class Calculadora():
    def __init__(self):
        self.historial = []
    
    def sumar(self, a , b):
        resultado = a + b
        self.historial.append(f"Suma: {a} + {b} = {resultado}")
        return resultado
    
    def restar (self, a, b):
        resultado = a - b
        self.historial.append(f"Resta: {a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a , b):
        resultado = a * b
        self.historial.append(f"Multiplicacion: {a} * {b} = {resultado}")
        return resultado
    
    def dividir(self, a , b):
        if b == 0:
            return None
        resultado = a / b
        self.historial.append(f"Division: {a} / {b} = {resultado}")
        return resultado
    
    def potencia(self, a , b):
        if b < 0:
            return f"No se existen potencias negativas en la recta real"
        elif b == 0:
            resultado = 1
            self.historial.append(f"Potencia: {a} ** {b} = {resultado}")
            return resultado
        else:
            resultado = a ** b
            self.historial.append(f"Potencia: {a} ** {b} = {resultado}")
            return resultado
        
    def modulo(self, a , b):
        if b == 0:
            return None
        else:
            resultado = a % b
            self.historial.append(f"Modulo: {a} % {b} = {resultado}")
            return resultado
    def graficas(self, archivo):
        pass
        