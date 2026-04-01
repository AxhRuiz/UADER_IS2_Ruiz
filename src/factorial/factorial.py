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
#ESTE ES UN COMENTARIO NUEVO

if len(sys.argv) < 2:
    # Sin argumento, solicitar entrada
    entrada = input("Ingrese un número o rango (ej: 5, 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Verificar si es un rango
if '-' in entrada:
    partes = entrada.split('-')
    
    # "-10" (no tiene limite inferior, desde 1 hasta 10)
    if len(partes) == 2 and partes[0] == '' and partes[1] != '':
        inicio = 1
        fin = int(partes[1])
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        for i in range(inicio, fin + 1):
            print(f"Factorial {i}! = {factorial(i)}")
    
    # "5-" (no tiene limite superior, desde 5 hasta 60)
    elif len(partes) == 2 and partes[0] != '' and partes[1] == '':
        inicio = int(partes[0])
        fin = 60
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        for i in range(inicio, fin + 1):
            print(f"Factorial {i}! = {factorial(i)}")
    
    # "4-8" (rango completo)
    elif len(partes) == 2 and partes[0] != '' and partes[1] != '':
        inicio = int(partes[0])
        fin = int(partes[1])
        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        for i in range(inicio, fin + 1):
            print(f"Factorial {i}! = {factorial(i)}")
    
    else:
        print("Formato no válido. Use: 5, 4-8, -10, 5-")
else:
    # Es un número simple
    num = int(entrada)
    print(f"Factorial {num}! = {factorial(num)}")
