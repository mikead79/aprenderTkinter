from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    __tempAnterior = ""
    
    def __init__(self):
        Tk.__init__(self)

        self.geometry("210x150")
        self.title("Termometro")
        self.configure(bg = "#ECECEC")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature)
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
    
    def validateTemperature(self, *args):
        try:
            val = float(self.temperatura.get())
            self.__tempAnterior = self.temperatura.get()
        except:
            self.temperatura.set(self.__tempAnterior)
    
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lblUnidad = ttk.Label(self, text="Grados").place(x=10, y=45)
        self.unidadF = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=25, y=70)
        self.unidadC = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C", command=self.selected).place(x=25, y=95)
    
    def start(self):
        self.mainloop()
    
    def selected(self):
        resultado = 0
        if self.tipoUnidad.get() == "F":
            resultado = float(self.temperatura.get()) * 9/5 + 32
        elif self.tipoUnidad.get() == "C":
            resultado = (float(self.temperatura.get()) - 32) * 5/9
        else:
            resultado = self.temperatura.get()
        self.temperatura.set(round(resultado, 2))

if __name__ == "__main__":
    app = mainApp()
    app.start()

