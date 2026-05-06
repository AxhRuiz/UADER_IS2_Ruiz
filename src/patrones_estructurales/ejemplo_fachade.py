# Ejemplo práctico de aplicación de patrón fachade
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Fachade
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Facade es útil cuando se desea  simplificar el uso de un sistema complejo, puede
verse también como una forma de aumentar la "cohesión"

Casos típicos:

	procesos de compra
	inicialización de aplicaciones
	acceso a servicios externos
	pipelines de procesamiento de datos
	compilación, validación y despliegue
	integración de varios módulos heredados

Facade no reemplaza los subsistemas. Los organiza detrás de una interfaz más simple.
Facade oculta complejidad operativa detrás de una API sencilla.
"""
class Inventario:
    """Subsistema encargado de verificar y reservar stock."""

    def verificar_stock(self, producto: str, cantidad: int) -> bool:
        print(f"[Inventario] Verificando stock de {cantidad} x {producto}")
        return cantidad <= 5

    def reservar(self, producto: str, cantidad: int) -> None:
        print(f"[Inventario] Reservando {cantidad} x {producto}")


class Pagos:
    """Subsistema encargado del cobro."""

    def cobrar(self, cliente: str, monto: float) -> bool:
        print(f"[Pagos] Cobrando ${monto:.2f} a {cliente}")
        return True


class Facturacion:
    """Subsistema encargado de emitir la factura."""

    def emitir_factura(self, cliente: str, producto: str, monto: float) -> str:
        numero_factura = "FAC-0001"
        print(f"[Facturación] Emitiendo factura {numero_factura}")
        return numero_factura


class Envios:
    """Subsistema encargado de preparar el envío."""

    def preparar_envio(self, cliente: str, producto: str, cantidad: int) -> str:
        codigo_seguimiento = "ENV-12345"
        print(f"[Envíos] Preparando envío para {cliente}")
        print(f"[Envíos] Producto: {producto}, cantidad: {cantidad}")
        return codigo_seguimiento


class CompraOnlineFacade:
    """
    Facade.

    Ofrece una interfaz simple para una operación compleja
    que involucra varios subsistemas.
    """

    def __init__(self) -> None:
        self.inventario = Inventario()
        self.pagos = Pagos()
        self.facturacion = Facturacion()
        self.envios = Envios()

    def comprar(
        self,
        cliente: str,
        producto: str,
        cantidad: int,
        precio_unitario: float,
    ) -> None:
        print("Iniciando proceso de compra...\n")

        hay_stock = self.inventario.verificar_stock(producto, cantidad)
        if not hay_stock:
            print("Compra rechazada: no hay stock suficiente.")
            return

        self.inventario.reservar(producto, cantidad)

        monto_total = cantidad * precio_unitario
        pago_aprobado = self.pagos.cobrar(cliente, monto_total)

        if not pago_aprobado:
            print("Compra rechazada: el pago fue rechazado.")
            return

        factura = self.facturacion.emitir_factura(
            cliente,
            producto,
            monto_total,
        )

        seguimiento = self.envios.preparar_envio(
            cliente,
            producto,
            cantidad,
        )

        print("\nCompra completada correctamente.")
        print(f"Factura: {factura}")
        print(f"Código de seguimiento: {seguimiento}")


def main() -> None:
    tienda = CompraOnlineFacade()

    tienda.comprar(
        cliente="María Gómez",
        producto="Notebook",
        cantidad=2,
        precio_unitario=850000.00,
    )


if __name__ == "__main__":
    main()
