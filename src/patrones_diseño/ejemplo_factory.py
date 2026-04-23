# Ejemplo práctico de aplicación de patrón factory
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Singleton
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Cuándo conviene usar Factory

Este patrón resulta útil cuando:

se necesita crear objetos de distintas clases según una condición,
se quiere  evitar muchos if/elif repartidos por todo el sistema,
se quiere desacoplar el código cliente de las clases concretas.

"""

from abc import ABC, abstractmethod


class Transporte(ABC):
    """Clase base abstracta para distintos tipos de transporte."""

    @abstractmethod
    def entregar(self) -> str:
        """Realiza la entrega y devuelve un mensaje descriptivo."""
        pass


class Camion(Transporte):
    """Implementación concreta de transporte por camión."""

    def entregar(self) -> str:
        return "La entrega se realiza por carretera usando un camión."


class Barco(Transporte):
    """Implementación concreta de transporte por barco."""

    def entregar(self) -> str:
        return "La entrega se realiza por vía marítima usando un barco."


class Avion(Transporte):
    """Implementación concreta de transporte por avión."""

    def entregar(self) -> str:
        return "La entrega se realiza por vía aérea usando un avión."


class TransporteFactory:
    """Fábrica encargada de crear objetos de tipo Transporte."""

    @staticmethod
    def crear_transporte(tipo: str) -> Transporte:
        """
        Crea y devuelve una instancia concreta de Transporte.

        Args:
            tipo: Tipo de transporte solicitado.

        Returns:
            Una instancia de una subclase de Transporte.

        Raises:
            ValueError: Si el tipo solicitado no es válido.
        """
        tipo_normalizado = tipo.strip().lower()

        if tipo_normalizado == "camion":
            return Camion()
        if tipo_normalizado == "barco":
            return Barco()
        if tipo_normalizado == "avion":
            return Avion()

        raise ValueError(
            f"Tipo de transporte no soportado: '{tipo}'. "
            "Opciones válidas: camion, barco, avion."
        )


def main() -> None:
    """Función principal de demostración."""
    tipos = ["camion", "barco", "avion", "tren"]

    for tipo in tipos:
        try:
            transporte = TransporteFactory.crear_transporte(tipo)
            print(f"{tipo!r} -> {transporte.entregar()}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
