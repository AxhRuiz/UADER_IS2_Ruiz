# Ejemplo práctico de builder
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Builder
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Qué está ocurriendo conceptualmente

El patrón Builder separa claramente cuatro roles:

Producto (Computadora)
Es el objeto complejo que se está construyendo.

Builder abstracto (BuilderComputadora)
Define los pasos de construcción, pero no cómo se implementan.

Builders concretos (BuilderPCGamer, BuilderPCOficina)
Definen configuraciones específicas del producto.

Director (Director)
Controla el orden de construcción, sin conocer detalles concretos.
from abc import ABC, abstractmethod
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Computadora:
    """Producto complejo que se construye paso a paso."""

    def __init__(self) -> None:
        self.componentes = []

    def agregar(self, componente: str) -> None:
        self.componentes.append(componente)

    def mostrar(self) -> str:
        return "Computadora con:\n  - " + "\n  - ".join(self.componentes)


class BuilderComputadora(ABC):
    """Interfaz abstracta del Builder."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._producto = Computadora()

    def obtener_resultado(self) -> Computadora:
        producto = self._producto
        self.reset()  # permite reutilizar el builder
        return producto

    @abstractmethod
    def construir_cpu(self) -> None:
        pass

    @abstractmethod
    def construir_memoria(self) -> None:
        pass

    @abstractmethod
    def construir_almacenamiento(self) -> None:
        pass

    @abstractmethod
    def construir_gpu(self) -> None:
        pass


class BuilderPCGamer(BuilderComputadora):
    """Builder concreto para una PC Gamer."""

    def construir_cpu(self) -> None:
        self._producto.agregar("CPU de alto rendimiento")

    def construir_memoria(self) -> None:
        self._producto.agregar("32GB RAM")

    def construir_almacenamiento(self) -> None:
        self._producto.agregar("SSD NVMe 1TB")

    def construir_gpu(self) -> None:
        self._producto.agregar("GPU dedicada RTX")


class BuilderPCOficina(BuilderComputadora):
    """Builder concreto para una PC de oficina."""

    def construir_cpu(self) -> None:
        self._producto.agregar("CPU estándar")

    def construir_memoria(self) -> None:
        self._producto.agregar("8GB RAM")

    def construir_almacenamiento(self) -> None:
        self._producto.agregar("SSD 256GB")

    def construir_gpu(self) -> None:
        self._producto.agregar("GPU integrada")


class Director:
    """
    El Director define el orden de construcción.
    No conoce los detalles concretos del producto.
    """

    def __init__(self, builder: BuilderComputadora) -> None:
        self._builder = builder

    def construir_computadora_basica(self) -> None:
        self._builder.construir_cpu()
        self._builder.construir_memoria()
        self._builder.construir_almacenamiento()

    def construir_computadora_completa(self) -> None:
        self._builder.construir_cpu()
        self._builder.construir_memoria()
        self._builder.construir_almacenamiento()
        self._builder.construir_gpu()


def main() -> None:
    # PC Gamer
    builder_gamer = BuilderPCGamer()
    director = Director(builder_gamer)

    director.construir_computadora_completa()
    pc_gamer = builder_gamer.obtener_resultado()
    print("PC Gamer:")
    print(pc_gamer.mostrar())
    print()

    # PC Oficina
    builder_oficina = BuilderPCOficina()
    director = Director(builder_oficina)

    director.construir_computadora_basica()
    pc_oficina = builder_oficina.obtener_resultado()
    print("PC Oficina:")
    print(pc_oficina.mostrar())


if __name__ == "__main__":
    main()
