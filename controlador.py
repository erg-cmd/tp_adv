##################################################################
# CONTROLADOR.PY --------------------------------------------------
# Desde este fichero lanzamos la app, consta de la vista de nuestra
# app, el inicio, detencion de nuestra base de datos en sqlite y
# una vez declarada la vista lanzamos el demonio del socketserver
##################################################################


from tkinter import *
from tkinter.messagebox import *
from base_datos import *
from vista import *
from socket_serv import MyTCPHandler
from tkinter import ttk
import val
from temas.OpcionTemas import EleccionTema

#variable global
log_socios = log_ingreso()

if __name__ == "__main__":
    try:
        window = Tk()
        application = Producto(window)

        # iniciamos la base de datos
        func_db_iniciar()
        # Se inicia el Thread para iniciar el servidor
        application.demonio_server()
        application.mostrar()
        window.mainloop()
    except:
        showerror("Error al Iniciar", "Contacte a Linux")
    finally:
        # cerramos la base de datos
        func_db_desconectar()
        print("\n Base de datos desconectada\n")
