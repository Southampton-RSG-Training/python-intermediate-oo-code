from numpy import loadtxt

from pipeline.data import DataBase


class DataCSV(DataBase):
    """
    Class for reading in a single-column CSV file.
    """
    def load(self, input_file):
        self.values = loadtxt(input_file, delimiter=',')
