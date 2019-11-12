from serial_thread import SerialThread
from Gui import Gui
import threading
from threading import *
from time import sleep
from device import Device

class Main(Thread):

    def __init__(self):
        self.gui = Gui()
        self.gui.start()

        self.device = Device()

        self.serial = SerialThread()
        self.serial.setDevice(self.device)
        self.gui.setDevice(self.device)
        self.serial.start()

        while(True):
            self.device_type = self.device.get_device()
            try:
                if self.device_type == 'TEMPERATURE':
                    current_temperature = self.device.get_last_measure()
                    self.gui.set_current_temperature(current_temperature)

                if self.device_type == 'LIGHT':
                    current_light = self.device.get_last_measure()
                    self.gui.set_current_light(current_light)

                self.gui.update()
                sleep(5)
            except: AttributeError



main = Main()