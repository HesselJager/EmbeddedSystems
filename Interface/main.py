from Interface.serial_thread import SerialThread
from Interface.csv_thread import CsvThread
from Interface.Gui import Gui

class Main:

    csv_data = []

    def __init__(self):
        self.start_threads()

    def start_threads(self):
        self.serialTools = SerialThread()
        self.serialTools.start()

        self.csvThread = CsvThread(self)
        self.csvThread.start()

        self.Gui = Gui(self)


Main()