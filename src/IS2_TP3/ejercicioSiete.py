""""7. Imagine una situación donde pueda ser de utilidad el patrón “abstract factory”"""

from abc import ABC, abstractmethod

#Productos Abstractos!
class Hamburguesa(ABC):
    
    @abstractmethod
    def descripcion(self) -> str:
        pass

class Guarnicion(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass

class Bebida(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass

#Productos Concretos - Hamburguesas
class HamburguesaCarne(Hamburguesa):
    def descripcion(self) -> str:
        return ("Hamburguesa de carne")
    
class HamburguesaSoja(Hamburguesa):
    def descripcion(self)-> str:
        return ("Hamburguesa de soja")
    
class HamburguersaDobleCarne(Hamburguesa):
    def descripcion(self)->str:
        return("Doble hamburguesa de carne")
    
#Productos concetros - Guarniciones
    
class PapasFritas(Guarnicion):
    def descripcion(self)-> str:
        return ("Papas fritas")

class Ensalada(Guarnicion):
    def descripcion(self)-> str:
        return ("Ensalada fresca")
    
class DoblePapasFritas(Guarnicion):
    def descripcion(self)->str:
        return("Doble porcion de papas fritas")
    
#Productos concretos - Bebidas
    
class Gaseosa(Bebida):
    def descripcion(self) -> str:
        return "Gaseosa"

class Agua(Bebida):
    def descripcion(self) -> str:
        return "Agua mineral"

class GaseosaGrande(Bebida):
    def descripcion(self) -> str:
        return "Gaseosa grande"

#Fabrica Abstracta    
class ComboFactory(ABC):#Fabrica Abstracta para crear combos de comida
    #define la interfaz para crear familias de productos relacionados.
    @abstractmethod
    def crear_hamburguesa(self)-> Hamburguesa:
        pass
    
    @abstractmethod
    def crear_guarnicion(self)-> Guarnicion:
        pass
    
    @abstractmethod
    def crear_bebida(self) -> Bebida:
        pass
    
#FABRICA 1
class ComboClasicoFactory(ComboFactory): #Fabrica concreta para el combo clasico
    #produce: hamburuesa de carne, papas fritas, gaseosa
    def crear_hamburguesa(self) -> Hamburguesa:
        return HamburguesaCarne()
    
    def crear_guarnicion(self)-> Guarnicion:
        return PapasFritas()
    
    def crear_bebida(self)-> Bebida:
        return Gaseosa()
    
#FABRICA 2
class ComboVeganoFactory(ComboFactory):#Fabrica concreta para el combo vegano
    #Produce: Hamburguesa de soja, ensalada fresca, agua mineral
    def crear_hamburguesa(self) -> Hamburguesa:
        return HamburguesaSoja()
    
    def crear_guarnicion(self)-> Guarnicion:
        return Ensalada()
    
    def crear_bebida(self)-> Bebida:
        return Agua()

#FABRICA 3    
class ComboExtraGrandeFactory(ComboFactory):# Fabrica concreta para el combo extra grande
    #produce: Doble hamburguesa de carne, doble papas fritas, gaseosa grande
    def crear_hamburguesa(self)-> Hamburguesa:
        return HamburguersaDobleCarne()
    
    def crear_guarnicion(self)-> Guarnicion:
        return DoblePapasFritas()
    
    def crear_bebida(self)-> Bebida:
        return GaseosaGrande()
    
    
def mostrar_combo(factory: ComboFactory, nombre: str) -> None:
    
    hamburguesa = factory.crear_hamburguesa()
    guarnicion = factory.crear_guarnicion()
    bebida = factory.crear_bebida()
    
    print(f"\n--- {nombre} ---")
    print(f"{hamburguesa.descripcion()}")
    print(f"{guarnicion.descripcion()}")
    print(f"{bebida.descripcion()}")

def main() -> None: 
    
    mostrar_combo(ComboClasicoFactory(), "Combo Clásico")
    
    
    mostrar_combo(ComboVeganoFactory(), "Combo Vegano")
    
    
    mostrar_combo(ComboExtraGrandeFactory(), "Combo Extra Grande")

if __name__ == "__main__":
    main()