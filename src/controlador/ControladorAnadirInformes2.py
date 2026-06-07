import os
import shutil
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog
from src.modelo.dao.InformeDAO import InformeDAO


class ControladorAnadirInformes2:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.dao_informes = InformeDAO()

        self.ruta_archivo_seleccionado = None  # Aquí guardaremos la ruta temporalmente

        self.preparar_interfaz()

        # botones
        if hasattr(self.vista, 'btnSeleccionarArchivo'):
            self.vista.btnSeleccionarArchivo.clicked.connect(self.abrir_explorador_archivos)

        if hasattr(self.vista, 'btnSubirInforme'):
            self.vista.btnSubirInforme.clicked.connect(self.guardar_nuevo_informe)

    def preparar_interfaz(self):
        if hasattr(self.vista, 'lblTitulo'):
            self.vista.lblTitulo.setText(f"Historial clínico de {self.nombre_mascota}")
        self.cargar_tabla_historial()

    def cargar_tabla_historial(self):
        try:
            informes = self.dao_informes.obtener_por_mascota(self.id_mascota)
            self.vista.tablaInformesVet.setRowCount(0)
            self.vista.tablaInformesVet.setColumnCount(3)

            self.vista.tablaInformesVet.setHorizontalHeaderLabels(["Fecha", "Tipo", "Archivo Adjunto"])

            for fila_idx, info in enumerate(informes):
                self.vista.tablaInformesVet.insertRow(fila_idx)

                self.vista.tablaInformesVet.setItem(fila_idx, 0, QTableWidgetItem(str(info.get_fecha())))
                self.vista.tablaInformesVet.setItem(fila_idx, 1, QTableWidgetItem(info.get_tipo_documento()))
                self.vista.tablaInformesVet.setItem(fila_idx, 2, QTableWidgetItem(info.get_descripcion()))

        except Exception as e:
            print(f"Error al cargar informes: {e}")

    def abrir_explorador_archivos(self):
        # se abre windows para seleccionar un pdf
        ruta, _ = QFileDialog.getOpenFileName(
            self.vista,
            "Seleccionar Informe Clínico",
            "",
            "Archivos PDF (*.pdf);;Todos los archivos (*.*)"
        )

        if ruta:
            self.ruta_archivo_seleccionado = ruta
            self.vista.lblRuta.setText(ruta)  # mostrar la ruta del archivo

    def guardar_nuevo_informe(self):
        if not self.ruta_archivo_seleccionado:
            QMessageBox.warning(self.vista, "Aviso", "Por favor, selecciona un archivo PDF primero.")
            return

        tipo = self.vista.cboTipo.currentText()

        # preparar carpeta segura en el proyecto
        directorio_actual = os.path.dirname(__file__)
        carpeta_informes = os.path.join(directorio_actual, "..", "informes_guardados")
        os.makedirs(carpeta_informes, exist_ok=True) # crea la carpeta si no existe

        # se copia ahi el archivo
        nombre_archivo = os.path.basename(self.ruta_archivo_seleccionado)
        # añadir id de la mascota (para evitar duplicados)
        nombre_final = f"mascota_{self.id_mascota}_{nombre_archivo}"
        ruta_destino_final = os.path.join(carpeta_informes, nombre_final)

        try:
            shutil.copy(self.ruta_archivo_seleccionado, ruta_destino_final)
        except Exception as e:
            QMessageBox.critical(self.vista, "Error", f"No se pudo copiar el archivo: {e}")
            return

        # se guadra la ruta en la bbdd
        exito = self.dao_informes.insertar_informe(tipo, self.id_mascota, ruta_destino_final)

        if exito:
            QMessageBox.information(self.vista, "Éxito", "El informe clínico se ha subido correctamente.")
            self.ruta_archivo_seleccionado = None
            self.vista.lblRuta.setText("(Ningún archivo seleccionado)")
            self.cargar_tabla_historial()
        else:
            QMessageBox.critical(self.vista, "Error", "Problema al guardar el enlace en la base de datos.")