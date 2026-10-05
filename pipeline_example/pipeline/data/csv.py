from pathlib import Path
import numpy as np

from pipeline.data import DataBase


class DataCSV(DataBase):
    """
    Class for reading in a single-column CSV file.
    """
    def __init__(self, input_file: Path):
        """
        Initialise the data file and store the path to load.

        :param input_file: The path to load from.
        """
        super().__init__()
        self.input_file = input_file

    def load(self):
        """
        We're just going to wrap the numpy function here.
        The structure seems a bit superfluous now, but you benefit from the flexibility later.

        :param input_file: The path to the input file to load.
        """
        values = np.loadtxt(self.input_file, delimiter=',')
        self.x = values[:, 0]
        self.y = values[:, 1]

