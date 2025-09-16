from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):
    def __init__(self, codigo: str, titulo: str, anio: int, disponible: bool):
        self._codigo = codigo
        self._titulo = titulo
        self._anio = int(anio)
        self._disponible = disponible
    
    def prestar(self) -> bool:
        if self._disponible == True:
            self._disponible = False
            return True
        return False
    
    def devolver(self) -> None:
        self._disponible = True
    def __str__(self):
        return f"[libro] {self.titulo} ({self._anio} - {self._autor})"
        