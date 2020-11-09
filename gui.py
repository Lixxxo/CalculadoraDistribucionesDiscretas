"""
Implementación de distribuciones.py para escritorio con interfaz grafica
"""
from tkinter import Entry, Label, Button, Tk, StringVar, OptionMenu

from distribuciones import distribuciones, calcular_acumulada
from utils import key_to_list_from_dict, CreateToolTip



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

def pack_results(app, text):
    """
    Subprograma que actualiza el último resultado dado al usuario
    """
    labels = [lb for lb in app.winfo_children() if isinstance(lb, Label)]
    labels[-1].destroy()
    label = Label(app, text = text, font=("sans", "12", "bold"))
    label.pack()
    return

def generar_menu_dist(*args):
    """
    Subprograma que genera los campos correspondientes al tipo de distribución seleccionada por el distribucion_seleccionada.
    """
    try:
        dic = distribuciones[distribucion_seleccionada.get()].dict_params
    except KeyError:
        distribucion_seleccionada.set("Binomial")
        dic = distribuciones["Binomial"].dict_params
    

    # busca los widgets que no se ocupan y los destruye
    flush_widgets(app)

    # genera los widgets necesarios de la distribucion
    for campo in dic.keys():
        if modo_seleccionado.get() == "Acumulada" and campo == "x":
            label = Label(app, text="Inicio",font=("sans", "12", "bold") )
            # agregar un form
            txtfld = Entry(app, text="Inicio")
            txtfld.tag = "inicio"
            tooltip = CreateToolTip(txtfld, text = "x inicial")
            # vincularlos a la app
            label.pack()
            txtfld.pack()

            label = Label(app, text="Fin",font=("sans", "12", "bold") )
            # agregar un form
            txtfld = Entry(app, text="Fin")
            txtfld.tag = "fin"
            tooltip = CreateToolTip(txtfld, text = "x final")
            # vincularlos a la app
            label.pack()
            txtfld.pack()
            continue

        label = Label(app, text=campo,font=("sans", "12", "bold") )
        # agregar un form
        txtfld = Entry(app, text=campo)
        txtfld.tag = campo
        tooltip = CreateToolTip(txtfld, text = dic[campo])
        # vincularlos a la app
        label.pack()
        txtfld.pack()

    button = Button(app, text="Calcular!", command=(lambda e=app.winfo_children(): calcular_distribucion(e)))

    button.pack()
    # texto por defecto para flushear bonito
    txt = '''
Probabilidad: -
Esperanza: -
Varianza: -
'''
    label = Label(app, text=txt, font=("sans", "12", "bold"))
    label.pack()


def calcular_distribucion(widgets):
    """
    Subprograma (invocado onclick) que captura los
    valores de los widgets y calcula la probabilidad
    de la distribución seleccionada
    """
    app.distrib = distribuciones[distribucion_seleccionada.get()]()
    lista = []
    for wid in widgets:
 
        if isinstance(wid, Entry):
            try:
                lista.append(float(wid.get()))
            except ValueError:
                lista.append(0)
    if modo_seleccionado.get() == "Acumulada":     
        inicio = lista.pop(0)
        fin = lista.pop(0)
    probabilidad = 0
    text = ""
    try:
        if modo_seleccionado.get() == "Acumulada":
            probabilidad = str(calcular_acumulada(app.distrib, int(inicio), int(fin), lista))
        else:
            app.distrib.iniciar(lista)
            probabilidad = str(app.distrib.probabilidad())

    except :
        pass

    esperanza = str(app.distrib.esperanza())
    varianza = str(app.distrib.varianza())

    txt = '''
Probabilidad: %s
Esperanza: %s
Varianza: %s
'''%(probabilidad, esperanza, varianza)
    # obtener todas las labels y eliminar la ultima
    pack_results(app, txt)
    pass


app = Tk()
app.title("Amigo de distribuciones")
app.geometry("350x400")
app.resizable(0, 0)
app.distrib = None
distribucion_seleccionada = StringVar(app)
distribucion_seleccionada.set("Selecciona una distibución")

lista_distribuciones = key_to_list_from_dict(distribuciones)

option1 = OptionMenu(app, distribucion_seleccionada, *lista_distribuciones)
option1.pack()
distribucion_seleccionada.trace("w", generar_menu_dist)

modo_seleccionado = StringVar(app)
modo_seleccionado.set("Discreta")

modos = ["Discreta", "Acumulada"]

option2 = OptionMenu(app, modo_seleccionado, *modos )
option2.pack()
modo_seleccionado.trace("w", generar_menu_dist)

app.mainloop()
