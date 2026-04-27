""""1. Provea una clase que dado un número entero cualquiera retorne el factorial del
mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
instancia de clase."""

""""""

import json
from threading import Lock

class CalculadoraFactorial:
    _instancia = None #Almacena la unica instancia de la clase
    _lock = Lock()  #Candado para la sincornizacion en entornos multihilo
    
    def __new__(cls, *args, **kwargs): #controla la crfeacion de instancias
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:  #implementa una doble verificacion garantizando una unica instancia
                    cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, archivo_config: str = None): #Inicializa la configuracion una vez
        if not hasattr(self, "_inicializado"):
            self._config= {}
            if archivo_config:
                self._cargar_desde_archivo(archivo_config) #archivo_config: Es la ruta opcional a un Json de configuracion
            self._inicializado = True
            
    def _cargar_desde_archivo(self, archivo:str)-> None:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                self._config = json.load(f) #Carga la configuracion desde un JSON
        except FileNotFoundError:
            print(f"Archivo de configuracion no encontrado: {archivo}") #mensaje de error al no encontrar la ruta
            self._config= {} #se utiliza la configuracion vacia
        except json.JSONDecodeError as e: 
            print(f"Error en formato Json: {e} , usando configuracion vacia") #ante un error de archivo, se procede a usar la configuracion vacia
            self._config={}
            
    def obtener(self, clave: str, default = None): #obtiene un valor de configuracion
        return self._config.get(clave, default) #args: siendo clave el nombre a buscar, default el valor por defecto si no existe clave
        #retorna el valor asociado a la clave o default
    
    def establecer(self, clave:str, valor) -> None: #establece un valor en la configuracion
        self._config[clave]= valor  #args: clave: nombre de la key; valor: valor a guardar
        
    def __str__(self)-> str: #Retorna una configuracion legible de la configuracion"
        return (f"configuracion actual {self._config}")
    
    def calcular(self,n: int)-> int: #Calcula el factorial de un numero de forma recursiva
        if n<=1:    #n: numero entero no negativo
            return 1
        return n* self.calcular(n-1) #retorna el factorial de n(n!)
    


def main(): #Demostracion del patron, aplicado al calculo factorial.
    calc1 = CalculadoraFactorial()
    calc2= CalculadoraFactorial()
    print(calc1 is calc2) #verificamos que llamen a la misma instancia
    print(calc1.calcular(5)) #Realizamos el calculo del factorial 5
    print(calc2.calcular(6)) #Realizamos el calculo del factorial 6
    
    


if __name__ == "__main__":
    main()
    