import threading
import time
import serial
import serial.tools.list_ports

class PortTools (threading.Thread):
    # Scan all of the comports
    def scan_ports(self):
        return serial.tools.list_ports.comports()

    # Return the list of ports
    def get_ports(self):
        return self.ports