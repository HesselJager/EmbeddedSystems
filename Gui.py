from tkinter import *
from tkinter import ttk



# main window:
window = Tk()
window.title("Centrale")
window.geometry("500x500")



# de widget die de tabs implenmenteerd
tabControl = ttk.Notebook(window)
tabControl.grid(row =1, column = 0, columnspan = 50, rowspan= 49, sticky = "NESW")

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Settings")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Lichtsensor")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text = "Temperatuursensor")

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text = "Ultrasoonsensor")



#maakt de verschillende tabs



# run the windonw:
window.mainloop()
