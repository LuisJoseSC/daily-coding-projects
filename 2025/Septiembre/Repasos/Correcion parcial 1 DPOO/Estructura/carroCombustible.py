"""
# fabrica/carro_combustible.py
from carro import Carro

class CarroCombustible(Carro):
    TIPO = "COMBUSTIBLE"
    IMPUESTO_ESPECIFICO = 0.08

    def __init__(self,
                tipoEspecifico: str,
                linea: str,
                modelo: int,
                codMotor: str,
                cilindraje: int,
                precio_base: float,
                capacidadMaxEnergia: float,
                energiaActualInicial: float):
        super().__init__(self.TIPO, tipoEspecifico, linea, modelo, codMotor,
                        cilindraje, precio_base, capacidadMaxEnergia, energiaActualInicial)

    def impuesto_especifico(self) -> float:
        return self.IMPUESTO_ESPECIFICO

    def recargar_energia(self, cantidad: float) -> None:
        if cantidad is None or cantidad <= 0:
            return
        self._set_energia_actual(self.energia_actual + cantidad)
"""
