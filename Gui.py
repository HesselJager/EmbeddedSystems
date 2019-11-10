from tkinter import *
from tkinter import ttk


import matplotlib.pyplot as plt
import random
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
import matplotlib.backends.backend_tkagg



# functie die entry1 checkt
def hitReturn(*args):
    print("Data verzonden")

# functie die zorgt dat button1 het rolluik uitrolt
def button1Function():
    print("rolluik wordt uitgerold")

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

label1 = Label(tab1, text = "Voer temperatuur in:")
label1.grid(row = 1, column =0, sticky = "W")

# Het veld dat de data verzend naar de arduino
entry1 = Entry(tab1)
entry1.grid(row = 3, column = 0, sticky = "W")
entry1.bind("<Return>", hitReturn)

#knop die het rolluik uitrolt
button1= Button(tab1, text = "rol uit", command = button1Function)
button1.grid(row = 8, column = 0, sticky = "W")

# grafiek voor de licht sensor

x_values = []
y_values = []

index = count()

def animate(i):
    x_values.append(next(index))
    y_values.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_values, y_values, label='Licht intensiteit')
    plt.legend(loc='upper left')


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plot1 = plt.show()

#

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)




# run the windonw:
window.mainloop()
