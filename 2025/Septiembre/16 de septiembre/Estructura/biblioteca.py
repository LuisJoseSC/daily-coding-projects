from abc import ABC, abstractmethod

class Biblioteca(ABC):
    def __init__(self,
                nombre: str,
                ciudad: str
                ):
        self._nombre = nombre
        self._ciudad = ciudad
        self._items = []
        
    def agregar_item(self, item):
        self._items.append(item)
    def buscar_por_codigo(self, codigo: str):
        for libro in self._items:
            if libro == codigo:
                return libro
            else:
                return "No se encontro ninguna coincidencia con el codio ingresado"            
    