"""
class Carro(ABC):
    IVA = 0.19
    matricula = 2_000_000
    
    def __init__(self,
                tipoGenerico: str,
                tipoEspecifico: str,
                linea: str,
                modelo: int,
                codMotor: str,
                cilindraje: int,
                precioBase: float,
                capacidadMaxEnergia: float,
                energiaAcutalInicial: float):
        self.tipoGenerico = tipoGenerico
        self.tipoEspecifico = tipoEspecifico
        self.linea = linea
        self.modelo = modelo
        self.codMotor = codMotor
        self.cilindraje = cilindraje
        self.precioBase = float(precioBase)
        self.capacidadMaxEnergia = float(capacidadMaxEnergia)
        self.energiaActual =  max(0.0, min(float(energiaAcutalInicial), self.capacidadMaxEnergia))
        
        @property
        def tipo_generico(self):
            return self.tipo_generico
        @property
        def tipo_especifico(self):
            return self.tipo_especifico
        @property
        def linea(self):
            return self.linea
        @property
        def modelo(self):
            return self.modelo
        @property
        def cod_motor(self):
            return self.cod_motor
        @property
        def cilindraje(self):
            return self.cilindraje
        @property
        def precio_base(self):
            return self.precio_base
        @property
        def capacidad_max_energia(self):
            return self.capacidad_max_energia
        @property
        def energia_actual(self):
            return self.energia_actual
        def set_energia_actual(self, nueva: float):
            self.energia_actual = max(0.0, min(float(nueva), self.capacidadMaxEnergia))
            
        @abstractmethod
        def impuesto_especifico(self, nueva: float):
            self.energiaActual = max(0.0, min(float(nueva), self.capacidadMaxEnergia))
            return NotImplementedError
        
        #logica comun:
        def precio_total(self):
            return self.precio_base * (1 + Carro.IVA + Carro.matricula + self.impuesto_especifico()) + self.matricula
        
        def __str__(self) -> str:
            return f"{self._tipoGenerico}:{self._linea}-{self._modelo}-{self._codMotor}"
            
"""

from abc import ABC, abstractmethod

class Carro(ABC):
    IVA = 0.19
    matricula = 2_000_000
    
    def __init__(self,
                tipo_generico: str,
                tipo_especifico: str,
                linea: str,
                modelo: int,
                cod_motor: str,
                cilindraje: int,
                precio_base: float,
                capacidad_max_energia: float,
                energia_actual: float):
        self._tipo_generico = tipo_generico
        self._tipo_especifico = tipo_especifico
        self._linea = linea
        self._modelo = modelo
        self._cod_motor = cod_motor
        self._cilindraje = cilindraje
        self._precio_base = float(precio_base)
        self._capacidad_max_energia = float(capacidad_max_energia)
        self._energia_actual =  max(0.0, min(float(energia_actual), self.capacidad_max_energia))
        
        @property
        
        def tipo_generico(self):
            return self._tipo_generico
        @property
        def tipo_especifico(self):
            return self._tipo_especifico 
        @property  
        def linea(self):
            return self._linea
        @property
        def modelo(self):
            return self._modelo
        @property
        def cod_motor(self):
            return self._cod_motor
        @property
        def cilindraje(self):
            return self._cilindraje
        @property
        def precio_base(self):
            return self._precio_base
        @property
        def capacidad_max_energia(self):
            return self._capacidad_max_energia
        
        def energia_actual(self):
            return self._energia_actual
        def _set_energia_actual(self, nueva: float):
            self.energia_actual = max(0.0, min(float(nueva), self.capacidad_max_energia))
        
        @abstractmethod
        def impuesto_especifico(self) -> float:
            return NotImplementedError