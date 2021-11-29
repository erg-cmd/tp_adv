##################################################################
# VISTA.PY --------------------------------------------------
# Vista de nuestra app que esta hecha en Tkinter
##################################################################

import os
import subprocess
import sys
import threading
from typing_extensions import final
from pathlib import Path
from logg import *
from tkinter import *
from tkinter.messagebox import *
from base_datos import *
from tkinter import ttk
import val
from temas.OpcionTemas import EleccionTema
from guardarModal import *
from eliminarModal import *
from modificarModal import *
from controlador import log_socios

# VARIABLES GLOBALES
subproc_server = ""


class Producto():
    """
    La vista de nuestra applicacion, hecho en Tkinter, se lanza
    desde controlador.py. Aqui tenemos los metodos para iniciar
    el demonio del servidor socket
    """
    path_raiz = ""
    path_server = ""

    def __init__(self, window):

        # Ventana principal
        self.root = window
        self.root.title("Tarea POO")

        titulo = Label(
            self.root,
            text="Ingrese sus datos",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=60,
        )
        titulo.grid(row=0,
                    column=0,
                    columnspan=4,
                    padx=1,
                    pady=1,
                    sticky=W + E)

        Label(self.root, text="Título").grid(row=1, column=0, sticky=W)
        Label(self.root, text="Descripción").grid(row=2, column=0, sticky=W)

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val = StringVar(), StringVar()
        w_ancho = 20

        self.entrada_nombre = Entry(self.root,
                                    textvariable=self.a_val,
                                    width=w_ancho)
        self.entrada_nombre.grid(row=1, column=1)
        self.entrada_descripcion = Entry(self.root,
                                         textvariable=self.b_val,
                                         width=w_ancho)
        self.entrada_descripcion.grid(row=2, column=1)

        self.tree = ttk.Treeview(height=10, columns=3)
        self.tree["columns"] = ("one", "three")
        self.tree.grid(row=7, column=0, columnspan=3)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("one", text="Título", anchor=CENTER)
        self.tree.heading("three", text="Descripción", anchor=CENTER)

        # Boton Agregar Producto
        ttk.Button(
            self.root,
            text="Mostrar registros existentes",
            command=lambda: self.mostrar(),
        ).grid(row=5, columnspan=3, sticky=W + E)

        Button(self.root, text="Alta",
               command=lambda: self.alta()).grid(row=6, column=1)

        Button(self.root,
               text="Guardar",
               command=lambda: self.pasarObjetoGuardar()).grid(row=11,
                                                               column=0)
        Button(self.root,
               text="Eliminar",
               command=lambda: self.pasarObjetoEliminar()).grid(row=11,
                                                                column=1)
        Button(self.root,
               text="Modificar",
               command=lambda: self.pasarObjetoModificar()).grid(row=11,
                                                                 column=2)

        # ######################################################
        # TEMAS

        self.temas_opciones = Frame(self.root,
                                    bg="red",
                                    borderwidth=2,
                                    relief=RAISED)
        self.temas_opciones.grid(row=12,
                                 column=0,
                                 columnspan=4,
                                 padx=1,
                                 pady=1,
                                 sticky=W + E)

        ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        # Agrego variables de control para eleccion de tema
        self.tema_option = IntVar(value=0)

        Label(
            self.temas_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Temas",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(
                self.temas_opciones,
                text=str(opcion),
                indicatoron=1,
                value=int(opcion[-1]) - 1,
                variable=self.tema_option,
                bg="#222",
                fg="OrangeRed",
                command=self.bg_fg_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

    def pasarObjetoGuardar(self, ):
        print(self)
        guardar(self)

    def pasarObjetoEliminar(self, ):
        print(self)
        eliminar(self)

    def pasarObjetoModificar(self, ):
        print(self)
        modificar(self)

    def bg_fg_option(self):
        print(self.tema_option.get())
        print(EleccionTema(self.tema_option.get()))
        self.temas_opciones["bg"] = EleccionTema(self.tema_option.get())
        self.root["bg"] = EleccionTema(self.tema_option.get())

    ######################################################
    ################# FIN DE TEMAS #######################
    ######################################################

    # obteniendo los productos

    def mostrar(self):
        """
        Actualiza/ muestra los items de la base de datos
        """
        # limpieza de tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Consiguiendo datos
        resultado = tabla_producto.select().order_by(tabla_producto.id.desc())

        # esta conectada?
        func_db_conectar()

        for fila in resultado:
            print(fila.titulo)
            self.tree.insert("",
                             0,
                             text=fila.id,
                             values=(fila.titulo, fila.descripcion))

    def alta(self):
        """
        Se realiza la carga del nuevo producto previa comprobacion por regex
        """
        print("Nueva alta de datos")
        # obtenemos la cadena del campo de texto
        cadena = self.a_val.get()
        if val.validar(cadena):
            tabla_producto.create(titulo=self.a_val.get(),
                                  descripcion=self.b_val.get())
            # Productos.save()
            log_socios.registrar("Alta", self.a_val.get())
            log_socios.registrar_mas_datos(self.a_val.get(), self.b_val.get())
            showinfo("Validado", "El registro se ha agregado correctamente")
        else:
            showinfo(
                "No Validado",
                """El campo de título no cumple los requisitos,ingrese datos alfabéticos""",
            )
        self.mostrar()

    def demonio_server(self):
        # 1 Lanzar el thread para el socketserver
        global subproc_server
        if subproc_server != "":
            subproc_server.kill()
            threading.Thread(target=self.lanzar_server,
                             args=(True, ),
                             daemon=True).start()
        else:
            threading.Thread(target=self.lanzar_server,
                             args=(True, ),
                             daemon=True).start()

    def lanzar_server(self, obj0):
        global subproc_server

        # 1 tenemos que iniciar el socket
        try:
            self.path_raiz = Path(__file__).resolve().parent
            self.path_server = self.path_raiz.joinpath("socket_serv.py")
            print("raiz", self.path_server)
            subproc_server = subprocess.Popen(
                [sys.executable, self.path_server])
            subproc_server.communicate()
        except:
            print("Error dentro de ", __name__)


if __name__ == "__main__":
    try:
        window = Tk()
        application = Producto(window)

        # iniciamos la base de datos
        func_db_iniciar()
        application.mostrar()
        window.mainloop()
    except:
        showerror("Error al Iniciar", "Contacte a Linux")
    finally:
        # cerramos la base de datos
        func_db_desconectar()
        print("\n Base de datos desconectada\n")
# EOF
