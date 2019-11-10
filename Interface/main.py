from serial_thread import SerialThread

class Main:

    def __init__(self):
        self.start_threads()

    def start_threads(self):
        self.serialTools = SerialThread()
        self.serialTools.start()


Main()