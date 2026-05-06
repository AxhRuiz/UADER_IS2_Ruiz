# Ejemplo práctico de aplicación de patrón adapter
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Adapter
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
El patrón Adapter es útil cuando hay que integrar una clase, biblioteca, API o sistema externo
 sin modificar el código cliente existente.

Adapter permite que dos interfaces incompatibles trabajen juntas.
"""
from abc import ABC, abstractmethod


class ProcesadorPago(ABC):
    """Interfaz esperada por la aplicación."""

    @abstractmethod
    def pagar(self, monto: float) -> bool:
        pass


class ProcesadorPagoInterno(ProcesadorPago):
    """Implementación original del sistema."""

    def pagar(self, monto: float) -> bool:
        print(f"Pago interno procesado por ${monto:.2f}")
        return True


class PasarelaExterna:
    """
    Servicio externo que no podemos modificar.

    Su interfaz es incompatible con la que usa nuestra aplicación.
    """

    def realizar_transaccion(self, importe_en_centavos: int, moneda: str) -> dict:
        print(
            f"Transacción externa procesada por "
            f"{importe_en_centavos} centavos en {moneda}"
        )
        return {
            "estado": "aprobada",
            "codigo_autorizacion": "ABC123"
        }


class AdaptadorPasarelaExterna(ProcesadorPago):
    """
    Adapter.

    Convierte la interfaz de PasarelaExterna a la interfaz ProcesadorPago.
    """

    def __init__(self, pasarela: PasarelaExterna) -> None:
        self.pasarela = pasarela

    def pagar(self, monto: float) -> bool:
        importe_en_centavos = int(monto * 100)

        respuesta = self.pasarela.realizar_transaccion(
            importe_en_centavos=importe_en_centavos,
            moneda="ARS"
        )

        return respuesta.get("estado") == "aprobada"


class Caja:
    """
    Cliente del sistema.

    La caja no sabe si usa el procesador interno o uno externo adaptado.
    Solo conoce la interfaz ProcesadorPago.
    """

    def __init__(self, procesador_pago: ProcesadorPago) -> None:
        self.procesador_pago = procesador_pago

    def cobrar(self, monto: float) -> None:
        if self.procesador_pago.pagar(monto):
            print("Cobro realizado correctamente.")
        else:
            print("El cobro fue rechazado.")


def main() -> None:
    print("=== Pago usando procesador interno ===")
    procesador_interno = ProcesadorPagoInterno()
    caja = Caja(procesador_interno)
    caja.cobrar(12500.50)

    print()

    print("=== Pago usando pasarela externa adaptada ===")
    pasarela_externa = PasarelaExterna()
    procesador_adaptado = AdaptadorPasarelaExterna(pasarela_externa)

    caja = Caja(procesador_adaptado)
    caja.cobrar(9800.75)


if __name__ == "__main__":
    main()
