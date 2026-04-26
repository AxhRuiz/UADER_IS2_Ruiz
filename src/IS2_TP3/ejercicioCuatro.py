"""4. Implemente una clase “factura” que tenga un importe correspondiente al total
de la factura pero de acuerdo a la condición impositiva del cliente (IVA
Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
condición"""

from abc import ABC, abstractmethod

class Factura(ABC):
    def __init__(self, importe: float):
        self.importe = importe
    
    @abstractmethod
    def generar(self) -> str:
        pass
    
class IvaInscripto(Factura):
    def generar(self) -> str :
        return (f"Factura IVA Inscripto - Importe: ${self.importe}")
        
class IvaNoInscripto(Factura):
    def generar(self) -> str:
        return (f"Factura IVA No Inscripto - Importe: ${self.importe}")
    
class IvaExento(Factura):
    def generar(self)-> str:
        return (f"Factura IVA Exento - Importe: ${self.importe}")
       
class FacturaFactory:
    def crear_factura (self, importe:float,tipo: str) -> Factura:
        tipo_normalizado= tipo.strip().lower()
        
        if (tipo_normalizado == "iva inscripto"):
            return IvaInscripto(importe)
        elif (tipo_normalizado =="iva no inscripto"):
            return IvaNoInscripto(importe)
        elif (tipo_normalizado == "iva exento"):
            return IvaExento(importe)
        else:
            raise ValueError(
                f"Tipo de condicion impositiva invalida {tipo}"
        )
            

def main() -> None:
    tipos= ["IVA Inscripto", "IVA No Inscripto", "IVA Exento"]
    factory= FacturaFactory()
    for tipo in tipos:
        try:    
            factura= factory.crear_factura(35.5, tipo)
            print(f"{tipo} -> {factura.generar()}")
        except ValueError as error:
            print(f"Error: {error}")

if __name__ =="__main__":
    main()