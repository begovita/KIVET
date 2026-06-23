import os
import shutil
from src.modelo.dao.InformeDAO import InformeDAO

class ServicioInformes:
    def __init__(self):
        self.dao_informes = InformeDAO()

    def obtener_informes_paciente(self, id_mascota):
        return self.dao_informes.obtener_por_mascota(id_mascota)

    def guardar_informe_completo(self, tipo, id_mascota, ruta_origen):
        directorio_actual = os.path.dirname(__file__)
        carpeta_informes = os.path.join(directorio_actual, "..", "informes_guardados")
        os.makedirs(carpeta_informes, exist_ok=True)

        nombre_archivo = os.path.basename(ruta_origen)
        nombre_final = f"mascota_{id_mascota}_{nombre_archivo}"
        ruta_destino_final = os.path.join(carpeta_informes, nombre_final)

        shutil.copy(ruta_origen, ruta_destino_final)

        exito = self.dao_informes.insertar_informe(tipo, id_mascota, ruta_destino_final)
        if not exito:
            raise Exception("Problema al guardar el enlace en la base de datos.")