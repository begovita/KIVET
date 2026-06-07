from src.modelo.dao.Conexion import Conexion
from src.modelo.vo.FacturaVO import FacturaVO


class FacturaDAO:
    def obtener_por_mascota(self, id_mascota):
        db = Conexion()
        if db.conexion is None:
            return []

        lista_facturas = []
        try:
            cursor = db.getCursor()
            # hago un INNER JOIN de facturas con citas para filtrar por el id_mascota
            sql = """
                SELECT f.id_factura, f.importe, f.fecha, f.id_cita 
                FROM FACTURAS f
                INNER JOIN CITAS c ON f.id_cita = c.id_cita
                WHERE c.id_mascota = ?
            """
            cursor.execute(sql, (id_mascota,))

            for fila in cursor.fetchall():
                factura = FacturaVO(
                    id_factura=fila[0],
                    importe=fila[1],
                    fecha=str(fila[2]) if fila[2] else "Sin fecha",
                    id_cita=fila[3]
                )
                lista_facturas.append(factura)

        except Exception as e:
            print(f"Error en FacturaDAO: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return lista_facturas

    def insertar_factura(self, id_cita, importe, archivo_pdf):
        from src.modelo.dao.Conexion import Conexion
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            sql = "INSERT INTO FACTURAS (id_cita, importe, fecha, archivo_pdf) VALUES (?, ?, CURDATE(), ?)"
            cursor.execute(sql, (id_cita, importe, archivo_pdf))
            exito = True
        except Exception as e:
            print(f"Error al insertar factura: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito

    def obtener_total_facturado_mes_actual(self):
        db = Conexion()
        if db.conexion is None:
            return 0.0

        total = 0.0
        try:
            cursor = db.getCursor()
            # importe total filtrado por  mes y año
            sql = """
                SELECT SUM(importe) 
                FROM FACTURAS 
                WHERE MONTH(fecha) = MONTH(CURDATE()) 
                  AND YEAR(fecha) = YEAR(CURDATE())
            """
            cursor.execute(sql)
            resultado = cursor.fetchone()

            if resultado and resultado[0] is not None:
                total = float(resultado[0])

        except Exception as e:
            print(f"Error al calcular la facturación del mes: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return total