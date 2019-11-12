import serial
import serial.tools.list_ports
from Interface.device import Device
import threading
from threading import *


class SerialThread(threading.Thread):

    # initialization of a SerialThread object
    def __init__(self):
        Thread.__init__(self)
        threading.Thread.__init__(self)
        self.device = None
        self.current_device = None

    # function that runs updates on the ports
    def run(self):
        self.update()

    # setter for device
    def set_device(self, device):
        self.device = device

    # getter for device
    def get_device(self):
        return self.device

    # function to update port states
    def update(self):
        self.scan_ports()
        threading.Timer(1, self.update).start()

    # this function scans ports to see if a device is connected
    def scan_ports(self):
        for port in serial.tools.list_ports.comports():
            if 'COM3' in port:
                try:
                    self.current_device = port.device
                    print('Connected to:', port.device)
                    self.device.run(port.device)
                except:
                    continue
