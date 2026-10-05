"""
Contains the basic class used for all data sources.
"""
from abc import ABC, abstractmethod

import numpy as np
from numpy.typing import NDArray


class DataBase(ABC):
    """
    Base class that standardises the interface for loading data.
    """
    def __init__(self):
        """
        We declare the values in the initialiser to be a numpy array.
        The typing is optional here, but if we use it our IDE will warn us
        if we try to overwrite the values with a non-array.
        """
        self.x: NDArray = np.zeros([0])
        self.y: NDArray = np.zeros([0])

    @abstractmethod
    def load(self, *args, **kwargs):
        """
        This method is *abstract* - subclasses of DataBase have to implement it.
        We indicate this with the `@abstractmethod` decorator before the function.

        :param *args: Any other non-keyword arguments added in subclasses.
        :param **kwargs: Any other keyword arguments added in subclasses.
        """
        raise NotImplementedError
