from Interface.serial_thread import SerialThread
from Interface.Gui import Gui
import threading
from threading import *
from time import sleep
from Interface.device import Device
import Interface.app as app


# noinspection PyBroadException,PyStatementEffect
class Main(threading.Thread):

    def __init__(self):
        # Thread.__init__(self)
        threading.Thread.__init__(self)

        self.gui = Gui()
        self.gui.start()

        self.device = Device()

        self.serial = SerialThread()
        self.serial.set_device(self.device)
        self.gui.set_device(self.device)
        self.serial.start()

        #app.run_server()

        while True:
            self.device_type = self.device.get_device()
            try:
                if self.device_type == 'TEMPERATURE':
                    if self.device.command_check == b'\x00':
                        current_temperature = self.device.get_last_measure()
                        self.gui.set_temperature(current_temperature)
                    else:
                        self.device.send_command()

                if self.device_type == 'LIGHT':
                    if self.device.command_check == b'\x00':
                        current_light = self.device.get_last_measure()
                        self.gui.set_light(current_light)
                    else:
                        self.device.send_command()


                self.gui.update()
                sleep(5)
            except:
                AttributeError


main = Main()
