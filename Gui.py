from tkinter import *
from tkinter import ttk

# functie die entry1 checkt
def hitReturn(*args):
    print("Data verzonden")


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





# run the windonw:
window.mainloop()
