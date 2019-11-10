import threading
import serial
import serial.tools.list_ports
from port_thread import PortThread

class SerialThread (threading.Thread):

    ports = []

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.update()

    def update(self):
        self.scan_ports()
        threading.Timer(1, self.update).start()

    def scan_ports(self):
        for port in serial.tools.list_ports.comports():
            try:
                if "Arduino Uno" in str(port):
                    if port.device not in self.ports:
                        portThread = PortThread(port.device)
                        portThread.start()

                        self.ports.append(port.device)
            except: continue
