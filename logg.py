##################################################################
# LOGG.PY --------------------------------------------------
# Clase log_ingreso que manega la lectura y escritura en archivo
# local log.txt
##################################################################

from os import path
from datetime import date, datetime

# CLASS log_ingreso
class log_ingreso():
    """
    Clase para el manejo de un archivo de texto en la carpeta local
    que por medio de los metodos registrar y leer_registo se pueden
    ver y grabar eventos en el archivo log.txt
    """
    ruta = path.dirname(path.abspath(__file__)) + "/log.txt"

    # print("La ruta es:", ruta)

    def __init__(self) -> None:
        pass

    def registrar(self, accion, usuario="User"):
        log = open(self.ruta, 'a')
        print(
            datetime.now().strftime("%c:"),
            "ACCION:",
            # print(datetime.now().strftime("%x-%X:"), "Se ha detectado:",
            accion,
            "de la persona:",
            usuario,
            file=log)

    def leer_registro(self):
        log = open(self.ruta, 'r')
        print("Lo que se ha grabado en el registro de Acceso es:\n")
        # print(log.read())
        return log.read()

    def registrar_mas_datos(self, dato1="", dato2="", dato3=""):
        log = open(self.ruta, 'a')
        print("Registro Afectado: ", dato1, ", ", dato2, ", ", dato3, file=log)

    def get_path(self):
        return self.ruta
