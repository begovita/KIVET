from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from src.modelo.dao.UsuarioDAO import UsuarioDAO
from src.vista.VistaValidarUsuario2 import VistaValidarUsuario2


class ControladorValidarUsuario:
    def __init__(self, vista, dni_admin):
        self.vista = vista
        self.dni_admin = dni_admin
        self.dao_usuarios = UsuarioDAO()

        self.cargar_tabla_pendientes()

        if hasattr(self.vista, 'btnSeleccionarUsuario'):
            self.vista.btnSeleccionarUsuario.clicked.connect(self.abrir_formulario_validacion)

    def cargar_tabla_pendientes(self):
        try:
            usuarios = self.dao_usuarios.obtener_usuarios_pendientes()
            self.vista.tablaUsuariosPendientes.setRowCount(0)
            self.vista.tablaUsuariosPendientes.setColumnCount(3)
            self.vista.tablaUsuariosPendientes.setHorizontalHeaderLabels(["DNI", "Nombre", "Rol Solicitado"])

            for fila_idx, user in enumerate(usuarios):
                self.vista.tablaUsuariosPendientes.insertRow(fila_idx)
                self.vista.tablaUsuariosPendientes.setItem(fila_idx, 0, QTableWidgetItem(user["dni"]))
                self.vista.tablaUsuariosPendientes.setItem(fila_idx, 1, QTableWidgetItem(user["nombre"]))
                self.vista.tablaUsuariosPendientes.setItem(fila_idx, 2, QTableWidgetItem(user["rol"]))
        except Exception as e:
            print(f"Error al cargar la tabla de pendientes: {e}")

    def abrir_formulario_validacion(self):
        fila_seleccionada = self.vista.tablaUsuariosPendientes.currentRow()

        if fila_seleccionada == -1:
            QMessageBox.warning(self.vista, "Aviso", "Por favor, selecciona un usuario.")
            return

        dni_usuario_a_validar = self.vista.tablaUsuariosPendientes.item(fila_seleccionada, 0).text()

        self.vista_final = VistaValidarUsuario2(self.dni_admin, dni_usuario_a_validar)
        self.vista_final.show()