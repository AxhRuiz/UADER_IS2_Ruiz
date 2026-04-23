# Ejemplo de abstract factory
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* abstract factory
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""

Primero están los productos abstractos, que definen las interfaces comunes. En este caso son Boton y Ventana.

Después aparecen los productos concretos, como BotonClaro, VentanaClara, BotonOscuro y VentanaOscura. Cada uno implementa una variante particular.

Luego está la fábrica abstracta, FabricaGUI, que define qué tipos de productos puede crear la familia.

Finalmente están las fábricas concretas, FabricaTemaClaro y FabricaTemaOscuro, que producen conjuntos consistentes de objetos.

El cliente, que aquí es Aplicacion, recibe una fábrica y trabaja únicamente con interfaces abstractas. No necesita saber si está usando tema claro o tema oscuro.

Para qué es útil

Este patrón es útil cuando en tu sistema existen familias de objetos relacionados y necesitas asegurar que se usen de manera consistente.
"""


from abc import ABC, abstractmethod


# =========================
# Productos abstractos
# =========================

class Boton(ABC):
    """Interfaz abstracta para botones."""

    @abstractmethod
    def renderizar(self) -> str:
        pass


class Ventana(ABC):
    """Interfaz abstracta para ventanas."""

    @abstractmethod
    def mostrar(self) -> str:
        pass


# =========================
# Productos concretos - Tema Claro
# =========================

class BotonClaro(Boton):
    """Botón concreto para tema claro."""

    def renderizar(self) -> str:
        return "Renderizando botón de tema claro."


class VentanaClara(Ventana):
    """Ventana concreta para tema claro."""

    def mostrar(self) -> str:
        return "Mostrando ventana de tema claro."


# =========================
# Productos concretos - Tema Oscuro
# =========================

class BotonOscuro(Boton):
    """Botón concreto para tema oscuro."""

    def renderizar(self) -> str:
        return "Renderizando botón de tema oscuro."


class VentanaOscura(Ventana):
    """Ventana concreta para tema oscuro."""

    def mostrar(self) -> str:
        return "Mostrando ventana de tema oscuro."


# =========================
# Abstract Factory
# =========================

class FabricaGUI(ABC):
    """Interfaz abstracta para crear una familia de componentes GUI."""

    @abstractmethod
    def crear_boton(self) -> Boton:
        pass

    @abstractmethod
    def crear_ventana(self) -> Ventana:
        pass


# =========================
# Fábricas concretas
# =========================

class FabricaTemaClaro(FabricaGUI):
    """Fábrica concreta para componentes de tema claro."""

    def crear_boton(self) -> Boton:
        return BotonClaro()

    def crear_ventana(self) -> Ventana:
        return VentanaClara()


class FabricaTemaOscuro(FabricaGUI):
    """Fábrica concreta para componentes de tema oscuro."""

    def crear_boton(self) -> Boton:
        return BotonOscuro()

    def crear_ventana(self) -> Ventana:
        return VentanaOscura()


# =========================
# Cliente
# =========================

class Aplicacion:
    """
    El cliente trabaja solo con interfaces abstractas.
    No depende de clases concretas.
    """

    def __init__(self, fabrica: FabricaGUI) -> None:
        self.boton = fabrica.crear_boton()
        self.ventana = fabrica.crear_ventana()

    def dibujar(self) -> None:
        print(self.ventana.mostrar())
        print(self.boton.renderizar())


def main() -> None:
    print("=== Aplicación con tema claro ===")
    fabrica_clara = FabricaTemaClaro()
    app_clara = Aplicacion(fabrica_clara)
    app_clara.dibujar()

    print()

    print("=== Aplicación con tema oscuro ===")
    fabrica_oscura = FabricaTemaOscuro()
    app_oscura = Aplicacion(fabrica_oscura)
    app_oscura.dibujar()


if __name__ == "__main__":
    main()
