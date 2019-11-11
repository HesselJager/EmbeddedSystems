from serial_thread import SerialThread
from Gui import Gui
import threading
from threading import *
from time import sleep

class Main(Thread):

    def __init__(self):
        self.gui = Gui(self)
        self.gui.start()

        self.serial = SerialThread()
        self.serial.start()

        #self.gui.setDevice(device)

main = Main()