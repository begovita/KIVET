from PyQt5.QtWidgets import QMessageBox
from src.modelo.vo.CitaVO import CitaVO
from src.modelo.dao.CitaDAO import CitaDAO


class ControladorPedirCita:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.dao = CitaDAO()

        # pongo las horas manualmente porque no sabia como hacerlo desde qtdesigner
        if hasattr(self.vista, 'inputHora'):
            self.vista.inputHora.clear()
            horas_clinica = [
                "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
                "12:00", "12:30", "13:00", "16:00", "16:30", "17:00",
                "17:30", "18:00", "18:30", "19:00", "19:30"
            ]
            self.vista.inputHora.addItems(horas_clinica)

        if hasattr(self.vista, 'btnGuardarCita'):
            self.vista.btnGuardarCita.clicked.connect(self.guardar_cita)

    def guardar_cita(self):
        # me guardo los datos
        fecha = self.vista.inputFecha.date().toString("yyyy-MM-dd")
        hora = self.vista.inputHora.currentText()
        motivo = self.vista.inputMotivo.text().strip()

        # verificacicon
        if not hora:
            QMessageBox.warning(self.vista, "Aviso", "Por favor, selecciona una hora para la cita.")
            return

        # empaquetar y guardar en la bbdd
        nueva_cita = CitaVO(fecha, hora, motivo, self.id_mascota)
        if self.dao.insertar(nueva_cita):
            QMessageBox.information(self.vista, "Éxito", f"Cita guardada correctamente para {self.nombre_mascota} el día {fecha} a las {hora}.")
            self.vista.hide()
        else:
            QMessageBox.critical(self.vista, "Error de Inserción", "No se pudo guardar la cita.")