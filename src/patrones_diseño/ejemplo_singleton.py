import json
from threading import Lock


class Configuracion:
    """
    Singleton para manejar la configuración global de la aplicación.
    """

    _instancia = None
    _lock = Lock()  # para hacerlo thread-safe

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:  # doble verificación
                    cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, archivo_config: str = None):
        """
        Inicializa la configuración solo una vez.
        """
        if not hasattr(self, "_inicializado"):
            self._config = {}
            if archivo_config:
                self._cargar_desde_archivo(archivo_config)
            self._inicializado = True

    def _cargar_desde_archivo(self, archivo: str) -> None:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                self._config = json.load(f)
        except FileNotFoundError:
            print(f"Archivo de configuración no encontrado: {archivo}")
            self._config = {}

    def obtener(self, clave: str, default=None):
        return self._config.get(clave, default)

    def establecer(self, clave: str, valor) -> None:
        self._config[clave] = valor

    def __str__(self) -> str:
        return f"Configuración actual: {self._config}"


def main():
    # Primera instancia
    config1 = Configuracion()
    config1.establecer("db_host", "localhost")
    config1.establecer("db_port", 5432)

    # Segunda "instancia"
    config2 = Configuracion()

    print("¿Son la misma instancia?", config1 is config2)

    # Acceso compartido
    print("Host desde config2:", config2.obtener("db_host"))

    # Modificación desde otra referencia
    config2.establecer("modo_debug", True)

    print("Config1:", config1)
    print("Config2:", config2)


if __name__ == "__main__":
    main()
