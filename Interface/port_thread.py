import threading
import serial

class PortThread (threading.Thread):

    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port=self.port, baudrate=19200)

        threading.Thread.__init__(self)

    def run(self):
        self.ser.readline()
        threading.Timer(1.01, self.run).start()