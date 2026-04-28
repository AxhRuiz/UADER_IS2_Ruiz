"""5. Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar
para construir aviones en lugar de vehículos. Para simplificar suponga que un
avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Avion: #productgo complejo que se construye paso a paso.
    #Representa un avion con sus componentes estructurales
    def __init__(self) -> None:
        self.componentes= [] #componentes: lista de componentes agregados al avion
        
    def agregar(self, componente: str)-> None: #agrega un componente al avion
        self.componentes.append(componente)
    
    def mostrar(self)-> str: #muestra la configuracion completa del avion
        return "Generando Avion... \n - " + "\n - ".join(self.componentes)
    
class BuilderAvion(ABC):
    def __init__(self)-> None: #inicializa el builder con un producto vacio
        self.reset()
    
    def reset(self) -> None: #reinicia el builder creando un nuevo avion
        self._producto = Avion()
        
    def obtener_resultado(self) -> Avion: #retorna el producto terminado y reinicia el bulder
        producto = self._producto
        self.reset()
        return producto
    
    @abstractmethod
    def construir_turbina(self) -> None: #constuye las turbinas del avion
        pass
    
    @abstractmethod
    def construir_alas(self) -> None: #construye las alas del avion
        pass
    
    @abstractmethod
    def construir_tren_aterrizaje(self) -> None: #construye el tren de aterrizaje del avion
        pass
    
    @abstractmethod
    def construir_body(self) -> None: #construye el body del avion
        pass

class Builder_Avion(BuilderAvion): #builder concreto para un avion estandar
    #implementa cada paso de construccion agregando los componentes especificos al producto
    def construir_turbina(self): #agrega 2 turbian al avion
        self._producto.agregar("Agregando 2 Turbinas")
    
    def construir_alas(self): #agrega 2 alas al avion
        self._producto.agregar("Agregando 2 Alas")
        
    def construir_tren_aterrizaje(self): #agrega tren de aterrizaje al avion 
        self._producto.agregar("Agregando tren de aterrizaje")
        
    def construir_body(self): #agrega body al avion
        self._producto.agregar("Agregando body")
        

        
class Director: #director que orquesta la construccion del avion
    #define el orden en que se ejecutan los pasos de contruccion
    
    def __init__(self, builder: BuilderAvion)-> None: #inicializa el director con un builder especifico
        self._builder =builder
        
    def construir_avion(self) -> None: #ejecuta los pasos para construir el avion
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