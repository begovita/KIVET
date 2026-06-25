from src.modelo.logica.ServicioUsuario import ServicioUsuario
from src.vista.VistaValidarUsuario2 import VistaValidarUsuario2

class ControladorValidarUsuario:
    def __init__(self, vista, dni_admin):
        self.vista = vista
        self.dni_admin = dni_admin
        self.servicio = ServicioUsuario()

        self.cargar_tabla_pendientes()

        if hasattr(self.vista, 'btnSeleccionarUsuario'):
            self.vista.btnSeleccionarUsuario.clicked.connect(self.abrir_formulario_validacion)

    def cargar_tabla_pendientes(self):
        try:
            usuarios = self.servicio.obtener_pendientes()
            self.vista.rellenar_tabla_pendientes(usuarios)
        except Exception as e:
            print(f"Error al cargar la tabla de pendientes: {e}")

    def abrir_formulario_validacion(self):
        fila = self.vista.obtener_fila_seleccionada()

        if fila == -1:
            self.vista.mostrar_aviso("Por favor, selecciona un usuario.")
            return

        dni_usuario_a_validar = self.vista.obtener_dni_fila(fila)

        self.vista_final = VistaValidarUsuario2(self.dni_admin, dni_usuario_a_validar)
        self.vista_final.show()