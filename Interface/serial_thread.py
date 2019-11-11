import serial
import serial.tools.list_ports
from Interface.device import Device
import threading
from threading import *


class SerialThread(threading.Thread):

    def __init__(self):
        Thread.__init__(self)
        threading.Thread.__init__(self)
        self.device = None

    def run(self):
        self.update()

    def setDevice(self, device):
        self.device = device

    def return_port_threads(self):
        return self.port_threads

    def return_device(self):
        return self.device

    def update(self):
        self.scan_ports()
        print(self.device)
        threading.Timer(1, self.update).start()

    def scan_ports(self):
        for port in serial.tools.list_ports.comports():
            if 'COM3' in port:  # om mijn leven makkelijker te maken, usb koptelefoon, zucht
                try:
                    print('Connected to ', port.device)
                    self.device.run(port.device)
                except:
                    continue


