from src.modelo.logica.ServicioUsuario import ServicioUsuario
from src.vista.MenuPpal import MenuPpal


class ControladorLogin:
    def __init__(self, vista):
        self.vista = vista
        self.servicio = ServicioUsuario()

        # vincular los botones a las funciones
        self.vista.botonAceptar.clicked.connect(self.procesar_login)
        self.vista.botonRegistrarse.clicked.connect(self.procesar_registro)

    def procesar_login(self):
        dni, contrasena = self.vista.obtener_credenciales_login()

        if not dni or not contrasena:
            self.vista.mostrar_aviso("Campos vacíos", "Por favor, introduce DNI y contraseña.")
            return

        rol_obtenido = self.servicio.validar_login(dni, contrasena)

        if rol_obtenido:
            self.vista.mostrar_exito("Éxito", f"Acceso concedido. Entrando como: {rol_obtenido}")

            self.vista_menu = MenuPpal(dni, rol_obtenido)
            self.vista_menu.show()
            self.vista.ocultar_ventana()
        else:
            self.vista.mostrar_error("Error de acceso", "DNI incorrecto, contraseña inválida o cuenta pendiente.")

    def procesar_registro(self):
        dni, contrasena = self.vista.obtener_datos_registro()

        if not dni or not contrasena:
            self.vista.mostrar_aviso("Campos vacíos", "Rellena todos los campos para registrarte.")
            return

        try:
            self.servicio.registrar_nuevo_usuario(dni, contrasena)
            self.vista.mostrar_exito("Registro completado", "Usuario registrado correctamente.")
            self.vista.limpiar_formulario_registro()
        except Exception as e:
            self.vista.mostrar_aviso("Error en el registro", str(e))