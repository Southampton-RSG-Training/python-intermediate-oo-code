import numpy as np
import scipy.optimize as spo

from pipeline.data import DataBase
from pipeline.models import ModelBase


class ModelCosine(ModelBase):
    """
    We know our data is a cosine wave, so we'll try to fit a cosine wave to it.
    """
    def fit(self, data: DataBase) -> np.ndarray:
        """
        We're going to fit a cosine wave, but we don't know the wavelength or height,
        or if there's an offset to the data.

        You don't need to think about the contents of this - I wrote it in a hurry!

        :param data: The data to fit.
        :return: The best fit of this model to the data.
        """

        def model_equation(x, offset, wavelength, height):
            """
            So this is the equation we're fitting.
            The form of it is set by SciPy optimise - don't think about it too much.
            """
            return np.cos((x + offset) / wavelength) * height

        def model_error(optimisation_params):
            """
            This is just a basic least squares.
            """
            offset, wavelength, height = optimisation_params
            return np.sum((model_equation(data.x, offset, wavelength, height) - data.y)**2)

        initial_guess = [0, 2, 0.5]
        result = spo.minimize(model_error, initial_guess)
        offset, wavelength, height = result.x

        return model_equation(data.x, offset, wavelength, height)
