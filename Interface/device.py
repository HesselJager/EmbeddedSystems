import serial as serial
import time
import threading
from threading import *

class Device(Thread):

    def __init__(self):
        Thread.__init__(self)


    def run(self, port):
        self.ser = serial.Serial(port, baudrate=19200, timeout=5)
        time.sleep(1)
        self.device = None
        self.handshake()
        print('Unit is ', self.device)
        self.last_measure = 0
        self.main()
        
    # returns a string with temperature or light,
    # which indicates if the connected device is a
    # temperature sensor of a light sensor
    def handshake(self):
        if self.read_data() == 255:
            self.write_data(b'\xFF')

            # 0x96
            if self.read_data() == 150:
                self.device = 'TEMPERATURE'

            # 0x69
            if self.read_data() == 105:
                self.device = 'LIGHT'

    # function that write a number to the arduino
    def write_data(self, data):  # something like b'\x02'
        self.ser.write(data)
        time.sleep(.5)

    # function that returns a number from the arduino
    def read_data(self):
        line = self.ser.read()
        # only show bytes with content, not the empty ones
        if line != b'':
            while (line is not None):
                # make sure to use int.from_bytes(line, "big")
                # otherwise it will print something like b'\xa4'

                return ord(line)

    def main(self):

        while (True):
            data = self.read_data()

            if data is not None:
                self.last_measure = data

                #print(data)

    def get_last_measure(self):
        return self.last_measure

    def get_device(self):
        return self.device

    def roll_out(self):
        self.ser.write(b'\x03')
        time.sleep(.5)

    def roll_in(self):
        self.ser.write(b'\x04')
        time.sleep(.5)

    def reset_to_default(self):
        self.ser.write(b'\x05')
        time.sleep(.5)

    def disable_autoroll(self):
        self.ser.write(b'\x06')
        time.sleep(.5)

    def enable_autoroll(self):
        self.ser.write(b'\x07')
        time.sleep(.5)
