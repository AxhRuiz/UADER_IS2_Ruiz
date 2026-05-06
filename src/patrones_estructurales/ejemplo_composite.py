
# Ejemplo práctico de aplicación de patrón composite
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Composite
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Composite es útil cuando el problema tiene una estructura jerárquica tipo árbol:
	carpetas y archivos
	menús y submenús
	organigramas
	productos compuestos por partes
	componentes gráficos anidados
	tareas y subtareas de un proyecto


La idea central es que el cliente no tenga que preguntar:
	if es_archivo:    ...
	elif es_carpeta:    ...

sino usar todos los elementos mediante una interfaz común.
Composite responde a la  necesidad:
“Se necesita tratar objetos simples y grupos de objetos de la misma manera.”
"""

from abc import ABC, abstractmethod


class RecursoSistemaArchivos(ABC):
    """Componente abstracto común para archivos y carpetas."""

    @abstractmethod
    def obtener_tamano(self) -> int:
        pass

    @abstractmethod
    def mostrar(self, indentacion: int = 0) -> None:
        pass


class Archivo(RecursoSistemaArchivos):
    """Hoja del Composite."""

    def __init__(self, nombre: str, tamano: int) -> None:
        self.nombre = nombre
        self.tamano = tamano

    def obtener_tamano(self) -> int:
        return self.tamano

    def mostrar(self, indentacion: int = 0) -> None:
        espacio = " " * indentacion
        print(f"{espacio}- Archivo: {self.nombre} ({self.tamano} KB)")


class Carpeta(RecursoSistemaArchivos):
    """Composite que puede contener archivos u otras carpetas."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.recursos: list[RecursoSistemaArchivos] = []

    def agregar(self, recurso: RecursoSistemaArchivos) -> None:
        self.recursos.append(recurso)

    def remover(self, recurso: RecursoSistemaArchivos) -> None:
        self.recursos.remove(recurso)

    def obtener_tamano(self) -> int:
        return sum(recurso.obtener_tamano() for recurso in self.recursos)

    def mostrar(self, indentacion: int = 0) -> None:
        espacio = " " * indentacion
        print(f"{espacio}+ Carpeta: {self.nombre} ({self.obtener_tamano()} KB)")
        for recurso in self.recursos:
            recurso.mostrar(indentacion + 4)


def main() -> None:
    raiz = Carpeta("proyecto")

    src = Carpeta("src")
    src.agregar(Archivo("main.py", 12))
    src.agregar(Archivo("factory.py", 8))
    src.agregar(Archivo("composite.py", 10))

    tests = Carpeta("tests")
    tests.agregar(Archivo("test_factory.py", 6))
    tests.agregar(Archivo("test_composite.py", 7))

    docs = Carpeta("docs")
    docs.agregar(Archivo("README.md", 4))
    docs.agregar(Archivo("arquitectura.pdf", 320))

    raiz.agregar(src)
    raiz.agregar(tests)
    raiz.agregar(docs)
    raiz.agregar(Archivo("requirements.txt", 2))

    raiz.mostrar()

    print()
    print(f"Tamaño total del proyecto: {raiz.obtener_tamano()} KB")


if __name__ == "__main__":
    main()
