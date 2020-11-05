"""
Implementación de distribuciones.py para escritorio con interfaz grafica
"""
from tkinter import Entry, Label, Button, Tk, StringVar, OptionMenu

from distribuciones import distribuciones
from utils import key_to_list_from_dict

class CreateToolTip(object):
    '''
    Create a tooltip for a given widget
    '''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background='light green', relief='solid', borderwidth=1,
                       font=("sans", "12", "bold"))
        label.pack(ipadx=1)
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()


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

def pack_results(app):
    """
    Subprograma que actualiza el último resultado dado al usuario
    """
    labels = [lb for lb in app.winfo_children() if isinstance(lb, Label)]
    labels[-1].destroy()
    label = Label(app, text = app.distrib, font=("sans", "12", "bold"))
    label.pack()
    return

def generar_menu_dist(*args):
    """
    Subprograma que genera los campos correspondientes al tipo de distribución seleccionada por el selector.
    """

    dic = distribuciones[selector.get()].dict_params

    # busca los widgets que no se ocupan y los destruye
    flush_widgets(app)

    # genera los widgets necesarios de la distribucion
    for campo in dic.keys():
        label = Label(app, text=campo,font=("sans", "12", "bold") )
        # agregar un form
        txtfld = Entry(app, text=campo)
        txtfld.tag = campo
        tooltip = CreateToolTip(txtfld, text= dic[campo])
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
    
    # obtener todas las labels y eliminar la ultima
    pack_results(app)
    pass


app = Tk()
app.title("Amigo de distribuciones")
app.geometry("350x400")
app.resizable(0, 0)
app.distrib = None
selector = StringVar(app)
selector.set("Selecciona una distibución")

opciones = key_to_list_from_dict(distribuciones)

w = OptionMenu(app, selector, *opciones, )
w.pack()

selector.trace("w", generar_menu_dist)

app.mainloop()
