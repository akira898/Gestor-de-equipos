class text:
    def __init__(self,contenido,idioma):
        self.contenido=contenido
        self.idioma=idioma
from tkinter import ttk
import tkinter as tkin
from mirarTextos import checkFile
Idioma=["Spanish","Engish"]
spanish="hola!"
english="hello!"
def DebugTextos():
    objeto_text = text(contenido="Hola Mundo", idioma="Spanish")
    #crea la ventana para la herramienta
    VentanaDeTextos=tkin.Tk()
    VentanaDeTextos.title("herramienta para ver los diferentes textos")
    VentanaDeTextos.geometry("200x100")
    ts = tkin.StringVar()
    def seleccionar(event):
            print(ts.get())
            objeto_text.idioma=ts.get()
            checkFile(objeto_text.idioma)
    #crea los elemntos de la interfaz
    selectorDeIdioma=ttk.Combobox(VentanaDeTextos,textvariable=ts,values=Idioma)
    selectorDeIdioma.pack(pady=5)
    selectorDeIdioma.bind("<<ComboboxSelected>>", seleccionar)
    VentanaDeTextos.mainloop()
DebugTextos()

