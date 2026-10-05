from abc import ABC, abstractmethod
from matplotlib.figure import Figure

from pipeline.analysis import Analysis


class PlotBase(ABC):
    """
    Base class that standardises the interface for plotting model fits.
    """
    @classmethod
    @abstractmethod
    def from_analysis(cls: type, analysis: Analysis) -> Figure:
        """
        This method is *abstract* - subclasses of ModelBase have to implement it.
        We indicate this with the `@abstractmethod` decorator before the function.

        It's also a class method - we don't actually want to store any data on a plot object,
        so the method exists only as part of the plot *class*.
        You don't even need to declare an instance of a plot object to use it.

        This is basically useful for situations where you want to use a Class to define an interface.

        :param cls: This class. Standard for classmethods.
        :param analysis: The analysis to plot.
        :returns: The plotted figure, in case the user wants to edit it more.
        """
        raise NotImplementedError
