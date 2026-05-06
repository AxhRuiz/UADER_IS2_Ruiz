# Ejemplo práctico de aplicación de patrón bridge
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Bridge
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Bridge es útil cuando tienes dos dimensiones que pueden cambiar de manera independiente.

En este ejemplo:

pueden aparecer nuevos tipos de notificación,
pueden aparecer nuevos canales de envío,

e impide la necesidad des multiplicar clases.

Sin Bridge, con 3 tipos de notificación y 3 canales habría  hasta 9 clases concretas.
Con Bridge, hay 3 clases de notificación y 3 clases de canal.

Diferencia con Adapter

Aunque ambos patrones usan composición, resuelven problemas distintos.

Adapter sirve para hacer compatible una interfaz existente con otra.

Bridge sirve para evitar una explosión de clases separando abstracción e implementación.
"""
from abc import ABC, abstractmethod


# =========================
# Implementación: canales
# =========================

class CanalEnvio(ABC):
    """Interfaz de implementación para canales de envío."""

    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str) -> None:
        pass


class CanalEmail(CanalEnvio):
    """Canal concreto: email."""

    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[EMAIL] Para: {destinatario}")
        print(f"Mensaje: {mensaje}")


class CanalSMS(CanalEnvio):
    """Canal concreto: SMS."""

    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[SMS] Para: {destinatario}")
        print(f"Mensaje: {mensaje}")


class CanalWhatsApp(CanalEnvio):
    """Canal concreto: WhatsApp."""

    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[WHATSAPP] Para: {destinatario}")
        print(f"Mensaje: {mensaje}")


# =========================
# Abstracción: notificaciones
# =========================

class Notificacion(ABC):
    """
    Abstracción principal.

    Mantiene una referencia al canal de envío, que es la implementación.
    """

    def __init__(self, canal: CanalEnvio) -> None:
        self.canal = canal

    @abstractmethod
    def notificar(self, destinatario: str, mensaje: str) -> None:
        pass


class NotificacionSimple(Notificacion):
    """Notificación común."""

    def notificar(self, destinatario: str, mensaje: str) -> None:
        self.canal.enviar(destinatario, mensaje)


class NotificacionUrgente(Notificacion):
    """Notificación urgente con formato especial."""

    def notificar(self, destinatario: str, mensaje: str) -> None:
        mensaje_urgente = f"URGENTE: {mensaje}"
        self.canal.enviar(destinatario, mensaje_urgente)


class NotificacionPromocional(Notificacion):
    """Notificación promocional."""

    def notificar(self, destinatario: str, mensaje: str) -> None:
        mensaje_promocional = f"PROMOCIÓN: {mensaje}"
        self.canal.enviar(destinatario, mensaje_promocional)


# =========================
# Cliente
# =========================

def main() -> None:
    email = CanalEmail()
    sms = CanalSMS()
    whatsapp = CanalWhatsApp()

    print("=== Notificación simple por email ===")
    notificacion = NotificacionSimple(email)
    notificacion.notificar(
        "cliente@example.com",
        "Su factura ya está disponible."
    )

    print("\n=== Notificación urgente por SMS ===")
    notificacion = NotificacionUrgente(sms)
    notificacion.notificar(
        "+5491123456789",
        "Se detectó un acceso sospechoso a su cuenta."
    )

    print("\n=== Notificación promocional por WhatsApp ===")
    notificacion = NotificacionPromocional(whatsapp)
    notificacion.notificar(
        "+5491123456789",
        "Tiene un 20% de descuento hasta el viernes."
    )


if __name__ == "__main__":
    main()
