import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from pipeline.analysis import Analysis
from pipeline.plots import PlotBase


class PlotError(PlotBase):
    """
    Class for plotting the fractional error.
    """
    @classmethod
    def from_analysis(cls: type, analysis: Analysis) -> Figure:
        """
        Plots the error of the model fit to the data,
        in both absolute, and fractional RMS.

        :param analysis: The analysis to plot.
        :return: The figure we've just made.
        """
        fig, ax = plt.subplots()
        ax2 = ax.twinx()
        ax.set_title(f"{analysis.title} model errors")
        ax.set_ylabel("Absolute error")
        ax2.set_ylabel("Fractional RMS error")

        absolute_error = analysis.data.y - analysis.results
        frms_error = absolute_error / np.sqrt(analysis.data.y**2)

        ax.scatter(analysis.data.x, absolute_error, marker='o', label="Absolute")
        ax2.scatter(analysis.data.x, frms_error, marker='x', color='orange', label="FRMS")
        fig.legend()
        fig.show()
        fig.savefig(f"{analysis.title.lower().replace(' ', '-')}-err.png")
        return fig
