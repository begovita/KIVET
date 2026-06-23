from src.modelo.dao.MascotaDAO import MascotaDAO
from src.modelo.vo.MascotaVO import MascotaVO


class ServicioMascota:
    def __init__(self):
        self.dao = MascotaDAO()

    def obtener_lista_mascotas(self):
        return self.dao.obtener_todas_las_mascotas()

    def anadir_mascota(self, nombre, especie, dni_dueno):
        # El servicio empaqueta los datos
        nueva_mascota = MascotaVO(nombre, especie, dni_dueno)

        exito = self.dao.insertar(nueva_mascota)
        if not exito:
            raise Exception("No se pudo guardar la mascota en la base de datos.")