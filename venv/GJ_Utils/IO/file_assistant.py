import numpy as np
import pandas as pd


class file_assistant:
    _vectorize = 'v'
    _read = 'r'
    _write = 'w'
    _append = 'a'

    def __init__(self, file_name, process='r', method='DataFrame'):
        self.name = file_name
        self.process = process.lower()
        self.method = method
        self.perform_process()

    def perform_process(self):
        if self._vectorize == self.process:
            print('The vectorize function is not ready yet, try again later.')
        elif self.process == self._read:
            self.f = open(self.name, self.process)
            if self.method is not None:
                self.read_file(self.method)
            else:
                print('You must supply a method.\nEnter help-methods for options\examples')
                quit(-99)
        elif self.process == self._write:
            self.f = open(self.name, self.process)
            if self.method is not None:
                self.write_file(self.method)
            else:
                print('You must supply a method.\nEnter help-methods for options\examples')
                quit(-99)
        elif self.process == _append:
            self.f = open(self.name, self.process)
            if self.method is not None:
                self.append_file(self.method)
            else:
                print('You must supply a method.\nEnter help-methods for options\examples')
                quit(-99)

    def read_file(self, method):
        if method == 'DataFrame':
            return self.Process_DataFrame()

    def write_file(self, method):
        pass

    def append_file(self, method):
        pass

    def Process_DataFrame(self, index=0, sheet='sheet1'):
        return pd.read_excel(self.name)