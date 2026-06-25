from src.modelo.dao.CitaDAO import CitaDAO
from src.modelo.vo.CitaVO import CitaVO

class ServicioCitas:
    def __init__(self):
        self.dao_citas = CitaDAO()

    def obtener_citas_dia(self, fecha_str):
        return self.dao_citas.obtener_citas_por_fecha(fecha_str)

    def obtener_telefono(self, id_cita):
        return self.dao_citas.obtener_telefono_por_cita(id_cita)

    def modificar_cita_paciente(self, id_cita, nueva_fecha, nueva_hora):
        exito = self.dao_citas.modificar_cita(id_cita, nueva_fecha, nueva_hora)
        if not exito:
            raise Exception("No se pudo actualizar la cita en la base de datos.")

    def agendar_cita(self, fecha, hora, motivo, id_mascota):
        nueva_cita = CitaVO(fecha, hora, motivo, id_mascota)

        exito = self.dao_citas.insertar(nueva_cita)
        if not exito:
            raise Exception("No se pudo guardar la cita.")