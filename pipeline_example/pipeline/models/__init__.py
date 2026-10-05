from abc import ABC, abstractmethod

import numpy as np
from numpy.typing import ArrayLike


class ModelBase(ABC):
    """
    Base class that standardises the interface for fitting models to data.
    """
    @abstractmethod
    def fit(self, *args, **kwargs) -> ArrayLike:
        """
        This method is *abstract* - subclasses of ModelBase have to implement it.
        We indicate this with the `@abstractmethod` decorator before the function.
        The arguments use Python magic which means 'any non-keyword argument, any keyword argument'.

        We're going to type hint what this function returns, too, with `-> ArrayLike`,
        to make it clear this should
        """
        raise NotImplemented("This method has not been implemented!")
