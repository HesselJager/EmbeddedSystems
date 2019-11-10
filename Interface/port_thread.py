import threading
import serial
import time

class PortThread:

    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port='COM3', baudrate=19200, timeout=5)

        while True:
            self.ser.readline()
            time.sleep(2)

