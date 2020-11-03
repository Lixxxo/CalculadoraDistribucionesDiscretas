from tkinter import *

from distribuciones import distribuciones


def generar_option_menu(dictionary):
    arr = []

    for key in dictionary.keys():
        arr.append(key)

    return arr

def generar_menu_dist(*args):
    for campo in distribuciones[selector.get()].dict_parametros():
        #agregar una etiqueta
        #agregar un form
        #vincularlos a la app
        pass


    probabilidad = distribuciones[selector.get()]()



## def capturar valores en forms
# asignarlos a la distibucion correspondiente
# 


app = Tk()
app.title("Amigo de distribuciones")

selector = StringVar(app)
selector.set("Selecciona una distibución")

opciones = generar_option_menu(distribuciones)
w = OptionMenu(app, selector, *opciones)
w.pack()
