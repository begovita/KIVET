import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorGestionarCitas2 import ControladorGestionarCitas2

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaGestionarCitas2.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaGestionarCitas2(QMainWindow, Form):
    def __init__(self, id_cita, nombre_mascota):
        super().__init__()
        self.setupUi(self)
        self.id_cita = id_cita
        self.nombre_mascota = nombre_mascota

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorGestionarCitas2(self, self.id_cita, self.nombre_mascota)

    def actualizar_titulo(self, nombre_mascota):
        self.lblTitulo.setText(f"Modificar Cita de {nombre_mascota}")

    def cargar_horas_disponibles(self):
        horas_disponibles = [
            "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
            "12:00", "12:30", "13:00", "16:00", "16:30", "17:00",
            "17:30", "18:00", "18:30", "19:00", "19:30"
        ]
        self.cboNuevaHora.addItems(horas_disponibles)

    def mostrar_advertencia_telefono(self, telefono):
        self.lblAdvertencia.setText(
            f"IMPORTANTE: Debes llamar al dueño al teléfono {telefono} para confirmar el cambio."
        )

    def obtener_nueva_fecha(self):
        return self.calendarNueva.selectedDate().toString("yyyy-MM-dd")

    def obtener_nueva_hora(self):
        return self.cboNuevaHora.currentText()

    def mostrar_exito(self, titulo, mensaje):
        QMessageBox.information(self, titulo, mensaje)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def cerrar_ventana(self):
        self.close()