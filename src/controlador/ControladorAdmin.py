import subprocess
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from src.modelo.dao.FacturaDAO import FacturaDAO
from src.vista.VistaAnadirFactura import VistaAnadirFactura
from src.vista.VistaValidarUsuario import VistaValidarUsuario

class ControladorAdmin:
    def __init__(self, vista, dni_admin):
        self.vista = vista
        self.dni_admin = dni_admin
        self.dao_facturas = FacturaDAO()

        self.conectar_botones()

    def conectar_botones(self):
        if hasattr(self.vista, 'btnValidarCuentas'):
            self.vista.btnValidarCuentas.clicked.connect(self.abrir_flujo_validar)

        if hasattr(self.vista, 'btnAnadirFacturas'):
            self.vista.btnAnadirFacturas.clicked.connect(self.abrir_flujo_facturas)

        if hasattr(self.vista, 'btnTotalFacturadoMes'):
            self.vista.btnTotalFacturadoMes.clicked.connect(self.mostrar_total_facturado_mes)

        if hasattr(self.vista, 'btnCopiaSeguridad'):
            self.vista.btnCopiaSeguridad.clicked.connect(self.hacer_copia_seguridad)

        if hasattr(self.vista, 'btnRestaurarCopia'):
            self.vista.btnRestaurarCopia.clicked.connect(self.restaurar_copia)

    def mostrar_total_facturado_mes(self):
        try:
            total = self.dao_facturas.obtener_total_facturado_mes_actual()

            QMessageBox.information(
                self.vista,
                "Facturación Mensual",
                f"El dinero total facturado durante este mes en KiVet es:\n\n {total:.2f} €"
            )
        except Exception as e:
            QMessageBox.critical(
                self.vista,
                "Error",
                "Ocurrió un error al calcular la facturación del mes."
            )

    def abrir_flujo_validar(self):
        self.vista_validar = VistaValidarUsuario(self.dni_admin)
        self.vista_validar.show()

    def abrir_flujo_facturas(self):
        self.vista_anadir_facturas = VistaAnadirFactura(self.dni_admin)
        self.vista_anadir_facturas.show()

    def hacer_copia_seguridad(self):
        ruta_archivo, _ = QFileDialog.getSaveFileName(
            self.vista,
            "Guardar Copia de Seguridad",
            "Copia_KiVet_Backup.sql",
            "Archivos SQL (*.sql);;Todos los archivos (*.*)"
        )

        if not ruta_archivo:
            return

        comando = [
            r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe",
            "-h", "localhost",
            "-u", "root",
            "-pcontraIS",
            "kivet_db"
        ]

        try:
            with open(ruta_archivo, "w") as archivo_salida:
                subprocess.run(comando, stdout=archivo_salida, check=True)

            QMessageBox.information(
                self.vista,
                "Copia Exitosa",
                f"La base de datos se ha respaldado correctamente en:\n{ruta_archivo}"
            )

        except FileNotFoundError:
            QMessageBox.critical(
                self.vista,
                "Error Crítico",
                "No se encuentra la herramienta 'mysqldump'."
            )
        except Exception as e:
            QMessageBox.critical(self.vista, "Error", f"No se pudo realizar la copia:\n{e}")

    def restaurar_copia(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            self.vista,
            "Seleccionar Copia de Seguridad",
            "",
            "Archivos SQL (*.sql);;Todos los archivos (*.*)"
        )

        if not ruta_archivo:
            return

        respuesta = QMessageBox.question(
            self.vista,
            "Confirmación de Restauración",
            "ATENCIÓN: Al restaurar esta copia, se sobrescribirán todos los datos actuales de KiVet.\n\n¿Estás seguro de que deseas continuar?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if respuesta == QMessageBox.No:
            return

        comando = [
            r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe",
            "-h", "localhost",
            "-u", "root",
            "-pcontraIS",
            "kivet_db"
        ]

        try:
            with open(ruta_archivo, "r") as archivo_entrada:
                subprocess.run(comando, stdin=archivo_entrada, check=True)

            QMessageBox.information(
                self.vista,
                "Restauración Exitosa",
                "La base de datos ha vuelto al estado de la copia de seguridad correctamente."
            )

        except FileNotFoundError:
            QMessageBox.critical(
                self.vista,
                "Error Crítico",
                "No se encuentra la herramienta 'mysql'."
            )
        except Exception as e:
            QMessageBox.critical(self.vista, "Error", f"No se pudo restaurar la copia:\n{e}")