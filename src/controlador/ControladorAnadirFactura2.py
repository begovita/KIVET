import os
import shutil
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog
from src.modelo.dao.FacturaDAO import FacturaDAO
from src.modelo.dao.CitaDAO import CitaDAO

class ControladorAnadirFactura2:
    def __init__(self, vista, dni_admin, id_mascota, nombre_mascota):
        self.vista = vista
        self.dni_admin = dni_admin
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota

        self.dao_facturas = FacturaDAO()
        self.dao_citas = CitaDAO()

        self.ruta_archivo_seleccionado = None

        self.preparar_interfaz()

        if hasattr(self.vista, 'btnSeleccionarArchivo'):
            self.vista.btnSeleccionarArchivo.clicked.connect(self.abrir_explorador)

        if hasattr(self.vista, 'btnSubirFactura'):
            self.vista.btnSubirFactura.clicked.connect(self.guardar_factura)

    def preparar_interfaz(self):
        if hasattr(self.vista, 'lblTitulo'):
            self.vista.lblTitulo.setText(f"Historial de Facturación: {self.nombre_mascota}")

        self.cargar_tabla_facturas()
        self.cargar_desplegable_citas()

    def cargar_tabla_facturas(self):
        try:
            facturas = self.dao_facturas.obtener_por_mascota(self.id_mascota)
            self.vista.tablaFacturas.setRowCount(0)
            self.vista.tablaFacturas.setColumnCount(4)
            self.vista.tablaFacturas.setHorizontalHeaderLabels(["ID Factura", "ID Cita", "Fecha", "Importe (€)"])

            for fila_idx, f in enumerate(facturas):
                self.vista.tablaFacturas.insertRow(fila_idx)
                self.vista.tablaFacturas.setItem(fila_idx, 0, QTableWidgetItem(str(f.get_id_factura())))
                self.vista.tablaFacturas.setItem(fila_idx, 1, QTableWidgetItem(str(f.get_id_cita())))
                self.vista.tablaFacturas.setItem(fila_idx, 2, QTableWidgetItem(str(f.get_fecha())))
                self.vista.tablaFacturas.setItem(fila_idx, 3, QTableWidgetItem(f"{f.get_importe()} €"))
        except Exception as e:
            print(f"Error al cargar facturas: {e}")

    def cargar_desplegable_citas(self):
        # Necesitas una función en CitaDAO que devuelva las citas de un animal
        # Si no la tienes, simplemente devuelve un par de IDs falsos por ahora para probar
        citas_pendientes = self.dao_citas.obtener_citas_por_mascota(self.id_mascota)
        self.vista.cboCita.clear()

        for cita in citas_pendientes:
            # Mostramos el ID y la fecha para que el admin sepa qué cobra
            texto_opcion = f"Cita {cita.get_id_cita()} - {cita.get_fecha()}"
            # Guardamos el id_cita puro en los "datos ocultos" del combobox
            self.vista.cboCita.addItem(texto_opcion, cita.get_id_cita())

    def abrir_explorador(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self.vista,
            "Seleccionar Factura",
            "",
            "Archivos PDF (*.pdf);;Todos los archivos (*.*)"
        )
        if ruta:
            self.ruta_archivo_seleccionado = ruta
            self.vista.lblRuta.setText(ruta)

    def guardar_factura(self):
        if not self.ruta_archivo_seleccionado:
            QMessageBox.warning(self.vista, "Aviso", "Selecciona un archivo PDF.")
            return

        importe_str = self.vista.txtImporte.text().replace(',', '.')

        try:
            importe = float(importe_str)
        except ValueError:
            QMessageBox.warning(self.vista, "Aviso", "El importe debe ser un número válido.")
            return

        # Sacamos el ID de la cita que está guardado de forma oculta en el combobox
        id_cita_seleccionada = self.vista.cboCita.currentData()
        if id_cita_seleccionada is None:
            QMessageBox.warning(self.vista, "Aviso", "No hay citas seleccionadas.")
            return

        # COPIA DE SEGURIDAD DEL PDF
        directorio_actual = os.path.dirname(__file__)
        carpeta = os.path.join(directorio_actual, "..", "facturas_guardadas")
        os.makedirs(carpeta, exist_ok=True)

        nombre_archivo = os.path.basename(self.ruta_archivo_seleccionado)
        nombre_final = f"cita_{id_cita_seleccionada}_{nombre_archivo}"
        ruta_destino = os.path.join(carpeta, nombre_final)

        try:
            shutil.copy(self.ruta_archivo_seleccionado, ruta_destino)
        except Exception as e:
            QMessageBox.critical(self.vista, "Error", f"Fallo al copiar PDF: {e}")
            return

        # GUARDAR EN BASE DE DATOS
        if self.dao_facturas.insertar_factura(id_cita_seleccionada, importe, ruta_destino):
            QMessageBox.information(self.vista, "Éxito", "Factura procesada correctamente.")
            self.ruta_archivo_seleccionado = None
            self.vista.lblRuta.setText("(Ningún archivo seleccionado)")
            self.vista.txtImporte.clear()
            self.cargar_tabla_facturas()
        else:
            QMessageBox.critical(self.vista, "Error", "Error al guardar en base de datos.")