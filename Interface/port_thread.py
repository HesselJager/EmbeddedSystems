import threading
import serial
import time
import csv
from time import gmtime, strftime

class PortThread (threading.Thread):

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.device = None
        self.port = port
        self.ser = serial.Serial(port, baudrate=19200, timeout=5)
        self.handshake()
        time.sleep(2)
        self.run()
        print(self.device)

    def get_device(self):
        return self.device

    # function that write a number to the arduino
    def write_data(self, data): #something like b'\x02'
        self.ser.write(data)
        time.sleep(.5)

    # function that returns a number from the arduino
    def read_data(self):
        line = self.ser.read()

        # only show bytes with content, not the empty ones
        if line != b'':
            # make sure to use int.from_bytes(line, "big")
            # otherwise it will print something like b'\xa4'
            if (self.device is not None):
                with open(r'DATA_' + self.device + '.csv', 'ab') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=';')
                    csv_writer.writerow([strftime("%Y-%m-%d %H:%M:%S", gmtime()), ord(line)])

                    threading.Timer(0.01, self.read_data).start()
            return ord(line)

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

    def run(self):
        print(self.device)

        while(True):
            print(self.read_data())

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