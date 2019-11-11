import threading
import csv

class CsvThread (threading.Thread):

    def __init__(self, main):
        self.main = main
        threading.Thread.__init__(self)

    def run(self):
        self.update()

    def update(self):
        with open('test_data.csv', 'rt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            results = []

            for row in csv_reader:
                results.append(row)
                self.main.csv_data = results

        threading.Timer(1, self.update).start()