from itemBiblioteca import ItemBiblioteca
from libro import Libro
from revista import Revista
from typing import List
class Biblioteca:
    def __init__(self, nombre: str, ciudad: str):
        self._nombre = nombre
        self._ciudad = ciudad
        self._items: List[ItemBiblioteca] = []
        
    def agregar_item(self, item: ItemBiblioteca):
        self._items.append(item)
        
    def buscar_codigo(self, codigo: str):
        for item in self._items:
            if item.codigo == codigo:
                return item
        return None
    
    def prestar_item(self, codigo: str) -> bool:
        
        item = self.buscar_por_codigo(codigo)
        if item is None:
            return False
        return item.prestar()
    
    def devolver_item(self, codigo) -> None:
        
        item = self.buscar_por_codigo(codigo)
        if item is not None:
            item.devolver()
            
    def listar_disponibles(self) -> List[ItemBiblioteca]:
        return [item for item in self._items if item.disponible]
    