"""4. Implemente una clase “factura” que tenga un importe correspondiente al total
de la factura pero de acuerdo a la condición impositiva del cliente (IVA
Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
condición"""

from abc import ABC, abstractmethod

class Factura(ABC): #producto abstracto: Factura
    #Define la inteerfaz comun para todos los tipos de factura
    def __init__(self, importe: float): #inicializa la factura con el importe dado
        self.importe = importe #importe: Monto total de la factura
    
    @abstractmethod
    def generar(self) -> str: #genera la representacion de la factura
        pass
    
class IvaInscripto(Factura): #Factura para clientes con IVA inscripto
    def generar(self) -> str :
        return (f"Factura IVA Inscripto - Importe: ${self.importe}")
        
class IvaNoInscripto(Factura): #Factura para clientes con IVA no inscripto
    def generar(self) -> str:
        return (f"Factura IVA No Inscripto - Importe: ${self.importe}")
    
class IvaExento(Factura): #Factura para clientes con IVA exento
    def generar(self)-> str:
        return (f"Factura IVA Exento - Importe: ${self.importe}")
       
class FacturaFactory: #factory para crear facturas segun la condicion impositiva
    
    def crear_factura (self, importe:float,tipo: str) -> Factura:#cre y retorna la factura correspondiente al tipo indicado.
        tipo_normalizado= tipo.strip().lower()
        
        if (tipo_normalizado == "iva inscripto"): #retorna la instancia concreta de factura segun el tipo
            return IvaInscripto(importe)
        elif (tipo_normalizado =="iva no inscripto"):
            return IvaNoInscripto(importe)
        elif (tipo_normalizado == "iva exento"):
            return IvaExento(importe)
        else:
            raise ValueError( #si el tipo de condicion impositiva no es valida
                f"Tipo de condicion impositiva invalida {tipo}"
        )
            

def main() -> None: #Demostracion del patron Factory aplicado.
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