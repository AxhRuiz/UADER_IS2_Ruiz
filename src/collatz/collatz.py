import matplotlib.pyplot as plt

def collatz_iteraciones(n):
   
    iteraciones = 0
    
    while n != 1:
        if n % 2 == 0:
            # Si es par, dividir por 2
            n = n // 2
        else:
            # Si es impar, aplicar 3n + 1
            n = 3 * n + 1
        iteraciones += 1
    
    return iteraciones

def main():
    """
    Programa que calcula iteraciones para números del 1 al 10000
    y genera el gráfico.
    """
    print("Calculando la conjetura de Collatz para números del 1 al 10000...")
    
    # Listas para almacenar datos
    numeros = []
    iteraciones = []
    
    # Calcular iteraciones para cada número
    for i in range(1, 10001):
        numeros.append(i)
        iteraciones.append(collatz_iteraciones(i))
        
        # Mostrar progreso cada 1000 números
        if i % 1000 == 0:
            print(f"Procesados {i} números...")
    
    print("Cálculo completado. Generando gráfico...")
    
    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.scatter(iteraciones, numeros, s=1, alpha=0.5, c='blue')
    
    # Etiquetas y título
    plt.xlabel("Número de iteraciones")
    plt.ylabel("Número inicial (n)")
    plt.title("Conjetura de Collatz: Iteraciones por número inicial (1 a 10000)")
    
    # Agregar cuadrícula
    plt.grid(True, alpha=0.3)
    
    # Guardar el gráfico como imagen
    plt.savefig("collatz_grafico.png", dpi=150, bbox_inches='tight')
    print("Gráfico guardado como 'collatz_grafico.png'")
    
    # Mostrar el gráfico
    plt.show()
    
    # Mostrar estadísticas
    print(f"Máximo de iteraciones: {max(iteraciones)}")
    print(f"Mínimo de iteraciones: {min(iteraciones)}")
    print(f"Promedio de iteraciones: {sum(iteraciones)/len(iteraciones):.2f}")
    
    # Encontrar el número con más iteraciones
    max_iter = max(iteraciones)
    indice_max = iteraciones.index(max_iter)
    print(f"Número con más iteraciones: {numeros[indice_max]} ({max_iter} iteraciones)")

if __name__ == "__main__":
    main()
