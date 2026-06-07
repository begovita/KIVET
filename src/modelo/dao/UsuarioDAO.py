from src.modelo.dao.Conexion import Conexion
from src.modelo.vo.UsuarioVO import UsuarioVO


class UsuarioDAO:
    def __init__(self):
        pass

    def insertar(self, usuario):
        # insertar nuevo usuario en la bbdd
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            sql = "INSERT INTO USUARIOS (dni, contrasena, nombre, rol, estado) VALUES (?, ?, ?, ?, ?)"
            valores = (
                usuario.get_dni(),
                usuario.get_contrasena(),
                usuario.get_nombre(),
                usuario.get_rol(),
                usuario.get_estado()
            )

            cursor.execute(sql, valores)
            print(f"Usuario {usuario.get_nombre()} guardado en la base de datos.")
            exito = True
        except Exception as e:
            print(f"Error en UsuarioDAO al insertar: {e}")
        finally:
            # cierro el cursor y la conexion cuando termino
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito

    def validar_credenciales(self, dni, contrasena):
        # compruebo si el usuario existe y su rol
        db = Conexion()
        if db.conexion is None:
            return None

        rol_usuario = None
        try:
            cursor = db.getCursor()

            sql = "SELECT estado, rol FROM USUARIOS WHERE dni = ? AND contrasena = ?"
            valores = (dni, contrasena)

            cursor.execute(sql, valores)
            resultado = cursor.fetchone()

            if resultado:
                estado = resultado[0]
                rol = resultado[1]
                if estado in ["Validado"]:
                    print(f"Acceso concedido. Rol detectado: {rol}")
                    rol_usuario = rol
                elif estado == "Pendiente":
                    print("Acceso denegado: Cuenta pendiente de validación.")
                elif estado == "Bloqueado":
                    print("Acceso denegado: Cuenta bloqueada.")
            else:
                print("Acceso denegado: DNI o contraseña incorrectos.")

        except Exception as e:
            print(f"Error en UsuarioDAO al validar: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        # si va mal devuelve None, sino el rol del usuario
        return rol_usuario

    def obtener_usuarios_pendientes(self):
        from src.modelo.dao.Conexion import Conexion
        db = Conexion()
        if db.conexion is None:
            return []

        lista_pendientes = []
        try:
            cursor = db.getCursor()
            # solo cogemos a los que estan en estado Pendiente
            sql = "SELECT dni, nombre, rol FROM USUARIOS WHERE estado = 'Pendiente'"
            cursor.execute(sql)

            for fila in cursor.fetchall():
                usuario = {
                    "dni": fila[0],
                    "nombre": fila[1],
                    "rol": fila[2]
                }
                lista_pendientes.append(usuario)
        except Exception as e:
            print(f"Error al obtener usuarios pendientes: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return lista_pendientes

    def finalizar_validacion(self, dni, nombre, rol, telefono):
        from src.modelo.dao.Conexion import Conexion
        db = Conexion()
        if db.conexion is None:
            return False

        exito = False
        try:
            cursor = db.getCursor()
            # estado Validado
            sql = """
                UPDATE USUARIOS 
                SET nombre = ?, rol = ?, estado = 'Validado', telefono = ? 
                WHERE dni = ?
            """
            cursor.execute(sql, (nombre, rol, telefono, dni))
            exito = True
        except Exception as e:
            print(f"Error al finalizar validación: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            db.closeConnection()

        return exito


# prueba
if __name__ == "__main__":
    #para crear un nuevos usuarios de prueba
    '''
    nuevo_usuario = UsuarioVO(
        dni="06620936H",
        contrasena="bego1234",
        nombre="Begoña Vita",
        rol="Dueno",
        estado="Validado"
    )
    '''

    '''
    nuevo_usuario = UsuarioVO(
        dni = "11111111A",
        contrasena = "admin",
        nombre = "Martín Martín",
        rol = "Administrativo",
        estado = "Validado"
    )
    '''

    nuevo_usuario = UsuarioVO(
        dni = '22222222B',
        contrasena = "vete",
        nombre = "Doctora Juguetes",
        rol = "Veterinario",
        estado = "Validado"
    )

    dao = UsuarioDAO()

    print("\n prueba 1 insertar en la base de datos")
    dao.insertar(nuevo_usuario)
