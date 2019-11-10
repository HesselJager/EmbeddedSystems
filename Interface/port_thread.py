import threading
import serial
import time

class PortThread (threading.Thread):

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.ser = serial.Serial(port, baudrate=19200, timeout=5)
        time.sleep(2)

    def write_data(self, data): #something like b'\x02'
        self.ser.write(data)
        time.sleep(.5)

    def read_data(self):
        line = self.ser.read()

        # only show bytes with content, not the empty ones
        if line != b'':
            # make sure to use int.from_bytes(line, "big")
            # otherwise it will print something like b'\xa4'
            return int.from_bytes(line, "big")

    def run(self):
        while True:
            line = self.read_data()
            if isinstance(line, int):
                print(line)