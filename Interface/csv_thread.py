from threading import *
import csv


class CsvThread(Thread):

    # initialization for CsvThread object
    def __init__(self, main):
        self.main = main
        Thread.__init__(self)

    # function that runs a CsvThread object
    def run(self):
        self.update()

    # function that updates the csv files
    def update(self):
        with open('test_data.csv', 'rt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            results = []

            for row in csv_reader:
                results.append(row)
                self.main.csv_data = results

        Timer(1, self.update).start()
