from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.UsuarioDAO import UsuarioDAO

class ControladorValidarUsuario2:
    def __init__(self, vista, dni_admin, dni_a_validar):
        self.vista = vista
        self.dni_admin = dni_admin
        self.dni_a_validar = dni_a_validar
        self.dao_usuarios = UsuarioDAO()

        if hasattr(self.vista, 'lblDniUsuario'):
            self.vista.lblDniUsuario.setText(f"Validando usuario: {self.dni_a_validar}")

        if hasattr(self.vista, 'btnValidarFinal'):
            self.vista.btnValidarFinal.clicked.connect(self.validar_y_activar)

    def validar_y_activar(self):
        nombre = self.vista.txtNombre.text()
        telefono = self.vista.txtTelefono.text()
        rol = self.vista.cboRol.currentText()

        if not nombre or not telefono:
            QMessageBox.warning(self.vista, "Aviso", "Por favor, rellena todos los campos.")
            return

        exito = self.dao_usuarios.finalizar_validacion(self.dni_a_validar, nombre, rol, telefono)

        if exito:
            QMessageBox.information(self.vista, "Éxito", f"El usuario {nombre} ha sido validado correctamente como {rol}.")
            self.vista.close()
        else:
            QMessageBox.critical(self.vista, "Error", "No se pudo activar la cuenta.")