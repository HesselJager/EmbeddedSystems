from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import random
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Gui:

    def __init__(self):
        self.render()

    # functie die entry1 checkt
    def hitReturn(self, *args):
        print("Data verzonden")

    # functie die zorgt dat button1 het rolluik uitrolt
    def button1Function(self):
        print("rolluik wordt uitgerold")
        self.main.port_thread.roll_out()

    def button2Function(self):
        print("rolluik wordt ingerold")
        self.main.port_thread.roll_in()

    def button3Function(self):
        print("waarde zijn gereset")
        self.main.port_thread.reset_to_default()

    def button4Function(self):
        print("automatisch in/autrollen is uitgeschakeld")
        self.main.port_thread.dissable_autoroll()

    def button5Function(self):
        print("automatisch in/autrollen is ingeschakeld")
        self.main.port_thread.enable_autoroll()

    def render(self):
        # main window:
        window = Tk()
        window.title("Centrale")
        window.geometry("500x500")

        # de widget die de tabs implenmenteerd
        tabControl = ttk.Notebook(window)
        tabControl.grid(row =1, column = 0, sticky = "NESW")

        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = "Settings")

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Lichtsensor")

        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text = "Temperatuursensor")

        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text = "Ultrasoonsensor")

        label1 = Label(tab1, text = "maximale uitrolwaarde:")
        label1.grid(row = 1, column =0, sticky = "W")

        label2 = Label(tab1, text = "maximale inrolwaarde:")
        label2.grid(row = 4, column =0, sticky = "W")

        # Het veld dat de data verzend naar de arduino
        entry1 = Entry(tab1)
        entry1.grid(row = 3, column = 0, sticky = "W")
        entry1.bind("<Return>", self.hitReturn)

        # Het veld dat de data verzend naar de arduino
        entry2 = Entry(tab1)
        entry2.grid(row = 5, column = 0, sticky = "W")
        entry2.bind("<Return>", self.hitReturn)

        #knop die het rolluik uitrolt
        button1= Button(tab1, text = "rol uit", command = self.button1Function)
        button1.grid(row = 8, column = 0, sticky = "W")

        #knop rolt het rolluik uit
        button2 = Button(tab1, text = "Rol in", command= self.button2Function)
        button2.grid(row = 9, column = 0, sticky = "W")

        button3 = Button(tab1, text = "automatisch in/uit rollen uitschakelen", command =self.button4Function)
        button3.grid(row = 10, column = 0, sticky = "W")

        button4 = Button(tab1, text = "automatisch in/uit rollen inschakelen", command= self.button5Function)
        button4.grid(row = 11, column = 0, sticky = "W")

        button5 = Button(tab1, text = "Reset to default", command = self.button3Function)
        button5.grid(row = 12, column = 0, sticky = "W")

        # grafiek voor de licht sensor


        # run the windonw:
        window.mainloop()




gui = Gui()


#class Graph:
 #   def __init__(self):
  #      # grafiek voor de licht sensor
   #     self.x_values = []
    #    self.y_values = []
#
#        self.index = count()
#
#        def animate(self, i):
#        x_values.append(next(index))
#        y_values.append(random.randint(0, 5))
#        plt.cla()
 #       plt.plot(x_values, y_values, label='Licht intensiteit')
#        plt.legend(loc='upper left')

#    def start(self):
#       self.ani = FuncAnimation(plt.gcf(), self.animate, interval=1000)

#ani = Graph()
#ani.start()
#plt.show
