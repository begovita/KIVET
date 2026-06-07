from src.modelo.dao.Conexion import Conexion
from src.modelo.vo.MascotaVO import MascotaVO


class MascotaDAO:
    def __init__(self):
        pass

    def obtener_mascotas_por_dni(self, dni):
        # busco todas las mascotas que pertenecen a un dueño
        db = Conexion()
        if db.conexion is None:
            return []

        lista_mascotas = []
        try:
            cursor = db.getCursor()
            sql = "SELECT id_mascota, nombre, especie, dni_dueno FROM MASCOTAS WHERE dni_dueno = ?"
            cursor.execute(sql, (dni,))

            resultados = cursor.fetchall()

            for fila in resultados:
                mascota = MascotaVO(
                    id_mascota=fila[0],
                    nombre=fila[1],
                    especie=fila[2],
                    dni_dueno=fila[3]
                )
                lista_mascotas.append(mascota)

        except Exception as e:
            print(f"Error en MascotaDAO: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return lista_mascotas

    def insertar(self, mascota):
        # guardar una nueva mascota
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            sql = "INSERT INTO MASCOTAS (nombre, especie, dni_dueno) VALUES (?, ?, ?)"
            valores = (
                mascota.get_nombre(),
                mascota.get_especie(),
                mascota.get_dni_dueno()
            )
            cursor.execute(sql, valores)
            exito = True
        except Exception as e:
            print(f"Error al insertar: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito

    def eliminar(self, id_mascota):
        # eliminar a una mascota
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            sql = "DELETE FROM MASCOTAS WHERE id_mascota = ?"
            cursor.execute(sql, (id_mascota,))
            exito = True
        except Exception as e:
            print(f"Error al eliminar: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito

    def modificar(self, id_mascota, nuevo_nombre, nueva_especie):
        # actualizar los datos de una mascota
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            sql = "UPDATE MASCOTAS SET nombre = ?, especie = ? WHERE id_mascota = ?"
            cursor.execute(sql, (nuevo_nombre, nueva_especie, id_mascota))
            exito = True
        except Exception as e:
            print(f"Error al modificar: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito

    def obtener_todas_las_mascotas(self):
        db = Conexion()
        if db.conexion is None:
            return []

        lista_mascotas = []
        try:
            cursor = db.getCursor()
            sql = "SELECT id_mascota, nombre, especie, dni_dueno FROM MASCOTAS"
            cursor.execute(sql)

            for fila in cursor.fetchall():
                from src.modelo.vo.MascotaVO import MascotaVO
                mascota = MascotaVO(
                    id_mascota=fila[0],
                    nombre=fila[1],
                    especie=fila[2],
                    dni_dueno=fila[3]
                )
                lista_mascotas.append(mascota)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return lista_mascotas