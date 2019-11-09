import threading
import time
import serial
import serial.tools.list_ports

class SerialTools (threading.Thread):
    ports = []
    arduino_port = None
    arduino_port_serial = None

    def __init__(self):
        self.ports = self.scan_ports()
        threading.Thread.__init__(self)
    pass

    def run(self):
        self.read_data()

    # Scan all of the comports
    def scan_ports(self):
        return serial.tools.list_ports.comports()

    # Return the list of ports
    def get_ports(self):
        return self.ports

    # Set the COMPORT to use
    def set_port(self, port):
        self.arduino_port = port

    # Initialize the serial connection
    def initialize_connection(self):
        if self.arduino_port is not None:
            self.arduino_port_serial = serial.Serial(port=self.arduino_port, baudrate=19200)
            time.sleep(2)
        else:
            raise Exception('Please select a COMPORT to use first!')

    def open_connection(self):
        if self.arduino_port_serial is not None:
            if self.arduino_port_serial.isOpen():
                pass
            else:
                self.arduino_port_serial.open()
        else:
            raise Exception('Please initialize a serial connection first!')

    def write_data(self, data):
        self.arduino_port_serial.write(data)  # b'\x02' as example

    def read_data(self):
        self.write_data(b'\x02')
        print 'hey'

        line = self.arduino_port_serial.read()

        if (line != b''):
            print(int.from_bytes(line, "big"))
            print(line)


        threading.Timer(1.01, self.read_data).start()

