import threading
import serial
import time

class PortThread (threading.Thread):

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.ser = serial.Serial(port=port, baudrate=9600, timeout=5)

    def readCommand(self):
        print 'hey'

    def run(self):
        length = ord(self.ser.read(1).decode('utf-8'))  # Get command length
        commandString = self.ser.read(length).decode('utf-8')  # Get entire command with recieved length

        threading.Timer(0.01, self.readCommand).start()