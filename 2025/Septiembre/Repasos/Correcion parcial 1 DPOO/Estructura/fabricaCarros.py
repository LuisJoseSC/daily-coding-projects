from typing import List, Optional
from carro import Carro
from carroCombustible import CarroCombustible

class FabricaCarros:
    def __init__(self):
        self._marca: Optional[str] = None
        self._pais: Optional[str] = None
        self._carros: List[Carro] = []

    def inicializar(self, marca: str, pais: str) -> None:
        self._marca = marca
        self._pais = pais
        self._carros.clear()

    @property
    def marca(self) -> Optional[str]: return self._marca
    @property
    def pais(self) -> Optional[str]: return self._pais

    def numero_carros(self) -> int:
        return len(self._carros)

    def agregar(self, carro: Carro) -> None:
        if carro is not None:
            self._carros.append(carro)

    def buscar_por_cod_motor(self, cod: str) -> Optional[Carro]:
        for c in self._carros:
            if c.codMotor == cod:
                return c
        return None

    def crear_demo_3_combustible(self) -> None:
        c1 = CarroCombustible("GASOLINA", "M440i Coupé", 2026, "ABC123DEF456GHI789", 3000, 250_000_000, 60, 10)
        c2 = CarroCombustible("DIESEL",   "X5",            2025, "ZZZ111YYY222XXX333", 3000, 380_000_000, 70,  0)
        c3 = CarroCombustible("GASOLINA", "Serie 3",       2024, "MTR999QWE888RTY777", 2000, 180_000_000, 55, 20)
        self.agregar(c1); self.agregar(c2); self.agregar(c3)

    def consultar_info(self, codMotor: str) -> str:
        carro = self.buscar_por_cod_motor(codMotor)
        if carro is None:
            raise ValueError(f"No existe un carro con motor: {codMotor}")
        return str(carro)

    def consultar_precio_total(self, codMotor: str) -> float:
        carro = self.buscar_por_cod_motor(codMotor)
        if carro is None:
            raise ValueError(f"No existe un carro con motor: {codMotor}")
        return carro.precio_total()
