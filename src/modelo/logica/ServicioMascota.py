from src.modelo.dao.MascotaDAO import MascotaDAO
from src.modelo.vo.MascotaVO import MascotaVO


class ServicioMascota:
    def __init__(self):
        self.dao = MascotaDAO()

    def obtener_lista_mascotas(self):
        return self.dao.obtener_todas_las_mascotas()

    def anadir_mascota(self, nombre, especie, dni_dueno):
        nueva_mascota = MascotaVO(nombre, especie, dni_dueno)

        exito = self.dao.insertar(nueva_mascota)
        if not exito:
            raise Exception("No se pudo guardar la mascota en la base de datos.")

    def eliminar_mascota(self, id_mascota):
        exito = self.dao.eliminar(id_mascota)
        if not exito:
            raise Exception("No se pudo eliminar la mascota de la base de datos.")

    def obtener_mascotas_dueno(self, dni):
        return self.dao.obtener_mascotas_por_dni(dni)

    def modificar_mascota(self, id_mascota, nuevo_nombre, nueva_especie):
        exito = self.dao.modificar(id_mascota, nuevo_nombre, nueva_especie)
        if not exito:
            raise Exception("No se pudo modificar la mascota en la base de datos.")