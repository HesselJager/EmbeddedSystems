from serial_thread import SerialThread
from csv_thread import CsvThread

class Main:

    csv_data = []

    def __init__(self):
        self.start_threads()

    def start_threads(self):
        self.serialTools = SerialThread()
        self.serialTools.start()

        self.csvThread = CsvThread(self)
        self.csvThread.start()

Main()