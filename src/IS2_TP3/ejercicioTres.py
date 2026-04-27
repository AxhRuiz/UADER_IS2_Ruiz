"""3. Genere una clase donde se instancie una comida rápida “hamburguesa” que
pueda ser entregada en mostrador, retirada por el cliente o enviada por
delivery. A los efectos prácticos bastará que la clase imprima el método de
entrega"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Hamburguesa: #Producto construido por el bulder.
        #Representa una hamburguesa con un metodo de entrega configurable.
    
    def __init__(self) -> None: #Inicializa la hamburguesa sin metodo de entrega definido
        self.metodoEntrega= ""
        
    def definir_entrega(self, metodo:str)-> None: #Asigna el metodo de entrega a la hamburguesa
        self.metodoEntrega = metodo #metodo peude ser: ('Mostrador', 'Retiro', 'Delivery')
        
    def mostrar(self)-> str: #retorna la descripcion del metodo de entrega
        return (f"el metodo de entrega seleccionado es: {self.metodoEntrega}")
    
class BuilderMetodoEntrega(ABC): #Builder Abstracto para la constuccion de Hamburguesa
    #Define la interfaz para constuir una hamburguesa, permitiendo variar el metodo de entrega
    def __init__(self) -> None: #Inicializa el builder con un productgo vacio
        self.reset()
        
    def reset(self) -> None: #Reinicia el builder creando una nueva hamburguesa
        self._producto = Hamburguesa()
    
    def obtener_resultado(self) -> Hamburguesa: #retorna el producto terminado y reinicia el builder
        producto = self._producto
        self.reset()
        return producto #Hamburguesa comletamente construida
    
    @abstractmethod
    def definir_entrega(self)-> None: #define el metodo de entrega de la hamburguesa
        pass 

class BuilderMostrador(BuilderMetodoEntrega):#Builder concrteto para hamburguesa mostrador
    def definir_entrega(self):
        self._producto.definir_entrega("Mostrador")

class BuilderRetiro(BuilderMetodoEntrega): #Builder concreto para hamburguesa retirada por cliente
    def definir_entrega(self):
        self._producto.definir_entrega("Retiro")
        
class BuilderDelivery(BuilderMetodoEntrega): #Builder concreto para hamburguesa enviada por delivery
    def definir_entrega(self):
        self._producto.definir_entrega("Delivery")

class Director:  #Director que define la construccion de la hamburguesa
    
    def __init__(self, builder: BuilderMetodoEntrega) -> None: #Inicializa el director con un builder especifico
        self._builder= builder
        
    def construir_hamburguesa(self) -> None: #Ejecuta los pasos necesarios para construir la hamburguesa
        self._builder.definir_entrega()
        
def main()-> None: #Demostracion del builder aplicado a una hambursa
        #Construye y muestra tres hamburguesas con diferentes metodos de entrega.
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