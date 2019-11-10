import threading
import serial
import time

class PortThread (threading.Thread):

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.ser = serial.Serial(port=port, baudrate=19200, timeout=5)

    def readCommand(self):
        print 'hey'

    def run(self):
        print self.ser.readline()
        threading.Timer(0.01, self.readCommand).start()