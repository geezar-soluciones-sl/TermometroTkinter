from tkinter import *
from tkinter import ttk #Versión antigua themed

# themed da aspecto más profesional

# Creamos la clase mainApp, que hereda del objeto genérico TK
# (que ya es en sí una ventana, por tanto tenemos "subclase" con
# la herencia de todas las propiedades de Tk.
# Podríamos hacerla desde cero bastante sencillamente, pero no hace falta
# Por tanto, creamos objeto tipo Tkinter (una ventana, vamos)
# Generalmente se llama "root"
class mainApp(Tk):
    # Valores iniciales de temperatura (Que irá en un widget entry)
    # y unidades (que irán en un radiobutton)
    entrada = None
    tipoUnidad = None
    
    tamañoVentanaIni = "150x150"
    tituloVentanaIni = "Termometro Tkinter"
    colorVentanaIni = "#DED789"
    

    
    def __init__(self):
        # Constructor de Tk, clase padre (estamos heredando)
        Tk.__init__(self)
        
        # Vamos definiendo la ventana, el tamaño en un string...
        self.geometry(self.tamañoVentanaIni)
        self.title(self.tituloVentanaIni)
        self.configure(bg = self.colorVentanaIni)
        # Que no cambie de tamaño
        self.resizable(0,0)
    
        #StringVar es un objeto al que se pueden asociar eventos
        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value = "C")    
        
        self.crearDiseño()
        
    def crearDiseño(self):
        # Creamos los widgets entry, la etiqueta y el radiobutton.
        # Ponemos self porque es de quien dependen (quien las contiene)
                
        # Tkinter tiene tres formas de poner geometria:
        # Rejilla, place (en un sitio y/o tamaño concretos)
        # o pack (hace una pila en vertical de widgets)
        # y pone  posición (TOP u otro), rellenar, separadores, etc.)
        
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10,y=10)
        
        # Ponemos la etiqueta 
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10,y=40)
        
        # Ponemos el radiobutton del tipo de unidad
        # Definimos los dos primero. Saldrá ya seleccionado el que hemos puesto antes en tipoUnidad
        self.rbF = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F").place(x=20, y=80)
        self.rbC = ttk.Radiobutton(self, text="Celsius   ", variable=self.tipoUnidad, value="C").place(x=20, y=110)
        # Y asociamos los dos botones
        
        
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
    
