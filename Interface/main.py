from serial_tools import SerialTools

class Main:

    def __init__(self):
        self.start_threads()

    def start_threads(self):
        self.serial_tools = SerialTools()
        self.serial_tools_thread = self.serial_tools.start()

        self.serial_tools.set_port("COM4")
        self.serial_tools.initialize_connection()
        self.serial_tools.open_connection()

Main()