from serial_thread import SerialThread
from gui import Gui
import threading
from threading import *
from time import sleep
from device import Device

class Main(Thread):

    def __init__(self):
        self.gui = Gui()
        self.gui.start()

        self.serial = SerialThread()
        self.serial.start()

        self.gui.setDevice(device)


main = Main()