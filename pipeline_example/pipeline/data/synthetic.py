from pathlib import Path
import numpy as np

from pipeline.data import DataBase


class DataSynthetic(DataBase):
    """
    Class for creating synthetic data for testing our methods.
    """
    def __init__(self, noise_scale: float = 0):
        """
        Saves some configuration values for the synthetic data generator.

        :param noise_scale: How large the noise should be relative to the maximum value.
        """
        super().__init__()
        self.noise_scale = noise_scale

    def load(self, num_points: int = 20):
        """
        We're going to make cos(x) from 0 - 2 Pi.
        We'll optionally add some normal noise on top.

        :param num_points: The number of points of data to generate.
        """
        self.x = np.linspace(0, 2*np.pi, num_points)
        self.y = np.cos(self.x) + np.random.normal(scale=self.noise_scale, size=num_points)

    def to_csv(self, output_file: Path):
        """
        Saves synthetic data to file - I'm using this to make the 'real' data...

        :param output_file: The path to write the file to.
        """
        np.savetxt(
            output_file,
            np.column_stack([self.x.T, self.y.T]),
            delimiter=','
        )
