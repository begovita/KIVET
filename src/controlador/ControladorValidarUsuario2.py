from src.modelo.logica.ServicioUsuario import ServicioUsuario

class ControladorValidarUsuario2:
    def __init__(self, vista, dni_admin, dni_a_validar):
        self.vista = vista
        self.dni_admin = dni_admin
        self.dni_a_validar = dni_a_validar
        self.servicio = ServicioUsuario()

        self.vista.mostrar_dni_validando(self.dni_a_validar)

        if hasattr(self.vista, 'btnValidarFinal'):
            self.vista.btnValidarFinal.clicked.connect(self.procesar_validacion)

    def procesar_validacion(self):
        nombre, telefono, rol = self.vista.obtener_datos_validacion()

        if not nombre or not telefono:
            self.vista.mostrar_aviso("Por favor, rellena todos los campos.")
            return

        try:
            self.servicio.validar_y_activar_usuario(self.dni_a_validar, nombre, rol, telefono)

            self.vista.mostrar_exito(f"El usuario {nombre} ha sido validado correctamente como {rol}.")
            self.vista.cerrar_ventana()

        except Exception as e:
            self.vista.mostrar_error(str(e))