# Ejemplo práctico de aplicación de patrón proxy
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Proxy
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Proxy es útil cuando se debe controlar el acceso a otro objeto.

Casos típicos:

	carga diferida de recursos pesados,
	control de permisos,
	caché,
	acceso remoto,
	logging,
	rate limiting,
	validación previa,
	protección de recursos costosos.

Proxy actúa como representante de otro objeto.
El cliente cree hablar con el objeto real, pero en realidad habla con un intermediario que controla el acceso 
y eventualmente hace alguna actividad (ej. un registro o validación) antes de acceder al objeto final.
"""
from abc import ABC, abstractmethod
import time


class Documento(ABC):
    """Interfaz común para el documento real y el proxy."""

    @abstractmethod
    def mostrar(self) -> None:
        pass


class DocumentoRemoto(Documento):
    """Objeto real costoso de crear o cargar."""

    def __init__(self, nombre_archivo: str) -> None:
        self.nombre_archivo = nombre_archivo
        self.contenido = self._descargar_documento()

    def _descargar_documento(self) -> str:
        print(f"[Servidor] Descargando documento {self.nombre_archivo}...")
        time.sleep(1)
        return "Contenido confidencial del documento."

    def mostrar(self) -> None:
        print(f"[Documento] {self.nombre_archivo}")
        print(self.contenido)


class DocumentoProxy(Documento):
    """
    Proxy.

    Controla el acceso al documento real y lo carga bajo demanda.
    """

    def __init__(self, nombre_archivo: str, usuario: str, autorizado: bool) -> None:
        self.nombre_archivo = nombre_archivo
        self.usuario = usuario
        self.autorizado = autorizado
        self._documento_real: DocumentoRemoto | None = None

    def mostrar(self) -> None:
        if not self.autorizado:
            print(f"[Proxy] Acceso denegado para el usuario {self.usuario}.")
            return

        if self._documento_real is None:
            print("[Proxy] Documento no cargado. Cargando ahora...")
            self._documento_real = DocumentoRemoto(self.nombre_archivo)
        else:
            print("[Proxy] Usando documento ya cargado en memoria.")

        self._documento_real.mostrar()


def main() -> None:
    print("=== Usuario sin permiso ===")
    documento = DocumentoProxy(
        nombre_archivo="contrato_confidencial.pdf",
        usuario="invitado",
        autorizado=False,
    )
    documento.mostrar()

    print("\n=== Usuario autorizado ===")
    documento = DocumentoProxy(
        nombre_archivo="contrato_confidencial.pdf",
        usuario="admin",
        autorizado=True,
    )

    documento.mostrar()
    print()
    documento.mostrar()


if __name__ == "__main__":
    main()
