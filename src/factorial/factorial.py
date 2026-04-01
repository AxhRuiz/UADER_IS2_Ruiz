#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


if len(sys.argv) < 2:
    # Si no hay argumento, se pide que ingrese un número
    #num = int(input("Ingrese un número para calcular su factorial: "))
    # Sin argumento, solicitar entrada
    entrada = input("Ingrese un número o rango (ej: 5, 4-8): ")
else:
    # Si hay argumento, calula su factorial
    num = int(sys.argv[1])

    print("Factorial ", num, "! es ", factorial(num))
    entrada = sys.argv[1]

# Verificar si es un rango (contiene '-')
if '-' in entrada:
    partes = entrada.split('-')
    
    # Rango completo: "4-8"
    if len(partes) == 2 and partes[0] != '' and partes[1] != '':
        inicio = int(partes[0])
        fin = int(partes[1])
        
        # Calcular factorial para cada número en el rango
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        for i in range(inicio, fin + 1):
            print(f"Factorial {i}! = {factorial(i)}")
    else:
        print("Formato no válido. Use: numero (ej: 5) o rango (ej: 4-8)")
else:
    # Es un número simple
    num = int(entrada)
    print(f"Factorial {num}! = {factorial(num)}")
