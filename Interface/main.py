from Interface.serial_thread import SerialThread
from Interface.Gui import Gui
import threading
from threading import *
from time import sleep
from Interface.device import Device


class Main(threading.Thread):

    def __init__(self):
        self.gui = Gui()
        self.gui.start()

        self.device = Device()

        self.serial = SerialThread()
        self.serial.set_device(self.device)
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
