from abc import ABC, abstractmethod

class Componente(ABC):
    def __init__(self, nombre: str) -> None:
        """Inicializa el componente con un nombre"""
        self.nombre = nombre
        
    @abstractmethod
    def mostrar(self, indentacion: int=0)-> None:
        
        pass

class Pieza(Componente):
    def mostrar(self, indentacion = 0) -> None:
        espacio= " " * indentacion
        print(f"{espacio}- Pieza{self.nombre}")
        
class SubConjunto(Componente):
    def __init__(self, nombre: str)-> None:
        """Inicializa el subconjunto con una lista vacia de componentes."""
        super().__init__(nombre)
        self.componentes: list[Componente]= []
    def agregar(self, componente: Componente)-> None:
        """Agrega un componente al subconjunto"""
        self.componentes.append(componente)
    
    def mostrar(self, indentancion: int=0)-> None:
        espacio=" " * indentancion
        print(f"{espacio} + Sub-conjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(indentancion+4)

def main() -> None:
    """Crea un producto con tres subconjuntos.
    """
    
    producto= SubConjunto("Producto principal")
    
    for i in range (1,4 ):
        subconjunto = SubConjunto(f"Sub-Conjunto {i}")
        for j in range(1,5):
            subconjunto.agregar(Pieza(f"Pieza {i} . {j}"))
        producto.agregar(subconjunto)
    print("ensamblado inicial")
    producto.mostrar()
    
    print("Agragando subconjunto opcional")
    subconjunto_opcional = SubConjunto("Sub-Conjunto Opcional")
    for j in range(1,5):
        subconjunto_opcional.agregar(Pieza(f"Pieza opcional .{j}"))
    producto.agregar(subconjunto_opcional)
    
    print("ensamblado completo")
    producto.mostrar()
    
if __name__ == "__main__":
    main()