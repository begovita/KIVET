from src.modelo.dao.Conexion import Conexion

class CitaDAO:
    def __init__(self):
        pass

    def insertar(self, cita):
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            # Asumimos que id_cita es autoincremental
            sql = "INSERT INTO CITAS (fecha, hora, motivo, id_mascota) VALUES (?, ?, ?, ?)"
            valores = (
                cita.get_fecha(),
                cita.get_hora(),
                cita.get_motivo(),
                cita.get_id_mascota()
            )
            cursor.execute(sql, valores)
            exito = True
        except Exception as e:
            print(f"Error en CitaDAO al insertar: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito

    def obtener_citas_por_fecha(self, fecha_seleccionada):
        db = Conexion()
        if db.conexion is None:
            return []

        lista_citas = []
        try:
            cursor = db.getCursor()
            # INNER JOIN para unir citas y mascotas, y sacar el nombre de la mascota
            sql = """
                SELECT c.id_cita, c.hora, m.nombre, c.motivo 
                FROM CITAS c
                INNER JOIN MASCOTAS m ON c.id_mascota = m.id_mascota
                WHERE c.fecha = ?
                ORDER BY c.hora ASC
            """
            cursor.execute(sql, (fecha_seleccionada,))

            for fila in cursor.fetchall():
                cita = {
                    "id_cita": fila[0],
                    "hora": str(fila[1]),
                    "nombre_mascota": fila[2],
                    "motivo": fila[3]
                }
                lista_citas.append(cita)

        except Exception as e:
            print(f"Error al obtener citas por fecha: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return lista_citas

    def modificar_cita(self, id_cita, nueva_fecha, nueva_hora):
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            # actualizar fecha y hora de la cita
            sql = "UPDATE CITAS SET fecha = ?, hora = ? WHERE id_cita = ?"
            cursor.execute(sql, (nueva_fecha, nueva_hora, id_cita))
            exito = True
        except Exception as e:
            print(f"Error al modificar cita: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito

    def obtener_telefono_por_cita(self, id_cita):
        from src.modelo.dao.Conexion import Conexion
        db = Conexion()
        if db.conexion is None:
            return "Desconocido"

        telefono = "Desconocido"
        try:
            cursor = db.getCursor()
            # tripe INNER JOIN para enlazar cita con mascota, y despues mascota con dueño
            sql = """
                SELECT u.telefono 
                FROM CITAS c
                INNER JOIN MASCOTAS m ON c.id_mascota = m.id_mascota
                INNER JOIN USUARIOS u ON m.dni_dueno = u.dni
                WHERE c.id_cita = ?
            """
            cursor.execute(sql, (id_cita,))
            resultado = cursor.fetchone()

            if resultado and resultado[0]:
                telefono = str(resultado[0])

        except Exception as e:
            print(f"Error al obtener teléfono: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return telefono

    def obtener_citas_por_mascota(self, id_mascota):
        from src.modelo.dao.Conexion import Conexion
        from src.modelo.vo.CitaVO import CitaVO

        db = Conexion()
        if db.conexion is None:
            return []

        lista_citas = []
        try:
            cursor = db.getCursor()
            # Buscamos todas las citas de este animal específico
            sql = "SELECT id_cita, fecha, hora, motivo, id_mascota FROM CITAS WHERE id_mascota = ?"
            cursor.execute(sql, (id_mascota,))

            for fila in cursor.fetchall():
                # Importante: Asegúrate de que tu CitaVO acepte id_cita.
                # Si tu CitaVO tiene los parámetros en otro orden, ajústalos aquí.
                cita = CitaVO(
                    id_cita=fila[0],
                    fecha=str(fila[1]),
                    hora=str(fila[2]),
                    motivo=fila[3],
                    id_mascota=fila[4]
                )
                lista_citas.append(cita)

        except Exception as e:
            print(f"Error al obtener citas por mascota: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return lista_citas