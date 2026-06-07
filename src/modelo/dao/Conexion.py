import jaydebeapi
import os

#patron SINGLETON implementado en este fichero

class Conexion:

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Conexion, cls).__new__(cls)
            cls._instancia._inicializada = False
        return cls._instancia

    def __init__(self, host='localhost', database='kivet_db', user='root', password='contraIS'):
        self._host = host
        self._database = database
        self._user = user
        self._password = password
        self.conexion = self.createConnection()
        self._inicializada = True

    def createConnection(self):
        try:
            jdbc_driver = "com.mysql.cj.jdbc.Driver"

            directorio_actual = os.path.dirname(__file__)
            ruta_raiz = os.path.abspath(os.path.join(directorio_actual, "..", "..",".."))
            jar_file = os.path.join(ruta_raiz, "lib", "mysql-connector-j-8.3.0.jar")

            self.conexion = jaydebeapi.connect(
                jdbc_driver,
                f"jdbc:mysql://{self._host}/{self._database}",
                [self._user, self._password],
                jar_file
            )
            return self.conexion
        except Exception as e:
            print("Error creando conexión:", e)
            return None

    def getCursor(self):
        if self.conexion is None:
            self.createConnection()
        return self.conexion.cursor()

    def closeConnection(self):
        try:
            if self.conexion:
                self.conexion.close()
                self.conexion = None
                Conexion._instancia = None #se resetea el singleton al cerrar
        except Exception as e:
            print("Error cerrando la conexion:", e)


if __name__ == "__main__":
    prueba1 = Conexion()
    prueba2 = Conexion()

    if prueba1 is prueba2:
        print("el patron funciona. ambas variables usan la misma conexion")

    if prueba1.conexion:
        prueba1.closeConnection()