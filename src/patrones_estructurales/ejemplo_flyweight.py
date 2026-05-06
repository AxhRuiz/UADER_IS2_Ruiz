
# Ejemplo práctico de aplicación de patrón flyweight
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Flyweight
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Flyweight es útil cuando hay una gran cantidad de objetos similares y quieres reducir el consumo de memoria.
Casos típicos:
	editores gráficos
	videojuegos
	mapas
	sistemas CAD
	renderizado de caracteres en texto
	simulaciones con muchos agentes
	catálogos con objetos repetidos


Flyweight permite compartir la parte común de muchos objetos, manteniendo separada la parte que cambia. En 
una frase: Si muchos objetos se parecen mucho, no se debe duplicar sino compartir lo común
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class TipoArbol:
    """
    Flyweight.

    Contiene el estado intrínseco compartido por muchos árboles.
    """
    especie: str
    color: str
    textura: str
    imagen: str

    def dibujar(self, x: int, y: int, altura: float) -> None:
        """
        Usa datos externos para dibujar un árbol concreto.
        """
        print(
            f"Dibujando {self.especie} en ({x}, {y}), "
            f"altura={altura}m, color={self.color}, imagen={self.imagen}"
        )


class FabricaTiposArbol:
    """
    Flyweight Factory.

    Reutiliza instancias existentes de TipoArbol en lugar de crear duplicados.
    """

    def __init__(self) -> None:
        self._tipos: dict[tuple[str, str, str, str], TipoArbol] = {}

    def obtener_tipo(
        self,
        especie: str,
        color: str,
        textura: str,
        imagen: str,
    ) -> TipoArbol:
        clave = (especie, color, textura, imagen)

        if clave not in self._tipos:
            print(f"[Factory] Creando nuevo tipo de árbol: {especie}")
            self._tipos[clave] = TipoArbol(
                especie=especie,
                color=color,
                textura=textura,
                imagen=imagen,
            )
        else:
            print(f"[Factory] Reutilizando tipo de árbol: {especie}")

        return self._tipos[clave]

    def cantidad_tipos_creados(self) -> int:
        return len(self._tipos)


@dataclass
class Arbol:
    """
    Contexto.

    Contiene el estado extrínseco propio de cada árbol.
    """
    x: int
    y: int
    altura: float
    tipo: TipoArbol

    def dibujar(self) -> None:
        self.tipo.dibujar(self.x, self.y, self.altura)


class Bosque:
    """Cliente que administra muchos árboles."""

    def __init__(self) -> None:
        self._arboles: list[Arbol] = []
        self._fabrica = FabricaTiposArbol()

    def plantar_arbol(
        self,
        x: int,
        y: int,
        altura: float,
        especie: str,
        color: str,
        textura: str,
        imagen: str,
    ) -> None:
        tipo = self._fabrica.obtener_tipo(
            especie=especie,
            color=color,
            textura=textura,
            imagen=imagen,
        )

        arbol = Arbol(
            x=x,
            y=y,
            altura=altura,
            tipo=tipo,
        )

        self._arboles.append(arbol)

    def dibujar(self) -> None:
        for arbol in self._arboles:
            arbol.dibujar()

    def cantidad_arboles(self) -> int:
        return len(self._arboles)

    def cantidad_tipos_arbol(self) -> int:
        return self._fabrica.cantidad_tipos_creados()


def main() -> None:
    bosque = Bosque()

    bosque.plantar_arbol(
        x=10,
        y=20,
        altura=4.5,
        especie="Pino",
        color="verde oscuro",
        textura="rugosa",
        imagen="pino.png",
    )

    bosque.plantar_arbol(
        x=15,
        y=25,
        altura=5.1,
        especie="Pino",
        color="verde oscuro",
        textura="rugosa",
        imagen="pino.png",
    )

    bosque.plantar_arbol(
        x=40,
        y=80,
        altura=3.2,
        especie="Jacarandá",
        color="violeta",
        textura="media",
        imagen="jacaranda.png",
    )

    bosque.plantar_arbol(
        x=55,
        y=90,
        altura=3.8,
        especie="Jacarandá",
        color="violeta",
        textura="media",
        imagen="jacaranda.png",
    )

    print("\n=== Dibujando bosque ===")
    bosque.dibujar()

    print("\n=== Resumen ===")
    print(f"Árboles plantados: {bosque.cantidad_arboles()}")
    print(f"Tipos de árbol creados: {bosque.cantidad_tipos_arbol()}")


if __name__ == "__main__":
    main()
