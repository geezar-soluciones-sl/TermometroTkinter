from tkinter import *
from tkinter import ttk #Versión antigua themed

# themed da aspecto más profesional

# Creamos la clase mainApp, que hereda del objeto genérico TK
# (que ya es en sí una vetnana, por tanto tenemos "subclase" con
# la herencia de todas las propiedades de Tk.
# Podríamos hacerla desde cero bastante sencillamente, pero no hace falta
# Por tanto, creamos objeto tipo Tkinter (una ventana, vamos)
# Generalmente se llama "root"
class mainApp(Tk):
    tamañoVentana = "640x480"
    tituloVentana = "Mi ventana"
    colorVentana = "blue"
    
    
    def __init__(self):
        # Constructor de Tk (estamos heredando)
        Tk.__init__(self)
        
        # Vamos definiendo la ventana, el tamaño en un string...
        self.geometry(self.tamañoVentana)
        self.title(self.tituloVentana)
        self.configure(bg = self.colorVentana)

    def arrancar(self):
        # Hay que decirle que empiece a funcionar y se pinte
        # PALABRA LOOP en Tkinter: ESTÁ ESPERANDO EVENTOS
        # Parecido al bucle principal de pygame
        # Los controles visuales se llaman "widgets":
        # (radiobutton, button, entry, etc.)
        # TKINTER deja que Windows controle la ventana (estándar)    

        self.mainloop()

if __name__ == "__main__":
    app = mainApp()
    app.arrancar()
    
