import time

class Main:
    ports = []

    def __init__(self):
        self.ports = self.scanPorts()

        for port in self.ports:
            print port.device

        ser = serial.Serial(port="COM3", baudrate=19200)

        time.sleep(5)

        if ser.isOpen():
            test = 2
            ser.write(bytes([test]))
        else:
            ser.open()

        pass

Main()