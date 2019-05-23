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
        
        # El método trace hace un seguimiento. Puede valer w,r,u (escribir, ller o borrar)
        # En ese caso, llamamos al método y hacemos lo que corresponda
        self.temperatura.trace("w", self.validarTemperatura)
        
        self.tipoUnidad = StringVar(value = "C")
        
        #en el caso de radiobutton,
        # el trace se hace con un método de radiobutton que es "command"
        # Por tato, en vez de validar aquí lo hacemos en crearDiseño()
        
        
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
        # Poniendo lo de selected, al pinchar irá allí y hará lo que digamos
        self.rbF = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=20, y=80)
        self.rbC = ttk.Radiobutton(self, text="Celsius   ", variable=self.tipoUnidad, value="C", command=self.selected).place(x=20, y=110)
        # Y asociamos los dos botones
        
        
    def arrancar(self):
        # Hay que decirle que empiece a funcionar y se pinte
        # PALABRA LOOP en Tkinter: ESTÁ ESPERANDO EVENTOS
        # Parecido al bucle principal de pygame
        # Los controles visuales se llaman "widgets":
        # (radiobutton, button, entry, etc.)
        # TKINTER deja que Windows controle la ventana (estándar)    
        self.mainloop()
    
    # Definimos el método tras evento de cambio en Entry (temperatura)
    # Lleva *args porque se le pueden pasar argumentos (o no, pero al ponerlo no petará)
    # y como no lo se, pues con el * lo dejo abierto.
    # En este caso, no sabemos cómo funciona por dentro el trace
    def validarTemperatura(self, *args):
        # Si es float, lo mantenemos, pero si no borramos el cambio
        textoTemp = self.temperatura.get()
        try:
            float(textoTemp)   # Si es, lo dejamos
        except:
            self.temperatura.set(textoTemp[:-1]) # Si no es float, borramos el último
            
    # Aquí ejectuamos código si hay selected en radiobutton,
    # es decir, si cambiamos de unidades de temperatura
    #(command.selected lo hemos llamado)
    def selected(self):
        resultado = 0
        unidadFinal = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if unidadFinal == "F":
            resultado = grados * 9 / 5 +32
        elif unidadFinal == "C":
            resultado = (grados-32) * 5 / 9
        else:
            resultado = grados
        
        self.temperatura.set(str(resultado))

if __name__ == "__main__":
    app = mainApp()
    app.arrancar()
    
