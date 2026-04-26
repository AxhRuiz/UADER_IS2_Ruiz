"""3. Genere una clase donde se instancie una comida rápida “hamburguesa” que
pueda ser entregada en mostrador, retirada por el cliente o enviada por
delivery. A los efectos prácticos bastará que la clase imprima el método de
entrega"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Hamburguesa:
    
    def __init__(self) -> None:
        self.metodoEntrega= ""
        
    def definir_entrega(self, metodo:str)-> None:
        self.metodoEntrega = metodo
        
    def mostrar(self)-> str:
        return (f"el metodo de entrega seleccionado es: {self.metodoEntrega}")
    
class BuilderMetodoEntrega(ABC):
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self._producto = Hamburguesa()
    
    def obtener_resultado(self) -> Hamburguesa:
        producto = self._producto
        self.reset()
        return producto
    
    @abstractmethod
    def definir_entrega(self)-> None:
        pass

class BuilderMostrador(BuilderMetodoEntrega):
    def definir_entrega(self):
        self._producto.definir_entrega("Mostrador")

class BuilderRetiro(BuilderMetodoEntrega):
    def definir_entrega(self):
        self._producto.definir_entrega("Retiro")
        
class BuilderDelivery(BuilderMetodoEntrega):
    def definir_entrega(self):
        self._producto.definir_entrega("Delivery")

class Director:
    def __init__(self, builder: BuilderMetodoEntrega) -> None:
        self._builder= builder
        
    def construir_hamburguesa(self) -> None:
        self._builder.definir_entrega()
        
def main()-> None:
    
    builder= BuilderDelivery()
    directorDeli = Director(builder)
    directorDeli.construir_hamburguesa()
    hambur= builder.obtener_resultado()
    print(hambur.mostrar())
    
    builder= BuilderRetiro()
    directorReti= Director(builder)
    directorReti.construir_hamburguesa()
    hambur= builder.obtener_resultado()
    print(hambur.mostrar())
    
    
    builder= BuilderMostrador()
    directorMost= Director(builder)
    directorMost.construir_hamburguesa()
    hambur= builder.obtener_resultado()
    print(hambur.mostrar())

if __name__ == "__main__":
    main()