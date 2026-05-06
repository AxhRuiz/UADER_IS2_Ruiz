from abc import ABC, abstractmethod
class Numero(ABC):
    
    @abstractmethod
    def valor(self)-> float:
        """Retorna el valor numerico actual"""
        pass
    @abstractmethod
    def imprimir(self) -> None:
        """Imprime el valor numerico actual"""
        pass
    
class NumeroBase(Numero):
    def __init__(self, n: float)-> None:
        """Inicializa el numero base"""
        self._valor=n
    def valor(self)-> float:
            return self._valor
        
    def imprimir(self)-> None:
            print(f"Valor: {self._valor}")

class OperacionDecorator(Numero):
    def __init__(self, numero: Numero)-> None:
        self._numero= numero
    
    def valor(self) -> float: 
        return self._numero.valor()
    
    def imprimir(self)-> None:
        self._numero.imprimir()
class Sumar2(OperacionDecorator):
    """Decorator que suma 2 al valor."""

    def valor(self) -> float:
        return self._numero.valor() + 2

    def imprimir(self) -> None:
        print(f"Sumar 2: {self.valor()}")


class Multiplicar2(OperacionDecorator):
    """Decorator que multiplica por 2 el valor."""

    def valor(self) -> float:
        return self._numero.valor() * 2

    def imprimir(self) -> None:
        print(f"Multiplicar por 2: {self.valor()}")


class Dividir3(OperacionDecorator):
    """Decorator que divide por 3 el valor."""

    def valor(self) -> float:
        return self._numero.valor() / 3

    def imprimir(self) -> None:
        print(f"Dividir por 3: {self.valor()}")
        
def main()-> None:
    
    numero = NumeroBase(10)
    print("Número Base ")
    numero.imprimir()

    
    print("Agregando Sumar 2")
    numero = Sumar2(numero)
    numero.imprimir()

    
    print("Agregando Multiplicar por 2 ")
    numero = Multiplicar2(numero)
    numero.imprimir()

    
    print("Agregando Dividir por 3 ")
    numero = Dividir3(numero)
    numero.imprimir()

    
    print(f"Resultado final: {numero.valor()}")


if __name__ == "__main__":
    main()