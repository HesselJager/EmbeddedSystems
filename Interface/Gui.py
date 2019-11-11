from tkinter import *
from tkinter import ttk
from threading import *
import threading

class Gui(Thread):

    def __init__(self, main):
        Thread.__init__(self)
        self.device = None
        self.current_temperature = None
        self.current_light = None
        self.main = main

    def run(self):
        self.render()

    def setDevice(self, device):
        self.device = device

    def button1Function(self):
        print("rolluik wordt uitgerold")
        #self.main.port_thread.roll_out()

    def button2Function(self):
        print("rolluik wordt ingerold")
        #self.main.port_thread.roll_in()

    def button3Function(self):
        print("waarde zijn gereset")
        #self.main.port_thread.reset_to_default()

    def button4Function(self):
        print("automatisch in/autrollen is uitgeschakeld")
        #self.main.port_thread.dissable_autoroll()


    def button5Function(self):
        print("automatisch in/autrollen is ingeschakeld")
        #self.main.port_thread.enable_autoroll()

    def hitReturn(self):
        print("Data verzonden")

    def getTemperature(self):
        return "15°C"

    def getLight(self):
        return 3600

    def render(self):
        # main window:
        window = Tk()
        window.title("Centrale")
        window.geometry("500x500")

        # de widget die de tabs implenmenteerd
        tabControl = ttk.Notebook(window)
        tabControl.grid(row=1, column=0, sticky="NESW")

        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Settings")

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="Lichtsensor")

        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text="Temperatuursensor")

        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text="Ultrasoonsensor")

        label1 = Label(tab1, text="maximale uitrolwaarde:")
        label1.grid(row=1, column=0, sticky="W")

        label_temperature_text = Label(tab3, text="Huidige temperatuur:")
        label_temperature_text.grid(row=1, column=0, sticky="W")

        label_temperature = Label(tab3, text=self.getTemperature())
        label_temperature.grid(row=2, column=0, sticky="W")
        label_temperature.config(text=self.getTemperature())

        '''---------------------------------------------------------------'''

        label_light_text = Label(tab2, text="Huidige lichintensiteit:")
        label_light_text.grid(row=1, column=0, sticky="W")

        label_light = Label(tab2, text=self.getLight())
        label_light.grid(row=2, column=0, sticky="W")
        label_light.config(text=self.getLight())

        label2 = Label(tab1, text="maximale inrolwaarde:")
        label2.grid(row=4, column=0, sticky="W")

        # Het veld dat de data verzend naar de arduino
        entry1 = Entry(tab1)
        entry1.grid(row=3, column=0, sticky="W")
        entry1.bind("<Return>", self.hitReturn)

        # Het veld dat de data verzend naar de arduino
        entry2 = Entry(tab1)
        entry2.grid(row=5, column=0, sticky="W")
        entry2.bind("<Return>", self.hitReturn)

        # knop die het rolluik uitrolt
        button1 = Button(tab1, text="rol uit", command=self.button1Function)
        button1.grid(row=8, column=0, sticky="W")

        # knop rolt het rolluik uit
        button2 = Button(tab1, text="Rol in", command=self.button2Function)
        button2.grid(row=9, column=0, sticky="W")

        button3 = Button(tab1, text="automatisch in/uit rollen uitschakelen", command=self.button4Function)
        button3.grid(row=10, column=0, sticky="W")

        button4 = Button(tab1, text="automatisch in/uit rollen inschakelen", command=self.button5Function)
        button4.grid(row=11, column=0, sticky="W")

        button5 = Button(tab1, text="Reset to default", command=self.button3Function)
        button5.grid(row=12, column=0, sticky="W")

        # run the windonw:
        window.mainloop()
