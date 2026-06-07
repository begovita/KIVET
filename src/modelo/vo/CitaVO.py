class CitaVO:
    def __init__(self, fecha, hora, motivo, id_mascota, id_cita=None):
        self._id_cita = id_cita
        self._fecha = fecha
        self._hora = hora
        self._motivo = motivo
        self._id_mascota = id_mascota

    # getters
    def get_id_cita(self): return self._id_cita
    def get_fecha(self): return self._fecha
    def get_hora(self): return self._hora
    def get_motivo(self): return self._motivo
    def get_id_mascota(self): return self._id_mascota

    # setters
    def set_id_cita(self, id_cita): self._id_cita = id_cita
    def set_fecha(self, fecha): self._fecha = fecha
    def set_hora(self, hora): self._hora = hora
    def set_motivo(self, motivo): self._motivo = motivo
    def set_id_mascota(self, id_mascota): self._id_mascota = id_mascota