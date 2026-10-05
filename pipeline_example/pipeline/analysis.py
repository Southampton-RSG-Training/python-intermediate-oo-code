from typing import TYPE_CHECKING

import numpy as np

# As we'd get circular import problems otherwise,
# we only load the classes for type checking *when* we are type checking.
if TYPE_CHECKING:
    from pipeline.data import DataBase
    from pipeline.models import ModelBase
    from pipeline.plots import PlotBase


class Analysis:
    """
    This class ties together the whole pipeline.
    """
    def __init__(
            self,
            title: str,
            data: 'DataBase',
            model: 'ModelBase',
            plots: list['type[PlotBase]']
    ):
        """
        Initialises the class by recording all the components of the pipeline on it,
        to call later.

        We type hint the arguments in quotes - this means they're checked properly,
        but it doesn't throw an error when we're running and they aren't imported.

        The plots are expected to be classes, not objects, so we have to use 'type' on the hint.
        """
        self.title = title
        self.data = data
        self.model = model
        self.plots = plots
        self.results: np.ndarray = np.zeros([0])

    def run(self):
        """
        Wraps together the whole pipeline and runs it.
        """
        self.data.load()
        self.results = self.model.fit(self.data)
        for plot in self.plots:
            plot.from_analysis(self)
