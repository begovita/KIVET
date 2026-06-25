from src.modelo.logica.ServicioInformes import ServicioInformes

class ControladorInformes:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota

        self.servicio = ServicioInformes()

        self.cargar_tabla_informes()

    def cargar_tabla_informes(self):
        informes = self.servicio.obtener_informes_paciente(self.id_mascota)

        self.vista.rellenar_tabla_informes(informes, self.procesar_impresion)

    def procesar_impresion(self, id_informe):
        self.vista.mostrar_mensaje_impresion(id_informe, self.nombre_mascota)