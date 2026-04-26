"""2. Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
deberá recibir un valor de importe base imponible y deberá retornar la suma
del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
esa base imponible.
"""
import json
from threading import Lock
class CalculadoraImpuesto:
    _instancia = None
    _lock = Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, archivo_config: str = None):
        if not hasattr(self, "_inicializado"):
            self._config= {}
            if archivo_config:
                self._cargar_desde_archivo(archivo_config)
            self._inicializado = True
    
    def _cargar_desde_archivo(self, archivo: str)-> None:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                self._config= json.load(f)
        except FileNotFoundError:
            print(f"Archivo de configuracion no encontrado: {archivo}")
            self._config= {}
        except json.JSONDecodeError as e: 
            print(f"Error en formato Json: {e} , usando configuracion vacia")
            self._config={}
            
    def obtener(self,clave:str, default=None):
        return self._config.get(clave, default)
    
    def establecer(self, clave:str, valor)-> None:
        self._config[clave]= valor
        
    def __str__(self)-> str:
        return (f"Configuracion actual {self._config}")
    
    def calcular(self, base_imponible: float)-> float:
        return base_imponible * (0.21 + 0.05 + 0.012)
    
def main():
    calculo_impuestos= CalculadoraImpuesto()
    calculo_impuestos2= CalculadoraImpuesto()
    
    print("¿Son la misma instancia?", calculo_impuestos is calculo_impuestos2)
    
    print("se realiza calculo de impuestos sobre 275.02", calculo_impuestos.calcular(275.02),
          "monto final:", 275.02 + calculo_impuestos.calcular(275.02) )
    print("se realiza calculo de impuestos sobre 300.52", calculo_impuestos2.calcular(300.52),
          "monto final: ", 300.52 + calculo_impuestos2.calcular(300.52))

if __name__ =="__main__":
    main()
    
