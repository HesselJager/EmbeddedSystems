import serial as serial
import time
import threading
from threading import *

class Device(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.device = None


    def run(self, port):
        self.ser = serial.Serial(port, baudrate=19200, timeout=5)
        time.sleep(1)
        self.device = None
        self.handshake()
        print('Unit is ', self.device)
        self.last_measure = 0
        self.main()

    # returns a string with temperature or light,
    # which indicates if the connected device is a
    # temperature sensor of a light sensor
    def handshake(self):
        if self.read_data() == 255:
            self.write_data(b'\xFF')

            # 0x96
            if self.read_data() == 150:
                self.device = 'TEMPERATURE'

            # 0x69
            if self.read_data() == 105:
                self.device = 'LIGHT'

    # function that write a number to the arduino
    def write_data(self, data):  # something like b'\x02'
        self.ser.write(data)
        time.sleep(.5)

    # function that returns a number from the arduino
    def read_data(self):
        line = self.ser.read()
        # only show bytes with content, not the empty ones
        if line != b'':
            while (line is not None):
                # make sure to use int.from_bytes(line, "big")
                # otherwise it will print something like b'\xa4'

                return ord(line)

    def main(self):

        while (True):
            data = self.read_data()

            if data is not None:
                self.last_measure = data

    def get_last_measure(self):
        return self.last_measure

    def get_device(self):
        return self.device

    # function that calls a command from the arduino
    def send_command(self, command):
        # send command value to arduino and wait for a response
        self.write_data(command)
        response = self.read_data()

        # check if the command is succesfully executed (0xAA) or not (0xBB)
        if(response == 170): #0xAA
            self.confirmation_message(command)
        elif(response == 187): #0xBB
            self.error_message(command)
        else:
            print("oeps, er ging iets mis met het versturen of ontvangen van de command")

    # function that returns a confirmation message for a succesfully executed command
    def confirmation_message(self, command):
        switcher = {
            1: "Maximale uitrol waarde is succesvol aangepast",
            2: "Maximale oprol waarde is succesvol aangepast",
            3: "Het rolluik rolt nu uit (let op: automatisch rollen is uitgeschakeld)",
            4: "Het rolluik rolt nu op (let op: automatich rollen is uitgeschakeld)",
            5: "De maximale op- en uitrol waarden zijn gereset naar de standaard waarden",
            6: "Automatisch rollen is nu uitgeschakeld",
            7: "Automatisch rollen is nu ingeschakeld",
            # the following three commands are getter functions
            8: ("enabled" if self.read_data() == 240 else "disabled"),  # get state of automatic rolling
            9: self.read_data(),                                        # get maximum roll out border
            10: self.read_data()}                                       # get maximum roll in border
        return switcher.get(command, "invalid command")

    # function that returns an error message for an executed command
    def error_message(self, command):
        switcher = {
            1: "Fout: Maximale uitrol waarde mag niet kleiner zijn dan de maximale oprol waarde",
            2: "Fout: Maximale oprol waarde mag niet groter zijn dan de maximale uitrol waarde",
            3: "Fout: Het rolluik rolt al uit",
            4: "Fout: Het rolluik rolt al op",
            6: "Fout: Automatisch rollen is al uitgeschakeld",
            7: "Fout: Automatisch rollen is al ingeschakeld"}
        return switcher.get(command, "invalid command")
