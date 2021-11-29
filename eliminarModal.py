from tkinter import *
from eliminar import *
from base_datos import *
from controlador import log_socios


def log_registro_eliminar(obj):
    def interior(*args, **kwargs):
        variables = args[0]
        lista = []
        for variable in variables:
            lista.append(variable.get())
        log_socios.registrar("eliminado", lista[0])
        # log_socios.registrar_mas_datos(lista[0], lista[1])
        obj(*args, **kwargs)

    return interior


def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


@log_registro_eliminar
def elimina(variables, popupEliminar, elobjeto):
    popupEliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())

    borrar = tabla_producto.get(tabla_producto.id == lista[0])
    borrar.delete_instance()

    elobjeto.mostrar()


def eliminar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupEliminar = Toplevel()
    vars_eliminar = CrearFormEliminar(popupEliminar, campos)
    Button(popupEliminar,
           text="OK",
           command=(lambda: show(vars_eliminar, popupEliminar))).pack()
    Button(
        popupEliminar,
        text="eliminar",
        command=(lambda: elimina(vars_eliminar, popupEliminar, objeto)),
    ).pack()

    popupEliminar.grab_set()
    popupEliminar.focus_set()
    popupEliminar.wait_window()
