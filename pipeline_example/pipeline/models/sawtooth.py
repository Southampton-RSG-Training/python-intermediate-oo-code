import numpy as np
import scipy.optimize as spo
import scipy.signal as sps

from pipeline.data import DataBase
from pipeline.models import ModelBase


class ModelSawtooth(ModelBase):
    """
    We know our data is a cosine wave, so we'll make a very bad model of it as a triangle wave.
    """

    def __init__(self, width: float = 0.5):
        """
        Initialises the model. This takes a parameter, which we save to it.

        :param width: Part of the scipy sawtooth, what fraction of 1 period is up vs down.
        """
        self.width = width

    def fit(self, data: DataBase) -> np.ndarray:
        """
        We're going to fit a sawtooth wave, but we don't know the wavelength or height,
        or if there's an offset to the data.

        You don't need to think about the contents of this - I wrote it in a hurry!

        :param data: The data to fit.
        :returns: The best fit to that data with this model.
        """

        def model_equation(x, offset, wavelength, height):
            """
            So this is the equation we're fitting.
            It's a sawtooth wave, except the scipy version goes up then down
            unlike cos so for ease of fitting, we flip the height.
            """
            return sps.sawtooth((x + offset) / wavelength, self.width) * -height

        def model_error(optimisation_params):
            """
            This is just a basic least squares.
            You can probably get scipy to do this bit for you?
            """
            offset, wavelength, height = optimisation_params
            return np.sum((model_equation(data.x, offset, wavelength, height) - data.y)**2)

        initial_guess = [0, 1, 1]  # This should probably be set in the init somewhere!
        result = spo.minimize(model_error, initial_guess)
        offset, wavelength, height = result.x

        return model_equation(data.x, offset, wavelength, height)
