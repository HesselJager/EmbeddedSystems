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
            try:
                current_temperature = self.device.get_last_measure()
                #print(self.device.get_last_measure())
                sleep(5)
                self.gui.set_current_temperature(current_temperature)
            except: AttributeError



main = Main()