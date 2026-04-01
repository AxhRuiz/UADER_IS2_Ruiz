import sys

class Factorial:
    
    def __init__(self, entrada):
        self.entrada = entrada
        self.resultados = {}   
        self.mensaje = ""      


    '''Función que recibe el argumento y calcula el factorial de un número
    si el argumento es negativo, retorna none'''
    def _calcular_factorial(self, num):
        if num == 0:
            return 1
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            return fact
        

    '''Función que analiza la entrada, si el argumento es válido determina
    el inicio y el fin, si no es válido retorna none'''
    def _parsear_entrada(self):
        entrada = self.entrada
        
        if '-' not in entrada:
            try:
                num = int(entrada)
                return (num, num)
            except ValueError:
                return (None, None)
        
        partes = entrada.split('-')

        if partes[0] == '' and partes[1] != '':
            return (1, int(partes[1]))
        elif partes[0] != '' and partes[1] == '':
            return (int(partes[0]), 60)
        elif partes[0] != '' and partes[1] != '':
            return (int(partes[0]), int(partes[1]))
        
        return (None, None)

    '''Función que realiza los cálculos y devuelve el diccionario con los resultados'''
    def calcular(self):
        inicio, fin = self._parsear_entrada()
        
        if inicio is None or fin is None:
            self.mensaje = "Formato no válido. Use: 5, 4-8, -10, 5-"
            return None
        
        if inicio > fin:
            self.mensaje = f"Error: {inicio} > {fin}"
            return None
        
        self.mensaje = f"Calculando factoriales desde {inicio} hasta {fin}:"
        
        for num in range(inicio, fin + 1):
            fact = self._calcular_factorial(num)
            self.resultados[num] = fact
        
        return self.resultados

    #función que muestra los resultados
    def mostrar_resultados(self):
        print(self.mensaje)
        
        if self.resultados:
            print("\nResultados\n")
            for num, fact in self.resultados.items():
                print(f"Factorial {num}! = {fact}")

    #función que devuelce los resultados como diccionario
    def get_resultados(self):
        return self.resultados


if __name__ == "__main__":
    # Obtiene el argumento
    if len(sys.argv) < 2:
        entrada = input("Ingrese un número o rango (ej: 5, 4-8, -10, 5-): ")
    else:
        entrada = sys.argv[1]
    
    calc = Factorial(entrada)    # Crea un objeto con la entrada

    calc.calcular()             # Calcula factorial
    calc.mostrar_resultados()   # Muestra los resultados
