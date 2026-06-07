from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox
from src.modelo.dao.FacturaDAO import FacturaDAO


class ControladorFacturas:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.dao = FacturaDAO()

        self.cargar_tabla_facturas()

    def cargar_tabla_facturas(self):
        facturas = self.dao.obtener_por_mascota(self.id_mascota)

        self.vista.tablaFacturas.setRowCount(0)
        self.vista.tablaFacturas.setColumnCount(4)
        self.vista.tablaFacturas.setHorizontalHeaderLabels(["Nº Factura", "Fecha", "Importe", "Acción"])

        for fila_idx, fac in enumerate(facturas):
            self.vista.tablaFacturas.insertRow(fila_idx)

            self.vista.tablaFacturas.setItem(fila_idx, 0, QTableWidgetItem(str(fac.get_id_factura())))
            self.vista.tablaFacturas.setItem(fila_idx, 1, QTableWidgetItem(fac.get_fecha()))
            self.vista.tablaFacturas.setItem(fila_idx, 2, QTableWidgetItem(f"{fac.get_importe()} €"))

            # boton imprimir
            btn_imprimir = QPushButton("Imprimir Factura")
            id_actual = fac.get_id_factura()
            importe_actual = fac.get_importe()

            btn_imprimir.clicked.connect(
                lambda checked, id_fac=id_actual, imp=importe_actual: self.ejecutar_impresion(id_fac, imp))

            self.vista.tablaFacturas.setCellWidget(fila_idx, 3, btn_imprimir)

    def ejecutar_impresion(self, id_factura, importe):
        QMessageBox.information(
            self.vista,
            "Impresora KiVet",
            f"Conectando con la impresora.\n\nLa factura #{id_factura} de {self.nombre_mascota} se ha mandado a imprimir."
        )