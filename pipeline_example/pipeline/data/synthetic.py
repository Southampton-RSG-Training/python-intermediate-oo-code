import numpy as np

from pipeline.data import DataBase


class DataSynthetic(DataBase):
    """
    Class for creating synthetic data for testing our methods.
    """
    def load(self, num_points: int = 100):
        """
        We're going to make cos(x) from 0 - 2 Pi.
        """
        self.values = np.cos(
            np.linspace(0, 2* np.pi, num_points)
        )

