from src.modelo.dao.FacturaDAO import FacturaDAO
import subprocess

class ServicioAdmin:
    def __init__(self):
        self.dao_facturas = FacturaDAO()

    def calcular_facturacion_mensual(self):
        return self.dao_facturas.obtener_total_facturado_mes_actual()

    def ejecutar_backup(self, ruta):
        comando = [r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe", "-h", "localhost", "-u", "root", "-pcontraIS", "kivet_db"]
        with open(ruta, "w") as archivo:
            subprocess.run(comando, stdout=archivo, check=True)

    def ejecutar_restore(self, ruta):
        comando = [r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe", "-h", "localhost", "-u", "root", "-pcontraIS", "kivet_db"]
        with open(ruta, "r") as archivo:
            subprocess.run(comando, stdin=archivo, check=True)