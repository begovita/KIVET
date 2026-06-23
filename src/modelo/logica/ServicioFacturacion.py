import os
import shutil
from src.modelo.dao.FacturaDAO import FacturaDAO
from src.modelo.dao.CitaDAO import CitaDAO

class ServicioFacturacion:
    def __init__(self):
        self.dao_facturas = FacturaDAO()
        self.dao_citas = CitaDAO()

    def obtener_facturas_paciente(self, id_mascota):
        return self.dao_facturas.obtener_por_mascota(id_mascota)

    def obtener_citas_paciente(self, id_mascota):
        return self.dao_citas.obtener_citas_por_mascota(id_mascota)

    def guardar_factura_completa(self, id_cita, importe, ruta_origen):
        directorio_actual = os.path.dirname(__file__)
        carpeta = os.path.join(directorio_actual, "..", "facturas_guardadas")
        os.makedirs(carpeta, exist_ok=True)

        nombre_archivo = os.path.basename(ruta_origen)
        nombre_final = f"cita_{id_cita}_{nombre_archivo}"
        ruta_destino = os.path.join(carpeta, nombre_final)

        shutil.copy(ruta_origen, ruta_destino)

        exito = self.dao_facturas.insertar_factura(id_cita, importe, ruta_destino)
        if not exito:
            raise Exception("No se pudo insertar la factura en la base de datos.")