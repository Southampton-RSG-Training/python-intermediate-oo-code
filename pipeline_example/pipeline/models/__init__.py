from abc import ABC, abstractmethod

import numpy as np

from pipeline.data import DataBase


class ModelBase(ABC):
    """
    Base class that standardises the interface for fitting models to data.
    """
    @abstractmethod
    def fit(self, data: DataBase, *args, **kwargs) -> np.ndarray:
        """
        This method is *abstract* - subclasses of ModelBase have to implement it.
        We indicate this with the `@abstractmethod` decorator before the function.
        We'll also document it in a standard docstring format.
        Abstract models with clear documentation make it really easy to expand from.

        :param data: The standard data to fit.
        :param *args: Any other non-keyword arguments added in subclasses.
        :param **kwargs: Any other keyword arguments added in subclasses.
        :return: The y-values of the best-fit model.
        """
        raise NotImplementedError
