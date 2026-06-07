from src.modelo.dao.Conexion import Conexion
from src.modelo.vo.InformeVO import InformeVO


class InformeDAO:
    def obtener_por_mascota(self, id_mascota):
        db = Conexion()
        if db.conexion is None:
            return []

        lista_informes = []
        try:
            cursor = db.getCursor()

            # busco en todos los documentos por el id_mascota
            sql = "SELECT id_documento, tipo_documento, id_mascota, fecha, descripcion FROM DOCUMENTOS WHERE id_mascota = ?"
            cursor.execute(sql, (id_mascota,))

            for fila in cursor.fetchall():
                informe = InformeVO(
                    id_documento=fila[0],
                    tipo_documento=fila[1],
                    id_mascota=fila[2],
                    fecha=str(fila[3]) if fila[3] else "Sin fecha",
                    descripcion=fila[4] if fila[4] else "Sin descripción"
                )
                lista_informes.append(informe)

        except Exception as e:
            print(f"Error en InformeDAO: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return lista_informes

    def insertar_informe(self, tipo_documento, id_mascota, descripcion):
        from src.modelo.dao.Conexion import Conexion
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            sql = "INSERT INTO DOCUMENTOS (tipo_documento, id_mascota, fecha, descripcion) VALUES (?, ?, CURDATE(), ?)"
            cursor.execute(sql, (tipo_documento, id_mascota, descripcion))
            exito = True
        except Exception as e:
            print(f"Error al insertar informe: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito