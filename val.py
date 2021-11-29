import re
from tkinter.constants import FALSE, TRUE


def validar(cad):
    patron = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
    try:
        print("------------------")
        print(cad)
        re.match(patron, cad)
        if re.match(patron, cad):
            return TRUE
        else:
            return FALSE
    except:
        return FALSE
