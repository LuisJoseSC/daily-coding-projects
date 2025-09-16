class resvista():
    def __init__(self, volumen: int, numero: int):
        self.volumen = int(volumen)
        self.numero = int(numero)
    
    @property
    def volumen(self) -> int:
        return self.volumen
    
    @property
    def numero(self) -> int:
        return self.numero