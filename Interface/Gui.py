from tkinter import *
from tkinter import ttk
from threading import *

class Gui(Thread):

    # initialize Gui object
    def __init__(self, main):
        Thread.__init__(self)
        self.device = None
        self.current_temperature = None
        self.current_light = None
        self.main = main

    # run the Gui object
    def run(self):
        self.render()

    # function to set the current device
    def set_device(self, device):
        self.device = device

    # getter for device
    def get_device(self):
        return self.device

    # getter for current temperature
    def get_current_temperature(self):
        return self.current_temperature

    # getter for current light
    def get_current_light(self):
        return self.current_light

    #
    def button1_press(self):
        print("rolluik wordt uitgerold")
        #self.main.port_thread.roll_out()


    def button2_press(self):
        print("rolluik wordt ingerold")
        #self.main.port_thread.roll_in()


    def button3_press(self):
        print("waarde zijn gereset")
        #self.main.port_thread.reset_to_default()


    def button4_press(self):
        print("automatisch in/autrollen is uitgeschakeld")
        #self.main.port_thread.dissable_autoroll()


    def button5_press(self):
        print("automatisch in/autrollen is ingeschakeld")
        #self.main.port_thread.enable_autoroll()

    # placeholder function for sending data from entry field
    def hit_return(self):
        print("Data verzonden")

    # placeholder function for temperature data
    def get_temperature(self):
        return "15°C"

    # placeholder function for light data
    def get_light(self):
        return 3600

    # function to render the GUI on screen
    def render(self):
        # main window:
        window = Tk()
        window.title("Centrale")
        window.geometry("500x500")

        #-------------------------------------------------TABS

        # widget that implements the tabs in the GUI
        tab_control = ttk.Notebook(window)
        tab_control.grid(row=1, column=0, sticky="NESW")

        # settings tab
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="Settings")

        # light sensor device tab
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text="Lichtsensor")

        # temperature sensor device tab
        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text="Temperatuursensor")

        # ultrasound sensor tab
        tab4 = ttk.Frame(tab_control)
        tab_control.add(tab4, text="Ultrasoonsensor")

        #-------------------------------------------------LABELS

        # labels for settings tab
        label1 = Label(tab1, text="maximale uitrolwaarde:")
        label1.grid(row=1, column=0, sticky="W")

        label2 = Label(tab1, text="maximale inrolwaarde:")
        label2.grid(row=4, column=0, sticky="W")

        # labels for light sensor tab
        label_light_text = Label(tab2, text="Huidige lichintensiteit:")
        label_light_text.grid(row=1, column=0, sticky="W")

        label_light = Label(tab2, text=self.get_light())
        label_light.grid(row=2, column=0, sticky="W")
        label_light.config(text=self.get_light())

        # labels for temperature sensor tab
        label_temperature_text = Label(tab3, text="Huidige temperatuur:")
        label_temperature_text.grid(row=1, column=0, sticky="W")

        label_temperature = Label(tab3, text=self.get_temperature())
        label_temperature.grid(row=2, column=0, sticky="W")
        label_temperature.config(text=self.get_temperature())

        #-------------------------------------------------INPUT

        # Entry field that can update the maximum roll out value in arduino
        entry1 = Entry(tab1)
        entry1.grid(row=3, column=0, sticky="W")
        entry1.bind("<Return>", self.hit_return)

        # Entry field that can update the maximum roll in value in arduino
        entry2 = Entry(tab1)
        entry2.grid(row=5, column=0, sticky="W")
        entry2.bind("<Return>", self.hit_return)

        # button that, when pressed, signals manual_roll_out command in arduino
        button1 = Button(tab1, text="handmatig uitrollen", command=self.button1_press)
        button1.grid(row=8, column=0, sticky="W")

        # button that, when pressed, signals manual_roll_in command in arduino
        button2 = Button(tab1, text="handmatig oprollen", command=self.button2_press)
        button2.grid(row=9, column=0, sticky="W")

        # button that, when pressed, signals disable_autoroll_in command in arduino
        button3 = Button(tab1, text="automatisch rollen uitschakelen", command=self.button4_press)
        button3.grid(row=10, column=0, sticky="W")

        # button that, when pressed, signals enable_autoroll in command in arduino
        button4 = Button(tab1, text="automatisch rollen inschakelen", command=self.button5_press)
        button4.grid(row=11, column=0, sticky="W")

        # button that, when pressed, signals reset_to_default command in arduino
        button5 = Button(tab1, text="Reset standaard grenswaarden", command=self.button3_press)
        button5.grid(row=12, column=0, sticky="W")

        # run the windonw:
        window.mainloop()