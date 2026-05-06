from abc import ABC, abstractmethod

class TrenLaminador(ABC):
    """Interfaz cde implementacion para los trenes laminadores"""
    
    @abstractmethod
    def producir(self)-> str: #metodo que cada tren concreto debe implementar
        pass

class Tren5m(TrenLaminador):
    """Tren que produce planchas de 5 metros"""
    def producir(self)-> str:
        return "Plancha de 5 metros"
    
class Tren10m(TrenLaminador):
    """Tren que produce planchas de 10 metros"""
    def producir(self):
        return "Plancha de 10 metros"
    
class Lamina:
    """Abstraccion principal.
    representa una lamina de acero generica a la que se le asigna un tren que define el largo"""
    
    def __init__(self, tren: TrenLaminador) -> None: #inicializa la lamina con un laminador especifico
        self.tren= tren
        
    def producir(self)-> str: #produce la lamina usando el tren asignado.
        return f"Lamina de acero (0.5'' x 1.5M): {self.tren.producir()}"
    
def main()-> None:
    
    tren_corto=Tren5m()
    tren_largo=Tren10m()
    
    print("Generando tren de 5 metros")
    lamina1= Lamina(tren_corto)
    print(lamina1.producir())
    
    print("Generando tren de 10 metros")
    lamina2 =Lamina(tren_largo)
    print(lamina2.producir())
    
if __name__ == "__main__":
    main()