"""
Implementación de distribuciones.py para escritorio con interfaz grafica
"""
from tkinter import *

from distribuciones import distribuciones
from utils import key_to_list_from_dict


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
    
    button = Button(app, text="Calcular!",command=(lambda e = app.winfo_children(): calcular_distribucion(e)))

    button.pack()
    # texto por defecto para flushear bonito
    txt = '''
Probabilidad: -
Esperanza: -
Varianza: -
'''  
    label = Label(app, text = txt)
    label.pack()


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
            try:
                lista.append(float(wid.get()))
            except ValueError:
                lista.append(0)
            
    try:
        app.distrib.iniciar(lista)
    except :
        pass
    
    # print(app.distrib)

    # obtener todas las labels y eliminar la ultima
    labels = [lb for lb in app.winfo_children() if isinstance(lb, Label)]
    labels[-1].destroy()
    label = Label(app, text = app.distrib)
    label.pack()
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
