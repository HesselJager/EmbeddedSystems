import threading
import serial
import time

class PortThread (threading.Thread):

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.ser = serial.Serial(port=port, baudrate=19200, timeout=5)
        time.sleep(2)

    def readCommand(self):
        print 'hey'

    def run(self):
        while True:
            print 'true'
            self.ser.write(b'\x02')
            time.sleep(8)

            line = self.ser.read()

            # only show bytes with content, not the empty ones
            if (line != b''):
                # make sure to use int.from_bytes(line, "big")
                # otherwise it will print something like b'\xa4'
                print(int.from_bytes(line, "big"))
                print(line)