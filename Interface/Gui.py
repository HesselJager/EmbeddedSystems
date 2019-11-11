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
        button2 = Button(tab1, text = "Rol in")
        button2.grid(row = 9, column = 0, sticky = "W")

        button3 = Button(tab1, text = "automatisch in/uit rollen uitschakelen")
        button3.grid(row = 10, column = 0, sticky = "W")

        button4 = Button(tab1, text = "automatisch in/uit rollen inschakelen")
        button4.grid(row = 11, column = 0, sticky = "W")

        button5 = Button(tab1, text = "Reset to default")
        button5.grid(row = 12, column = 0, sticky = "W")

        # grafiek voor de licht sensor


        # run the windonw:
        window.mainloop()

    def animate(self):
        # grafiek voor de licht sensor
        x_values = []
        y_values = []

        index = count()
        x_values.append(next(index))
        y_values.append(random.randint(0, 5))
        plt.cla()
        plt.plot(x_values, y_values, label='Licht intensiteit')
        plt.legend(loc='upper left')



        FuncAnimation(plt.gcf(), animate, interval=1000)
        plt.show()



gui = Gui()
gui.animate()
