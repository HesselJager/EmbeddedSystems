from Interface.serial_thread import SerialThread
from Interface.Gui import Gui
import threading
from threading import *
from time import sleep
from Interface.device import Device

class Main(Thread):

    def __init__(self):
        self.gui = Gui(self)
        self.gui.start()

        self.serial = SerialThread()
        self.serial.start()

        #self.gui.setDevice(device)

main = Main()