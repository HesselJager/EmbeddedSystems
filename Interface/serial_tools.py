import serial
import serial.tools.list_ports

class SerialTools:
    ports = []
    arduino_port = None
    arduino_port_serial = None

    def __init__(self):
        self.ports = self.scan_ports()
    pass

    # Scan all of the comports
    def scan_ports(self):
        return serial.tools.list_ports.comports()

    # Return the list of ports
    def get_ports(self):
        return self.ports

    def select_port(self, port):
        self.arduino_port = port

    def initialize_connection(self):
        if self.arduino_port is not None:
            self.arduino_port_serial = serial.Serial(port=self.arduino_port, baudrate=19200)
        else:
            raise Exception('Please select a COMPORT to use first!')

    def open_connection(self):
        if self.arduino_port_serial is not None:
            if self.arduino_port_serial.isOpen():
                raise Exception('Serial connection is already open!')
            else:
                self.arduino_port_serial.open()
        else:
            raise Exception('Please initialize a serial connection first!')

    def write_data(self, data):
        self.arduino_port_serial.write(bytes(data))