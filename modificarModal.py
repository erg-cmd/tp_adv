from tkinter import *
from modificar import *
from base_datos import *
from controlador import log_socios


def log_registro_modificar(obj):
    def interior(*args, **kwargs):
        obj(*args, **kwargs)
        variables = args[0]
        lista = []
        for variable in variables:
            lista.append(variable.get())
        log_socios.registrar("modificado", lista[0])
        log_socios.registrar_mas_datos(lista[0],lista[1],lista[2])

    return interior


def show(variables, popupModificar):
    popupModificar.destroy()
    imprimir(variables)
    print(type(variables))


@log_registro_modificar
def modifica(variables, popupModificar, elobjeto):
    popupModificar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    actualizar = tabla_producto.update(
        titulo=lista[1],
        descripcion=lista[2]).where(tabla_producto.id == lista[0])
    actualizar.execute()

    elobjeto.mostrar()


def modificar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupModificar = Toplevel()
    vars_modificar = CrearFormModificar(popupModificar, campos)
    print(vars_modificar)
    Button(
        popupModificar,
        text="OK",
        command=(lambda: show(vars_modificar, popupModificar)),
    ).pack()
    Button(
        popupModificar,
        text="modificar",
        command=(lambda: modifica(vars_modificar, popupModificar, objeto)),
    ).pack()

    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()
