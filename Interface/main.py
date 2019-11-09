from serial_tools import SerialTools

class Main:

    def __init__(self):
        self.start_threads()

    def start_threads(self):
        self.serialTools = SerialTools()
        self.serialTools.set_port("COM3")
        self.serialTools.initialize_connection()
        self.serialTools.open_connection()
        self.serialTools.start()

Main()