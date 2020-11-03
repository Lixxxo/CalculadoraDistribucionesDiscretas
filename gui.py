from tkinter import *

from distribuciones import distribuciones


def generar_option_menu(dictionary):
    arr = []

    for key in dictionary.keys():
        arr.append(key)

    return arr


app = Tk()
app.title("Amigo de distribuciones")

opcion_defecto = StringVar(app)
opcion_defecto.set("Selecciona una distibución")

opciones = generar_option_menu(distribuciones)
w = OptionMenu(app, opcion_defecto, *opciones)

w.pack()
mainloop()

pass
