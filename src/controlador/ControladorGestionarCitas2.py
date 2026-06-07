from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.CitaDAO import CitaDAO

class ControladorGestionarCitas2:
    def __init__(self, vista, id_cita, nombre_mascota):
        self.vista = vista
        self.id_cita = id_cita
        self.nombre_mascota = nombre_mascota
        self.dao_citas = CitaDAO()

        self.preparar_interfaz()

        if hasattr(self.vista, 'btnGuardarCambios'):
            self.vista.btnGuardarCambios.clicked.connect(self.ejecutar_cambio)

    def preparar_interfaz(self):
        if hasattr(self.vista, 'lblTitulo'):
            self.vista.lblTitulo.setText(f"Modificar Cita de {self.nombre_mascota}")

        if hasattr(self.vista, 'cboNuevaHora'):
            horas_disponibles = [
                "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
                "12:00", "12:30", "13:00", "16:00", "16:30", "17:00",
                "17:30", "18:00", "18:30", "19:00", "19:30"
            ]
            self.vista.cboNuevaHora.addItems(horas_disponibles)

        # advertencia para avisar al dueño
        telefono_dueno = self.dao_citas.obtener_telefono_por_cita(self.id_cita)
        if hasattr(self.vista, 'lblAdvertencia'):
            self.vista.lblAdvertencia.setText(
                f"IMPORTANTE Debes llamar al dueño al teléfono {telefono_dueno} para confirmar el cambio."
            )

    def ejecutar_cambio(self):
        nueva_fecha = self.vista.calendarNueva.selectedDate().toString("yyyy-MM-dd")
        nueva_hora = self.vista.cboNuevaHora.currentText()

        exito = self.dao_citas.modificar_cita(self.id_cita, nueva_fecha, nueva_hora)

        if exito:

            telefono = self.dao_citas.obtener_telefono_por_cita(self.id_cita)
            QMessageBox.information(
                self.vista,
                "Cita Actualizada",
                f"La cita ha sido cambiada al día {nueva_fecha} a las {nueva_hora}.\n\n"
                f"RECUERDA: Llama ahora al {telefono} para informar del cambio."
            )
            self.vista.close()
        else:
            QMessageBox.critical(self.vista, "Error", "No se pudo actualizar la cita.")