from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from pipeline.analysis import Analysis
from pipeline.plots import PlotBase


class PlotLine(PlotBase):
    """
    Class for plotting a simple line plot.
    """
    @classmethod
    def from_analysis(cls: type, analysis: Analysis) -> Figure:
        """
        Simple line plot of the fit on the data used for it.

        :param analysis: The analysis to plot.
        :return: The figure we've just made.
        """
        fig, ax = plt.subplots()
        ax.set_title(f"{analysis.title} model comparison")
        ax.scatter(analysis.data.x, analysis.data.y, label="Data", marker='o')
        ax.scatter(analysis.data.x, analysis.results, label="Fit", marker='x')
        ax.legend()
        fig.show()
        fig.savefig(f"{analysis.title.lower().replace(' ', '-')}-line.png")
        return fig
