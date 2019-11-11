import serial
import serial.tools.list_ports
from Interface.device import Device
from threading import *


class SerialThread(Thread):

    # initialization of a SerialThread object
    def __init__(self):
        Thread.__init__(self)
        Thread.__init__(self)
        self.device = None

    # function that runs updates on the ports
    def run(self):
        self.update()

    # function that returns the device of a SerialThread object
    def return_device(self):
        return self.device

    # function to update port states
    def update(self):
        self.scan_ports()
        Timer(1, self.update).start()

    # this function scans ports to see if a device is connected
    def scan_ports(self):
        for port in serial.tools.list_ports.comports():
            if 'COM3' in port:  # om mijn leven makkelijker te maken, usb koptelefoon, zucht
                if port.device != self.device:
                    try:
                        print('Connected to ', port.device)
                        device = Device(port.device)
                        device.run()
                        self.device = port.device
                    except:
                        continue
