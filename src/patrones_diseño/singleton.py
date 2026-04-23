# Straightforward implementation of the Singleton Pattern
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Singleton
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
class LoggerSans(object):
    def __new__(cls):
        cls._instance = super(LoggerSans,cls).__new__(cls)
        return cls._instance

class Logger(object):
    _instance = None
    pepe=0
    def __init__(self):
        pepe=0
        print('Inicializa el objeto')

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
#*------------------------------------------------------------------
import os
os.system('clear')

print("Genero objetos sin utilizar SINGLETON")
log1s= LoggerSans()
log2s= LoggerSans()

print(log1s)
print(log2s)

print("Genero ahora objetos utilizando SINGLETON")
log1 = Logger()
log1.pepe=log1.pepe+1
print(log1,log1.pepe)
log2 = Logger()
log2.pepe=log2.pepe+1
print(log2,log2.pepe)

