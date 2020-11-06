"""
Colección de metodos de utilidad para las implementaciones
"""
from tkinter import *
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


def key_to_list_from_dict(dictionary):
    """
    Obtiene una lista compuesta por las claves del diccionario recibido
    """
    return [key for key in dictionary.keys()]

