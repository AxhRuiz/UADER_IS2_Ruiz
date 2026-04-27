"""5. Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar
para construir aviones en lugar de vehículos. Para simplificar suponga que un
avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Avion:
    def __init__(self) -> None:
        self.componentes= []
        
    def agregar(self, componente: str)-> None:
        self.componentes.append(componente)
    
    def mostrar(self)-> str:
        return "Generando Avion... \n - " + "\n - ".join(self.componentes)
    
class BuilderAvion(ABC):
    def __init__(self)-> None:
        self.reset()
    
    def reset(self) -> None:
        self._producto = Avion()
        
    def obtener_resultado(self) -> Avion:
        producto = self._producto
        self.reset()
        return producto
    
    @abstractmethod
    def construir_turbina(self) -> None:
        pass
    
    @abstractmethod
    def construir_alas(self) -> None:
        pass
    
    @abstractmethod
    def construir_tren_aterrizaje(self) -> None:
        pass
    
    @abstractmethod
    def construir_body(self) -> None:
        pass

class Builder_Avion(BuilderAvion):
    def construir_turbina(self):
        self._producto.agregar("Agregando 2 Turbinas")
    
    def construir_alas(self):
        self._producto.agregar("Agregando 2 Alas")
        
    def construir_tren_aterrizaje(self):
        self._producto.agregar("Agregando tren de aterrizaje")
        
    def construir_body(self):
        self._producto.agregar("Agregando body")
        

        
class Director:
    def __init__(self, builder: BuilderAvion)-> None:
        self._builder =builder
        
    def construir_avion(self) -> None:
        self._builder.construir_alas()
        self._builder.construir_body()
        self._builder.construir_tren_aterrizaje()
        self._builder.construir_turbina()
    
    
def main()-> None:
    builder= Builder_Avion()
    director = Director(builder)
    
    director.construir_avion()
    avionUno= builder.obtener_resultado()
    print(avionUno.mostrar())
    
if __name__ == "__main__":
    main()