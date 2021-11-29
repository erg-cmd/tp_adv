from tkinter import *
from guardar import *
from base_datos import *
from controlador import log_socios


def log_registro_guardar(obj):
    def interior(*args, **kwargs):
        obj(*args, **kwargs)
        variables = args[0]
        lista = []
        for variable in variables:
            lista.append(variable.get())
        log_socios.registrar("guardado", lista[0])
        log_socios.registrar_mas_datos(lista[0], lista[1])

    return interior


def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


@log_registro_guardar
def guarda(variables, popupGuardar, elobjeto):

    popupGuardar.destroy()
    print("guardar------------")
    lista = []
    for variable in variables:
        lista.append(variable.get())
    producto = tabla_producto()
    producto.titulo = lista[0]
    producto.descripcion = lista[1]
    producto.save()
    elobjeto.mostrar()


def guardar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)

    Button(popupGuardar,
           text="OK",
           command=(lambda: show(vars_guardar, popupGuardar))).pack()
    Button(
        popupGuardar,
        text="guardar",
        command=(lambda: guarda(vars_guardar, popupGuardar, objeto)),
    ).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()