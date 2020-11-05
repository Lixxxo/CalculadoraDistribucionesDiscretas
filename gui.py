"""
Implementación de distribuciones.py para escritorio con interfaz grafica
"""
from tkinter import *

from distribuciones import distribuciones
from utils import key_to_list_from_dict
from random import randint


def flush_widgets(frame):
    """
    Subprograma que destruye todos los widgets de tipo {Label},{Entry} y {Button} de una {Frame} llamada {frame}
    """
    for widget in frame.winfo_children():
        if isinstance(widget, Entry) or isinstance(widget, Label) or isinstance(widget, Button):
            widget.destroy()
            pass
        pass
    pass


def generar_menu_dist(*args):
    """
    Subprograma que genera los campos correspondientes al tipo de distribución seleccionada por el selector.
    """
    # distribuciones["Binomial"].init(x,n,p)
    # distribuciones["Binomial"].probabilidad()

    # distribuciones["Binomial"](x, n, p).probabilidad()
    # distribuciones[selector].dict_params
    #cada dist tiene cant != de params
    #definir una variable comun para esa cant
    #es variable es len(dict_params) que cada dist tiene
    #para asignar los campos, lo estamos 
    # haciendo de forma temporal (usando una instancia)
    #lo que yo prongo es que usemos las distribuciones de forma estatica
    # asginando sus params en su clase respectiva

    dic = distribuciones[selector.get()].dict_params
    

    # busca los widgets que no se ocupan y los destruye
    flush_widgets(app)

    # genera los widgets necesarios de la distribucion
    for campo in dic:
        label = Label(app, text=campo)
        # agregar un form
        txtfld = Entry(app, text=campo)
        txtfld.tag = campo
        # vincularlos a la app
        label.pack()
        txtfld.pack()
    button = Button(app, text="Calcular!",command=(lambda e=app.winfo_children(): calcular_distribucion(e)))
    button.pack()


# TODO: corregir apropiadamente el metodo
def calcular_distribucion(widgets):
    """
    Subprograma (invocado onclick) que captura los
    valores de los widgets y calcula la probabilidad
    de la distribución seleccionada
    """
    app.distrib = distribuciones[selector.get()]()
    lista = []
    for wid in widgets:
        if isinstance(wid, Entry):
            lista.append(float(wid.get()))

    app.distrib.iniciar(lista)
    print(app.distrib)
    # set label probabilidad
    pass


app = Tk()
app.title("Amigo de distribuciones")
app.geometry("300x600")
app.distrib = None
selector = StringVar(app)
selector.set("Selecciona una distibución")

opciones = key_to_list_from_dict(distribuciones)

w = OptionMenu(app, selector, *opciones)
w.pack()

selector.trace("w", generar_menu_dist)

app.mainloop()
