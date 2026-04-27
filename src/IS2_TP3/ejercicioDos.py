"""2. Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
deberá recibir un valor de importe base imponible y deberá retornar la suma
del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
esa base imponible.
"""
import json
from threading import Lock
class CalculadoraImpuesto:
    _instancia = None #Almacena la unica instancia de la clase
    _lock = Lock()  #Candado para sincronizacion en entornos multihilos
    
    def __new__(cls, *args, **kwargs): #controla la creacion de instancias
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None: #implementa doble verificacion garantizando una unica instancia
                    cls._instancia = super().__new__(cls)
        return cls._instancia #Retorna la unica instancia de la clase
    
    def __init__(self, archivo_config: str = None): #Inicializa la configuracion una sola vez
        if not hasattr(self, "_inicializado"):
            self._config= {}
            if archivo_config:
                self._cargar_desde_archivo(archivo_config) #ruta opcional a Json de configuracion
            self._inicializado = True
    
    def _cargar_desde_archivo(self, archivo: str)-> None: #Carga la configuracion desde un archivo JSON
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                self._config= json.load(f)
        except FileNotFoundError:
            print(f"Archivo de configuracion no encontrado: {archivo}") #mensaje de error al no encontrar la configuracion, Siendo archivo la ruta del msimo
            self._config= {} #se establece la configuracion vacia
        except json.JSONDecodeError as e: 
            print(f"Error en formato Json: {e} , usando configuracion vacia") #error en archivo json
            self._config={} #se establce la configuracion vacia
            
    def obtener(self,clave:str, default=None): #obtiene un valor de configuracion ; clave: nombde de la clave a buscar ; default: balor por defecto si la clave no existe
        return self._config.get(clave, default) #retorna el valor asociado a la clave o default
    
    def establecer(self, clave:str, valor)-> None: #establece un valor en la configuracion; clave: nombbre de la clave; valor: valor a guardar
        self._config[clave]= valor
        
    def __str__(self)-> str: #retorna una representacion legible de la configuracion
        return (f"Configuracion actual {self._config}")
    
    def calcular(self, base_imponible: float)-> float: #calcula la suma de impuestos sobre una base imponible
        return base_imponible * (0.21 + 0.05 + 0.012) #retorna la suma total de los 3 impuestos
    
def main():#demostracion del Patron singleton
    calculo_impuestos= CalculadoraImpuesto() #crea dos referencias a la calculadora
    calculo_impuestos2= CalculadoraImpuesto()
    
    print("¿Son la misma instancia?", calculo_impuestos is calculo_impuestos2) #verifica que sean la misma instancia
    
    print("se realiza calculo de impuestos sobre 275.02", calculo_impuestos.calcular(275.02), 
          "monto final:", 275.02 + calculo_impuestos.calcular(275.02) ) #realiza los calculos correspondientes
    print("se realiza calculo de impuestos sobre 300.52", calculo_impuestos2.calcular(300.52),
          "monto final: ", 300.52 + calculo_impuestos2.calcular(300.52))

if __name__ =="__main__":
    main()
    
