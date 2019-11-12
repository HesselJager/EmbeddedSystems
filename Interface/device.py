import serial as serial
import time
import threading
from threading import *


# noinspection PyMethodMayBeStatic
class Device(threading.Thread):

    def __init__(self):
        # Thread.__init__(self)
        threading.Thread.__init__(self)
        self.port = None
        self.ser = None
        self.command_in_progress = False
        self.device = None
        self.last_measure = 0

    # run thread function for Device object
    def run(self):
        self.ser = serial.Serial(self.port, baudrate=19200, timeout=5)
        time.sleep(1)
        self.command_in_progress = False
        self.device = None
        self.last_measure = 0

        self.handshake()
        self.main()

    # main function
    def main(self):
        while True:
            if not self.command_in_progress:
                data = self.read_data()
                if data is not None:
                    self.last_measure = data

    # setter for port
    def set_port(self, port):
        self.port = port

    # getter for port
    def get_port(self):
        return self.port

    # returns a string with temperature or light,
    # which indicates if the connected device is a
    # temperature sensor of a light sensor
    def handshake(self):
        if self.read_data() == 255:
            self.write_data(b'\xFF')
            device_id = self.read_data()

            if device_id == 150:  # 0x96
                self.device = 'TEMPERATURE'
            elif device_id == 105:  # 0x69
                self.device = 'LIGHT'
            else:
                print("Er ging iets fout bij de handshake")

            print('Unit is:', self.device)

    # function that write a number to the arduino
    def write_data(self, data):  # something like b'\x02'
        self.ser.write(data)
        time.sleep(.5)

    # function that returns a number from the arduino
    def read_data(self):
        line = self.ser.read()
        # only show bytes with content, not the empty ones
        if line != b'':
            while line is not None:
                # make sure to use int.from_bytes(line, "big")
                # otherwise it will print something like b'\xa4'

                return ord(line)

    # getter for last measurement
    def get_last_measure(self):
        return self.last_measure

    # getter for device name
    def get_device(self):
        return self.device

    # function that calls a command from the arduino
    def send_command(self, command):
        self.command_in_progress = True

        # send command value to arduino and wait for a response
        self.write_data(command)
        response = self.ser.read()

        self.command_in_progress = False

        print(response)

        # check if the command is successfully executed (0xAA) or not (0xBB)
        if response == 170:  # 0xAA
            print(self.confirmation_message(command))
        elif response == 187:  # 0xBB
            print(self.error_message(command))

    # function that returns a confirmation message for a succesfully executed command
    def confirmation_message(self, command):
        switcher = {
            b'\x01': "Maximale uitrol waarde is succesvol aangepast",
            b'\x02': "Maximale oprol waarde is succesvol aangepast",
            b'\x03': "Het rolluik rolt nu uit (let op: automatisch rollen is uitgeschakeld)",
            b'\x04': "Het rolluik rolt nu op (let op: automatich rollen is uitgeschakeld)",
            b'\x05': "De maximale op- en uitrol waarden zijn gereset naar de standaard waarden",
            b'\x06': "Automatisch rollen is nu uitgeschakeld",
            b'\x07': "Automatisch rollen is nu ingeschakeld",
            # the following three commands are getter functions
            b'\x08': ("enabled" if self.read_data() == 240 else "disabled"),  # get state of automatic rolling
            b'\x09': self.read_data(),  # get maximum roll out border
            b'\x0A': self.read_data()}  # get maximum roll in border
        return switcher.get(command, "invalid command")

    # function that returns an error message for an executed command
    def error_message(self, command):
        switcher = {
            b'\x01': "Fout: Maximale uitrol waarde mag niet kleiner zijn dan de maximale oprol waarde",
            b'\x02': "Fout: Maximale oprol waarde mag niet groter zijn dan de maximale uitrol waarde",
            b'\x03': "Fout: Het rolluik rolt al uit",
            b'\x04': "Fout: Het rolluik rolt al op",
            b'\x06': "Fout: Automatisch rollen is al uitgeschakeld",
            b'\x07': "Fout: Automatisch rollen is al ingeschakeld"}
        return switcher.get(command, "invalid command")
