from abc import ABC, abstractmethod

import numpy as np
from numpy.typing import ArrayLike


class DataBase(ABC):
    """
    Base class that standardises the interface for loading data.
    """
    def __init__(self) -> None:
        """
        We declare the values in the initialiser to be a numpy array.
        The typing is optional here, but if we use it our IDE will warn us
        if we try to overwrite the values with a non-array.
        """
        self.values: ArrayLike = np.zeros([0])

    @abstractmethod
    def load(self, *args, **kwargs):
        """
        This method is *abstract* - subclasses of DataBase have to implement it.
        We indicate this with the `@abstractmethod` decorator before the function.
        The arguments use Python magic which means 'any non-keyword argument, any keyword argument'.
        """
        raise NotImplemented("This method has not been implemented!")
