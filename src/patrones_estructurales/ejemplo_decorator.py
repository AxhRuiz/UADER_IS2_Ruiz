# Ejemplo práctico de aplicación de patrón decorator
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Decorator
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Decorator es útil cuando es necesario agregar capacidades opcionales sin modificar
 la clase original y sin crear una explosión de subclases.

Casos típicos:

	logging
	compresión
	cifrado
	validación
	caché
	autorización
	envío multicanal
	métricas
	reintentos

Diferencia con Composite

Ambos usan composición, pero con objetivos distintos.
Decorator agrega comportamiento adicional envolviendo objetos.

Composite agrupa objetos; Decorator envuelve objetos para extenderlos.
"""

from abc import ABC, abstractmethod


class Notificador(ABC):
    """Interfaz común para todos los notificadores."""

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


class NotificadorEmail(Notificador):
    """Componente concreto: notificación básica por email."""

    def enviar(self, mensaje: str) -> None:
        print(f"[EMAIL] {mensaje}")


class NotificadorDecorator(Notificador):
    """
    Decorator base.

    Mantiene una referencia a otro objeto Notificador.
    """

    def __init__(self, notificador: Notificador) -> None:
        self._notificador = notificador

    def enviar(self, mensaje: str) -> None:
        self._notificador.enviar(mensaje)


class NotificadorSMS(NotificadorDecorator):
    """Decorator concreto: agrega envío por SMS."""

    def enviar(self, mensaje: str) -> None:
        super().enviar(mensaje)
        print(f"[SMS] {mensaje}")


class NotificadorWhatsApp(NotificadorDecorator):
    """Decorator concreto: agrega envío por WhatsApp."""

    def enviar(self, mensaje: str) -> None:
        super().enviar(mensaje)
        print(f"[WHATSAPP] {mensaje}")


class NotificadorConLog(NotificadorDecorator):
    """Decorator concreto: agrega registro de auditoría."""

    def enviar(self, mensaje: str) -> None:
        print(f"[LOG] Enviando mensaje: {mensaje}")
        super().enviar(mensaje)


def main() -> None:
    print("=== Notificación básica ===")
    notificador = NotificadorEmail()
    notificador.enviar("Su factura está disponible.")

    print("\n=== Email + SMS ===")
    notificador = NotificadorSMS(NotificadorEmail())
    notificador.enviar("Su código de verificación es 123456.")

    print("\n=== Email + SMS + WhatsApp ===")
    notificador = NotificadorWhatsApp(
        NotificadorSMS(
            NotificadorEmail()
        )
    )
    notificador.enviar("Se detectó un acceso sospechoso.")

    print("\n=== Email + SMS + WhatsApp + Log ===")
    notificador = NotificadorConLog(
        NotificadorWhatsApp(
            NotificadorSMS(
                NotificadorEmail()
            )
        )
    )
    notificador.enviar("Transferencia realizada correctamente.")


if __name__ == "__main__":
    main()
