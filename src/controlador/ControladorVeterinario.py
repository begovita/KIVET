from src.vista.VistaAnadirInformes import VistaAnadirInformes
from src.vista.VistaGestionarCitas import VistaGestionarCitas


class ControladorVeterinario:
    def __init__(self, vista, dni_veterinario):
        self.vista = vista
        self.dni_veterinario = dni_veterinario

        self.conectar_botones()

    def conectar_botones(self):
        if hasattr(self.vista, 'btnAnadirInformes'):
            self.vista.btnAnadirInformes.clicked.connect(self.abrir_flujo_informes)

        if hasattr(self.vista, 'btnGestionarCitas'):
            self.vista.btnGestionarCitas.clicked.connect(self.abrir_flujo_citas)

    def abrir_flujo_informes(self):
        self.vista_buscador = VistaAnadirInformes()
        self.vista_buscador.show()

    def abrir_flujo_citas(self):
        self.vista_agenda = VistaGestionarCitas()
        self.vista_agenda.show()